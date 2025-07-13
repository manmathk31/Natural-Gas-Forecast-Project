# Natural Gas Price Forecasting

This project is part of the **JPMorgan Chase & Co. Quantitative Research Virtual Experience Program** on Forage.

It demonstrates how to use historical natural gas price data to:

- Analyze seasonal pricing patterns 📊
- Forecast future prices for the next 12 months 📈
- Predict the price of gas for any given date using a trained regression model 🤖

---

## 🧠 Project Objectives

- Load and visualize natural gas price data (Oct 2020 – Sep 2024)
- Understand seasonal effects on pricing (e.g., summer vs winter)
- Train a regression model to predict prices based on date & month
- Allow users to input a custom date and return estimated price
- Extrapolate price forecast for an extra 1 year

---

## 📁 Files Included

## 📁 Files Included

| File                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `natural_gas_forecast.py`| Python script for loading data, training the model, making predictions, and plotting results |
| `Nat_Gas.csv`            | Historical natural gas prices from October 2020 to September 2024          |


## 📌 Features

- Uses `pandas` for data handling
- Uses `matplotlib` for plotting seasonal trends and predictions
- Uses `scikit-learn` for regression modeling
- Accepts any date as input and returns estimated price
- Plots both historical and extrapolated future prices

---

## 🔧 Requirements

Make sure you have Python 3 installed.

To install all necessary dependencies, run:

```bash
pip install -r requirements.txt

