import pandas as pd


# ==========================================
# LOAD DATA
# ==========================================

transactions = pd.read_csv("data/transactions.csv")
customers = pd.read_csv("data/customers.csv")
merchants = pd.read_csv("data/merchants.csv")


# ==========================================
# JOIN DATASETS
# ==========================================

df = transactions.merge(
    customers,
    on="customer_id",
    how="left"
)

df = df.merge(
    merchants,
    on="merchant_id",
    how="left"
)


# ==========================================
# FEATURE 1: AMOUNT ANOMALY
# ==========================================

df["amount_anomaly_ratio"] = (
    df["amount"] / df["avg_transaction_amount"]
)


# ==========================================
# FEATURE 2: LOCATION MISMATCH
# ==========================================

df["location_mismatch"] = (
    df["city_x"] != df["city_y"]
).astype(int)


# ==========================================
# FEATURE 3: MERCHANT RISK SCORE
# ==========================================

risk_map = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3
}

df["merchant_risk_score"] = (
    df["risk_level"]
    .map(risk_map)
)


# ==========================================
# FEATURE 4: PAYMENT RISK SCORE
# ==========================================

payment_map = {
    "UPI": 1,
    "Wallet": 2,
    "Card": 3
}

df["payment_risk_score"] = (
    df["payment_method"]
    .map(payment_map)
)


# ==========================================
# FEATURE 5: TRANSACTION VELOCITY
# ==========================================

velocity = (
    df.groupby("customer_id")
      .cumcount() + 1
)

df["transaction_velocity"] = velocity


# ==========================================
# FEATURE 6: FRAUD RISK SCORE
# ==========================================

df["fraud_risk_score"] = (
    df["amount_anomaly_ratio"] * 0.4 +
    df["merchant_risk_score"] * 0.25 +
    df["payment_risk_score"] * 0.15 +
    df["location_mismatch"] * 0.2
)


# ==========================================
# CLEAN COLUMNS
# ==========================================

df = df.rename(
    columns={
        "city_x": "transaction_city",
        "city_y": "customer_city"
    }
)


# ==========================================
# SAVE FEATURES
# ==========================================

df.to_csv(
    "data/fraud_features.csv",
    index=False
)

print(df.head())
print("Fraud features generated successfully.")
