# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 23:39:29 2025

@author: manmath
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load and clean data
df = pd.read_csv("Nat_Gas.csv")
df.columns = df.columns.str.strip().str.lower()
df['dates'] = pd.to_datetime(df['dates'], format='%m/%d/%y')
df = df.sort_values('dates')
df.set_index('dates', inplace=True)

# Plot historical gas prices
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['prices'], marker='o', linestyle='-', color='blue', label='Historical Price')
plt.title("Natural Gas Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Feature engineering
df['month'] = df.index.month
df['time_index'] = np.arange(len(df))

# Prepare input features
X = pd.get_dummies(df['month'])
X['time_index'] = df['time_index']
X.columns = X.columns.astype(str)
y = df['prices']

# Train model
model = LinearRegression()
model.fit(X, y)

# Function to estimate price
def estimate_price(date_input):
    date = pd.to_datetime(date_input)
    months_since_start = (date.year - df.index[0].year) * 12 + (date.month - df.index[0].month)
    month_dummies = [0] * 12
    month_dummies[date.month - 1] = 1
    features = month_dummies + [months_since_start]
    features_df = pd.DataFrame([features], columns=X.columns)
    predicted = model.predict(features_df)[0]
    return round(predicted, 2)

# Forecast next 12 months
future_dates = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')
future_prices = [estimate_price(d) for d in future_dates]
future_df = pd.DataFrame({'prices': future_prices}, index=future_dates)

# Plot actual + predicted
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['prices'], label="Historical", marker='o')
plt.plot(future_df.index, future_df['prices'], label="Predicted", marker='x', linestyle='--')
plt.title("Natural Gas Price Forecast")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# User input for date prediction
date_input = input("Enter a date (YYYY-MM-DD): ")
try:
    predicted_price = estimate_price(date_input)
    print(f"Estimated Price on {date_input}: {predicted_price}")
except:
    print("Invalid date format. Please use YYYY-MM-DD.")

