import re

def identify_ticker(query):
    tickers = {
        "Tesla": "TSLA",
        "Palantir": "PLTR",
        "Nvidia": "NVDA",
        "Apple": "AAPL",
        "Google": "GOOGL",
        "Microsoft": "MSFT",
    }
    for name, ticker in tickers.items():
        if name.lower() in query.lower():
            return ticker
    # Try direct ticker mention
    match = re.search(r"\b[A-Z]{2,5}\b", query)
    return match.group(0) if match else None