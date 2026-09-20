# finance-risk-projects

Finance + Python projects. PGDM @ SJIM, learning by building.

## Projects
1. **Portfolio Risk Analyzer** (`risk_analyzer.py`) — CAGR, volatility, Sharpe (vs 6.5% risk-free rate), VaR (95%) for Reliance, HDFC Bank, Infosys, TCS (2022-present). Outputs `risk_report.csv` + `portfolio_growth.png`.
2. **Equity Valuation Dashboard** (`dashboard.py`) — Streamlit app: P/E, P/B, ROE + 1yr price chart. Run: `streamlit run dashboard.py`
3. **Nifty Options Payoff** (`options_payoff.py`) — long call / long put / straddle payoff chart + breakevens. Output `options_payoff.png`.
4. **Zomato DCF (simplified)** (`Zomato_DCF.xlsx`) — 5yr DCF with assumptions, teaching model. Fair value ~Rs.53/share (EV Rs.38,784 Cr + net cash Rs.12,000 Cr).

## Run
```bash
pip install yfinance pandas numpy matplotlib streamlit openpyxl
python risk_analyzer.py
python options_payoff.py
streamlit run dashboard.py
```
