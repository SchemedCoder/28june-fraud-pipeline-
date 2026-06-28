import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv("data/fraud_features.csv")

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


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load("ml/fraud_model.pkl")

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))
