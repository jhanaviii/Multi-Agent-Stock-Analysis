import yfinance as yf
from datetime import datetime, timedelta

def ticker_price_change(ticker, days=7):
    end = datetime.now()
    start = end - timedelta(days=days)
    df = yf.download(ticker, start=start, end=end)
    if df.empty:
        return "No data"
    start_price = df.iloc[0]["Close"]
    end_price = df.iloc[-1]["Close"]
    change = ((end_price - start_price) / start_price) * 100
    return round(change, 2)