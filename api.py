from fastapi import FastAPI
from predict import predict_fraud

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.get("/predict")
def predict(amount: float, device_risk: int, ip_risk: int, is_international: int):
    pred, prob = predict_fraud(amount, device_risk, ip_risk, is_international)

    return {
        "fraud": int(pred),
        "probability": prob
    }