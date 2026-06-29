import pandas as pd
import joblib

model = joblib.load("ml/fraud_model.pkl")
df = pd.read_csv("data/fraud_features.csv")

features = [
    "amount_anomaly_ratio",
    "merchant_risk_score",
    "payment_risk_score",
    "location_mismatch",
    "transaction_velocity",
    "fraud_risk_score"
]

alerts = []

for _, row in df.iterrows():

    sample = pd.DataFrame([row[features]])
    probability = model.predict_proba(sample)[0][1]

    if probability > 0.85:
        alerts.append({
            "transaction_id": row["transaction_id"],
            "fraud_probability": probability
        })

alerts_df = pd.DataFrame(alerts)
alerts_df.to_csv("data/fraud_alerts.csv", index=False)

print(alerts_df)
