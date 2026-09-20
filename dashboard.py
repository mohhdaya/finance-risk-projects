import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Equity Valuation Dashboard", layout="wide")
st.title("Equity Valuation Dashboard")

ticker = st.selectbox("Select Stock", ["HDFCBANK.NS", "RELIANCE.NS", "INFY.NS", "TATAMOTORS.NS", "SBIN.NS"])
info = yf.Ticker(ticker).info

c1, c2, c3, c4 = st.columns(4)
c1.metric("P/E", round(info.get("trailingPE") or 0, 2))
c2.metric("P/B", round(info.get("priceToBook") or 0, 2))
roe = (info.get("returnOnEquity") or 0) * 100
c3.metric("ROE", f"{roe:.2f}%")
c4.metric("Market Cap", f"Rs.{(info.get('marketCap') or 0)/1e12:.2f}L Cr")

hist = yf.download(ticker, period="1y", auto_adjust=True)["Close"]
st.line_chart(hist)
pe = info.get("trailingPE") or 25
if pe < 22:
    verdict = "UNDERVALUED - Buy zone"
elif pe > 30:
    verdict = "OVERVALUED - Caution"
else:
    verdict = "FAIRLY VALUED - Hold"
st.success("Verdict: " + verdict)
