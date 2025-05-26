import requests
from utils.config import ALPHA_VANTAGE_API_KEY

def ticker_news(ticker):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "feed" in data:
        return [article["title"] for article in data["feed"][:5]]
    return ["No news available."]