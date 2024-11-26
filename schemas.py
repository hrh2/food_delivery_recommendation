from pydantic import BaseModel
from typing import Optional

# Schema for creating users
class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True  # Allow pydantic to handle SQLAlchemy models

# Schema for creating customers
class CustomerCreate(UserCreate):
    email: str
    location: str

    class Config:
        from_attributes = True

# Customer schema (Response schema)
class Customer(BaseModel):
    id: int
    username: str
    location: str
    email: str
    role: str

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str
    password: str

# Base schema for an order
class OrderBase(BaseModel):
    menu_name: str
    menu_details: str
    price: float

    class Config:
        from_attributes = True

# Order schema for creating a new order
class OrderCreate(OrderBase):
    customer_id: int

    class Config:
        from_attributes = True

# Order schema for response (after creation)
class Order(OrderBase):
    id: int
    customer_id: int

    class Config:
        from_attributes = True
