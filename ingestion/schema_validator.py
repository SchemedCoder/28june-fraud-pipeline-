import pandas as pd

df = pd.read_csv("data/transactions.csv")

required_columns = [
    "transaction_id",
    "customer_id",
    "merchant_id",
    "amount",
    "transaction_time",
    "city",
    "payment_method",
    "is_fraud"
]

missing = []

for col in required_columns:
    if col not in df.columns:
        missing.append(col)

if missing:
    print("Missing columns:", missing)
else:
    print("Schema validation passed")
