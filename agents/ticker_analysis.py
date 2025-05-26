from agents.ticker_news import ticker_news
from agents.ticker_price_change import ticker_price_change

def ticker_analysis(ticker):
    news = ticker_news(ticker)
    price_change = ticker_price_change(ticker)
    summary = f"{ticker} moved {price_change}% recently. Possible reasons:
"
    summary += "\n".join(["- " + item for item in news])
    return summary