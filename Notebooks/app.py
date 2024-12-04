# Design an API for Real-Time Predictions

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import joblib
import pandas as pd
import numpy as np

# Load the trained model
with open('fraud_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize FastAPI
app = FastAPI()

# Define the API endpoint for predictions
@app.post("/predict")
def predict(features: dict):
    try:
        # Convert input dictionary to DataFrame
        input_data = pd.DataFrame([features])
        
        # Make predictions
        prediction = model.predict(input_data)
        
        return {"fraud_prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in prediction: {str(e)}")