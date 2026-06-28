# 28june-fraud-pipeline-

# Real-Time Fraud Detection Platform

An end-to-end Data Engineering + Machine Learning platform for detecting fraudulent financial transactions in real time.

---

## Problem Statement

Banks, payment gateways, and UPI systems process millions of transactions daily.

Fraud patterns include:

- Card theft
- High-value suspicious transfers
- Rapid repeated transactions
- Impossible location jumps
- Merchant anomalies

Traditional batch detection is slow.

This platform enables near real-time fraud detection.

---

## Architecture

```text
Raw Transactions
      ↓
Bronze Layer
      ↓
Feature Engineering
      ↓
Silver Layer
      ↓
ML Fraud Scoring
      ↓
Gold Alerts
      ↓
Dashboard
```

---

## Tech Stack

- Python
- SQL
- Pandas
- Scikit-learn
- Streamlit
- Kafka (simulation)
- GitHub Actions
- Docker

---

## Key Features

### Data Engineering
- Transaction ingestion
- Data validation
- Feature pipelines
- Fraud alert warehouse

### Machine Learning
- Fraud probability scoring
- Binary fraud classification
- Risk scoring

### Analytics
- High-risk merchants
- Customer fraud patterns
- Alert monitoring

---

## Business Value

Useful for:

- Banks
- Fintech
- UPI providers
- Payment gateways
- Credit card processors
