from datetime import datetime

from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Float, DateTime
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Base User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="admin")
    type = Column(String)  # Discriminator column (this column stores the type)

    # Remove orders relationship from User and move it to Customer
    __mapper_args__ = {
        "polymorphic_identity": "user",  # Identity for the User model
        "polymorphic_on": type,          # Pointing to the 'type' column for polymorphism
    }

# Derived Customer model
class Customer(User):
    __tablename__ = "customers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)  # FK to users
    email = Column(String, unique=True, index=True)
    location = Column(String)

    # Define the orders relationship on the Customer model instead
    orders = relationship("Order", back_populates="customer")

    __mapper_args__ = {
        "polymorphic_identity": "customer",  # Identity for the Customer model
    }

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))  # ForeignKey referencing Customer
    menu_name = Column(String)
    menu_details = Column(String)
    price = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)  # New date column

    # Define the relationship with the Customer
    customer = relationship("Customer", back_populates="orders")

# Base.metadata.drop_all(bind=engine)
# Create tables
Base.metadata.create_all(bind=engine)
