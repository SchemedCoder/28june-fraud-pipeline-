import pandas as pd
import random
from datetime import datetime, timedelta

customers = [f"C{str(i).zfill(3)}" for i in range(1, 11)]
merchants = [f"M{str(i).zfill(3)}" for i in range(1, 11)]
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad"]
payment_methods = ["UPI", "Card", "Wallet"]

rows = []

base_time = datetime.now()

for i in range(200):
    amount = random.randint(100, 100000)

    fraud = 1 if amount > 40000 else 0

    rows.append({
        "transaction_id": f"T{str(i+1).zfill(4)}",
        "customer_id": random.choice(customers),
        "merchant_id": random.choice(merchants),
        "amount": amount,
        "transaction_time": base_time + timedelta(seconds=i),
        "city": random.choice(cities),
        "payment_method": random.choice(payment_methods),
        "is_fraud": fraud
    })

df = pd.DataFrame(rows)
df.to_csv("data/generated_transactions.csv", index=False)

print("Synthetic transactions generated.")
