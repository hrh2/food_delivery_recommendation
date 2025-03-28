# Food Delivery Recommendation System
## (From Food Delivery Management System)

This project involves building a machine learning model that provides meal recommendations to customers based on their historical orders. The model uses data from food delivery orders and customer information to predict what meal a customer is likely to order next.

## Project Overview

- **Goal**: Develop a recommendation system for customers based on historical order data.
- **Data Source**: Orders and customer information obtained from a FastAPI endpoint.
- **Model**: RandomForestClassifier for predicting menu recommendations.
- **Challenges**: The model currently struggles to generalize well but will be improved through better data preprocessing and feature engineering.

## Steps Taken

### 1. Data Collection
- Fetched order data and customer details via API requests.
- Merged both datasets on `customer_id` to create a complete dataset.

### 2. Data Preprocessing
- Dropped irrelevant columns (e.g., email, username, role, etc.).
- Converted date fields into relevant time-based features (month, day of the week, weekend indicator).
- Categorized price into three tiers: Low, Medium, High.
- Calculated customer order frequency and menu popularity per location.

### 3. Data Encoding
- Applied Label Encoding to categorical features such as `menu_name`, `location`, and `price_tier`.

### 4. Model Training
- Split data into training and testing sets.
- Used a **RandomForestClassifier** to train the model on historical customer orders.
- Evaluated performance using classification metrics.

### 5. Model Deployment (Ongoing)
- The model is planned to be integrated into a FastAPI route to serve recommendations.
- Currently testing the API response and ensuring the model outputs relevant predictions.

## API Integration
The trained model is exposed via FastAPI under the `/ml_model` route in the backend of the food delivery management system. Customers can get meal recommendations by sending a request with their `customer_id` and `date`.

### API Endpoint
**URL:** `POST /ml_model/recommend`

**Request Format:**
```json
{
  "customer_id": 123,
  "date": "2025-03-28",
  "location": "Rulindo"
}
```

**Response Format:**
```json
{
  "recommended_menu": [
    { "menu_name": "Grilled Chicken with Rice", "confidence": 0.85 },
    { "menu_name": "Pasta Alfredo", "confidence": 0.75 },
    { "menu_name": "Beef Burger", "confidence": 0.68 }
  ]
}
```

## Setup and Usage
### Clone the Repository
```sh
git https://github.com/hrh2/food_delivery_recommendation.git
cd food_delivery_recommendation
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the FastAPI Application
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000/docs` for interactive testing.

## Challenges Faced
- **Generalization Issues**: The model struggles to make accurate predictions for new users or uncommon orders.
- **Feature Selection**: Some features may not contribute significantly to recommendation accuracy.
- **Data Imbalance**: Some menu items are ordered significantly more than others, leading to biased predictions.

## Next Steps
- **Improve Data Preprocessing**: Perform feature scaling and transformation for better generalization.
- **Hyperparameter Tuning**: Experiment with different configurations of the RandomForest model.
- **Try Different Models**: Consider collaborative filtering or deep learning-based recommendation systems.
- **Improve API Integration**: Ensure smooth communication between the FastAPI backend and the model.
- **Deploy and Monitor**: Deploy the API and collect feedback to improve the recommendation system over time.

---
This documentation will be updated as improvements are made to the model and API integration. 🚀

