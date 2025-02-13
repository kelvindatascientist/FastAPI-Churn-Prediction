# Churn Prediction API

This project provides a Dockerized FastAPI application to predict customer churn using a Logistic Regression model. 

## Features
- Predicts whether a customer will churn (1) or not (0).
- Simple **POST** endpoint for inference.

## Project Structure
- `app/main.py` : Contains the FastAPI application code.
- `models/churn_model.pkl` : Pre-trained logistic regression model.
- `requirements.txt` : Python dependencies.
- `Dockerfile` : Instructions for building the Docker image.

## How To Use

1. **Train the model** (if needed):
   ```bash
   python train_model.py