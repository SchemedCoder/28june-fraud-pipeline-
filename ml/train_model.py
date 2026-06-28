import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# ==========================================
# LOAD FEATURE DATA
# ==========================================

df = pd.read_csv("data/fraud_features.csv")


# ==========================================
# SELECT FEATURES
# ==========================================

features = [
    "amount_anomaly_ratio",
    "merchant_risk_score",
    "payment_risk_score",
    "location_mismatch",
    "transaction_velocity",
    "fraud_risk_score"
]

X = df[features]
y = df["is_fraud"]


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# TRAIN MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)


# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "ml/fraud_model.pkl"
)

print("Fraud model trained successfully.")
