import pandas as pd
import time

df = pd.read_csv("data/transactions.csv")

for _, row in df.iterrows():
    print("Publishing transaction:", row["transaction_id"])
    time.sleep(1)
