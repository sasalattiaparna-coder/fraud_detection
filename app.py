import streamlit as st
from predict import predict_fraud

st.title("💳 Fraud Detection System")

amount = st.number_input("Transaction Amount", 10.0, 10000.0)
device_risk = st.slider("Device Risk Score", 1, 100)
ip_risk = st.slider("IP Risk Score", 1, 100)
is_international = st.selectbox("International Transaction", [0, 1])

if st.button("Check Fraud"):
    pred, prob = predict_fraud(amount, device_risk, ip_risk, is_international)

    if pred == 1:
        st.error(f"⚠️ Fraud Detected! Probability: {prob}")
    else:
        st.success(f"✅ Safe Transaction. Probability: {prob}")