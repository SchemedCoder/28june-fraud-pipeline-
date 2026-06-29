import pandas as pd

transactions = pd.read_csv("data/transactions.csv")
customers = pd.read_csv("data/customers.csv")
merchants = pd.read_csv("data/merchants.csv")

print("Transactions:", transactions.shape)
print("Customers:", customers.shape)
print("Merchants:", merchants.shape)
