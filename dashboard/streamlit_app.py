import os
import subprocess
import joblib
import pandas as pd
import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Fraud Detection Platform",
    layout="wide"
)

st.title("🚨 Real-Time Fraud Detection Platform")
st.write("Monitor suspicious transactions using Machine Learning")

# ==========================================
# AUTO TRAIN MODEL
# ==========================================

model_path = "ml/fraud_model.pkl"

if not os.path.exists(model_path):
    st.warning("Fraud model missing. Training...")
    subprocess.run(["python", "ml/train_model.py"])

model = joblib.load(model_path)

# ==========================================
# USER INPUTS
# ==========================================

amount = st.number_input(
    "Transaction Amount (₹)",
    min_value=1.0,
    value=5000.0
)

merchant_risk = st.selectbox(
    "Merchant Risk",
    [1, 2, 3]
)

payment_risk = st.selectbox(
    "Payment Risk",
    [1, 2, 3]
)

location_mismatch = st.selectbox(
    "Location Mismatch",
    [0, 1]
)

transaction_velocity = st.slider(
    "Transactions in Session",
    1,
    20,
    3
)

avg_amount = st.number_input(
    "Customer Avg Transaction Amount",
    min_value=1.0,
    value=1000.0
)

# ==========================================
# PREDICTION
# ==========================================

if st.button("Check Fraud Risk"):

    anomaly_ratio = amount / avg_amount

    fraud_score = (
        anomaly_ratio * 0.4 +
        merchant_risk * 0.25 +
        payment_risk * 0.15 +
        location_mismatch * 0.2
    )

    sample = pd.DataFrame([{
        "amount_anomaly_ratio": anomaly_ratio,
        "merchant_risk_score": merchant_risk,
        "payment_risk_score": payment_risk,
        "location_mismatch": location_mismatch,
        "transaction_velocity": transaction_velocity,
        "fraud_risk_score": fraud_score
    }])

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    probability_percent = round(probability * 100, 2)

    if probability_percent >= 85:
        risk = "HIGH"
    elif probability_percent >= 50:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    if prediction == 1:
        st.error(f"⚠ Fraud Detected ({risk} Risk)")
    else:
        st.success("✓ Legit Transaction")

    st.metric("Fraud Probability", f"{probability_percent}%")
    st.metric("Risk Score", round(fraud_score, 2))

# ==========================================
# SAMPLE ALERT TABLE
# ==========================================

st.subheader("Recent Fraud Alerts")

alerts = pd.DataFrame({
    "transaction_id": ["T003", "T005", "T011"],
    "customer_id": ["C003", "C005", "C001"],
    "fraud_probability": [96.2, 98.4, 91.1],
    "risk_level": ["HIGH", "HIGH", "MEDIUM"],
    "status": ["OPEN", "OPEN", "UNDER_REVIEW"]
})

st.dataframe(alerts)
