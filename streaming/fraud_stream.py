import pandas as pd
import joblib
import os
import subprocess

model_path = "ml/fraud_model.pkl"

if not os.path.exists(model_path):
    subprocess.run(["python", "ml/train_model.py"])

model = joblib.load(model_path)

df = pd.read_csv("data/fraud_features.csv")

features = [
    "amount_anomaly_ratio",
    "merchant_risk_score",
    "payment_risk_score",
    "location_mismatch",
    "transaction_velocity",
    "fraud_risk_score"
]

for _, row in df.iterrows():

    sample = pd.DataFrame([row[features]])

    pred = model.predict(sample)[0]
    prob = model.predict_proba(sample)[0][1]

    status = "FRAUD" if pred == 1 else "SAFE"

    print(
        row["transaction_id"],
        status,
        round(prob * 100, 2)
    )
