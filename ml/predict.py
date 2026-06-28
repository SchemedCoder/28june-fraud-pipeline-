import os
import subprocess
import joblib
import pandas as pd


model_path = "ml/fraud_model.pkl"

# ==========================================
# AUTO-TRAIN IF MISSING
# ==========================================

if not os.path.exists(model_path):
    print("Fraud model missing. Training...")
    subprocess.run(["python", "ml/train_model.py"])


# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(model_path)


# ==========================================
# SAMPLE TRANSACTION
# ==========================================

sample = pd.DataFrame([{
    "amount_anomaly_ratio": 25.0,
    "merchant_risk_score": 3,
    "payment_risk_score": 3,
    "location_mismatch": 1,
    "transaction_velocity": 7,
    "fraud_risk_score": 11.5
}])


prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0][1]

status = "FRAUD" if prediction == 1 else "LEGIT"

print("Prediction:", status)
print("Fraud Probability:", round(probability * 100, 2), "%")
