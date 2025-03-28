from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
import database, schemas
import jwt
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import joblib

# Secret key for JWT encoding/decoding
SECRET_KEY = "mysecretkey"  # Keep this secret!
ALGORITHM = "HS256"

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer instance to extract token from the Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Helper function to verify the password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Helper function to create JWT token
def create_jwt_token(username: str):
    expiration = datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    payload = {
        "sub": username,
        "exp": expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Dependency to extract user from JWT
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Could not validate credentials")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token has expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

# Login endpoint
@app.post("/login/")
def login(user: schemas.LoginRequest, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(database.User).filter(database.User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Verify the password
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create JWT token
    token = create_jwt_token(db_user.username)

    return {"access_token": token, "token_type": "bearer"}

# Example protected route
@app.get("/protected/")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}! This is a protected route."}

# Create a new customer
@app.post("/create_customer/")
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(customer.password)
    db_customer = database.Customer(
        username=customer.username,
        hashed_password=hashed_password,
        location=customer.location,
        email=customer.email,
        role="customer",  # Explicitly set the role as 'customer'
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Endpoint to place an order (requires authentication)
@app.post("/place_order/")
def place_order(
    order: schemas.OrderCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    # Decode token and get the current user (customer)
    username = get_current_user(token)
    customer = db.query(database.Customer).filter(database.Customer.username == username).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    try:
        # Create a new order with a timestamp
        db_order = database.Order(
            customer_id=customer.id,
            menu_name=order.menu_name,
            menu_details=order.menu_details,
            price=order.price,
            date=datetime.utcnow()  # Automatically set current timestamp
        )

        db.add(db_order)
        db.commit()
        db.refresh(db_order)

        return {
            "order_id": db_order.id,
            "customer_id": db_order.customer_id,
            "menu_name": db_order.menu_name,
            "menu_details": db_order.menu_details,
            "price": db_order.price,
            "date": db_order.date
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Order placement failed: {str(e)}")

    finally:
        db.close()

# Endpoint to get all orders
@app.get("/get_orders/")
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(database.Order).all()
    return orders

# Endpoint to get all customers
@app.get("/get_all_customers/")
def get_all_customers(db: Session = Depends(get_db)):
    db_customers = db.query(database.Customer).all()
    if not db_customers:
        raise HTTPException(status_code=404, detail="No customers found")
    return db_customers


def recommend_menu(customer_id, date, location, top_n=3):
    artifacts = joblib.load('ml_model/menu_recommender.joblib')
    model = artifacts['model']
    le = artifacts['label_encoders']

    date = pd.to_datetime(date)
    features = {
        'month': date.month,
        'day_of_week': date.dayofweek,
        'is_weekend': int(date.dayofweek in [5, 6]),
        'price_tier': 1,
        'cust_order_freq': artifacts['cust_order_count'].get(customer_id, 1),
        'loc_menu_count': artifacts['loc_menu_pop'].get((location, ''), 1),
        'location': le['location'].transform([location])[0]
    }

    X = pd.DataFrame([features])
    probs = model.predict_proba(X)[0]
    top_indices = np.argsort(probs)[-top_n:][::-1]

    recommendations = []
    for idx in top_indices:
        menu_id = model.classes_[idx]
        menu_name = le['menu_name'].inverse_transform([menu_id])[0]
        confidence = probs[idx] * 10
        recommendations.append({"menu_name": menu_name, "confidence": float(confidence)})

    return recommendations


@app.post("/recommend")
def get_recommendation(request: dict):
    customer_id = request.get("customer_id")
    date = request.get("date")
    location = request.get("location")
    if not all([customer_id, date, location]):
        raise HTTPException(status_code=400, detail="Missing required parameters")

    recommendations = recommend_menu(customer_id, date, location)
    return {"recommended_menu": recommendations}


# Custom OpenAPI Schema to modify Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My API",
        version="1.0.0",
        description="This API uses JWT tokens for authentication. Obtain a token by sending a POST request to `/login/`. Use the format `Bearer <your-token>` in the Authorization header for authenticated endpoints.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"]["OAuth2PasswordBearer"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "Paste your token in the format 'Bearer <your-token>' to authenticate."
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            if "security" in method:
                method["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
