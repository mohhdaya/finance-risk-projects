# options payoff calculator
# by prateek - learning derivatives payoff profiles
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

spot_range = np.linspace(20000, 30000, 200)
strike = 25000
premium_call = 450
premium_put = 380
LOT_SIZE = 65  # Nifty lot size; chart below is per-unit PnL - multiply by LOT_SIZE for per-lot

long_call = np.maximum(spot_range - strike, 0) - premium_call
long_put = np.maximum(strike - spot_range, 0) - premium_put
straddle = (np.maximum(spot_range - strike, 0) + np.maximum(strike - spot_range, 0)) - (premium_call + premium_put)

plt.figure(figsize=(10, 5))
plt.plot(spot_range, long_call, label="Long Call K=25000")
plt.plot(spot_range, long_put, label="Long Put K=25000")
plt.plot(spot_range, straddle, label="Long Straddle", linestyle="--")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(strike, color="grey", linestyle=":", label="Strike")
plt.title("Nifty Options Payoff (expiry, per-unit)")
plt.xlabel("Nifty at expiry")
plt.ylabel("PnL (Rs per unit)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("options_payoff.png", dpi=150)
print("saved options_payoff.png")

# breakevens
print(f"call breakeven: {strike + premium_call}")
print(f"put breakeven: {strike - premium_put}")
print(f"straddle breakevens: {strike - (premium_call+premium_put)} / {strike + (premium_call+premium_put)}")
print(f"note: multiply per-unit PnL by lot size ({LOT_SIZE}) for per-lot PnL")
