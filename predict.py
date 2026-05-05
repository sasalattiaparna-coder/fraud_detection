import joblib

model = joblib.load("fraud_model.pkl")

def predict_fraud(amount, device_risk, ip_risk, is_international):
    pred = model.predict([[amount, device_risk, ip_risk, is_international]])[0]
    prob = model.predict_proba([[amount, device_risk, ip_risk, is_international]])[0][1]

    return pred, round(prob, 2)