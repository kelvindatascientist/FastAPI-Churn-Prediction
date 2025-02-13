from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Define request body model
class ChurnFeatures(BaseModel):
    tenure: float
    monthly_charges: float
    contract_type: int

app = FastAPI(title="Churn Prediction API", version="1.0")

# Load the pre-trained model
with open("models/churn_model.pkl", "rb") as f:
    churn_model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Churn Prediction API!"}

@app.post("/predict")
def predict_churn(features: ChurnFeatures):
    """
    Predict if a customer will churn (1) or not (0).
    """
    data = np.array([
        [
            features.tenure, 
            features.monthly_charges, 
            features.contract_type
        ]
    ])

    prediction = churn_model.predict(data)
    predicted_class = int(prediction[0])  # 0 or 1

    return {
        "prediction": predicted_class,
        "explanation": "1 means the model predicts churn, 0 means no churn."
    }
