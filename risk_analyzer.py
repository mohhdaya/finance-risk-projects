# portfolio risk analyzer - nifty heavyweights
# by Prateek - built for learning risk metrics
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

stocks = ["RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "TCS.NS"]
START = "2022-01-01"
RF_ANNUAL = 0.065  # India 91-day T-bill approx; adjust as needed

print("Downloading data...")
data = yf.download(stocks, start=START, auto_adjust=True)["Close"]
returns = data.pct_change().dropna()

# risk-free daily rate for Sharpe
rf_daily = (1 + RF_ANNUAL) ** (1 / 252) - 1

sharpe = (returns.mean() - rf_daily) / returns.std() * np.sqrt(252)
vol = returns.std() * np.sqrt(252)
var_95 = -returns.quantile(0.05)  # positive loss number (convention)
cagr = (1 + returns).prod() ** (252 / len(returns)) - 1

print("\n=== RISK REPORT ===")
summary = pd.DataFrame({"CAGR": cagr, "Annual Vol": vol, "Sharpe": sharpe, "VaR_95_daily": var_95})
print(summary.round(4).to_string())
summary.round(4).to_csv("risk_report.csv")
print("\nSaved: risk_report.csv")

# cumulative growth chart
(1 + returns).cumprod().plot(figsize=(10, 5), title="Portfolio Growth - Nifty Heavyweights (Rs.1 invested)")
plt.ylabel("Growth of Rs.1")
plt.grid(True)
plt.tight_layout()
plt.savefig("portfolio_growth.png", dpi=150)
print("Saved chart: portfolio_growth.png")
