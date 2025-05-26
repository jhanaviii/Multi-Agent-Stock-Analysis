from agents.identify_ticker import identify_ticker
from agents.ticker_price import ticker_price
from agents.ticker_news import ticker_news
from agents.ticker_price_change import ticker_price_change
from agents.ticker_analysis import ticker_analysis

def handle_query(query):
    ticker = identify_ticker(query)
    if not ticker:
        return "Sorry, could not identify the stock."

    if "price change" in query or "changed" in query:
        return f"{ticker} price change: {ticker_price_change(ticker)}%"
    elif "news" in query:
        return "\n".join(ticker_news(ticker))
    elif "price" in query:
        return f"{ticker} current price: ${ticker_price(ticker)}"
    else:
        return ticker_analysis(ticker)

if __name__ == "__main__":
    sample_queries = [
        "Why did Tesla stock drop today?",
        "What’s happening with Palantir stock recently?",
        "How has Nvidia stock changed in the last 7 days?",
        "What is the current price of Apple stock?"
    ]
    for q in sample_queries:
        print(f"Query: {q}")
        print(handle_query(q))
        print("-" * 60)