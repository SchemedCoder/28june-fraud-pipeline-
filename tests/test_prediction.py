import joblib
import pandas as pd


def test_prediction_output():
    model = joblib.load("ml/fraud_model.pkl")

    sample = pd.DataFrame([{
        "amount_anomaly_ratio": 20,
        "merchant_risk_score": 3,
        "payment_risk_score": 3,
        "location_mismatch": 1,
        "transaction_velocity": 5,
        "fraud_risk_score": 9.2
    }])

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    assert prediction in [0, 1]
    assert 0 <= probability <= 1
