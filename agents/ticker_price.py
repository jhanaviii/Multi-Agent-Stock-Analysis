import yfinance as yf

def ticker_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.info.get("regularMarketPrice", "Price unavailable")