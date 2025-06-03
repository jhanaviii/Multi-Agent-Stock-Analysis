# Multi-Agent Stock Analysis System

## Overview
This project implements a multi-agent system to answer stock-related questions using the Alpha Vantage API and Yahoo Finance.
(internshala assignment)
## Agents
- `identify_ticker`: Parses natural language and detects ticker.
- `ticker_news`: Fetches top 5 stock news.
- `ticker_price`: Gets current stock price.
- `ticker_price_change`: Calculates recent % price change.
- `ticker_analysis`: Combines news + change to explain movement.

## Setup
1. Replace `"YOUR_ALPHA_VANTAGE_API_KEY"` in `utils/config.py`
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run:
```
python main.py
```

## Sample Queries
- "Why did Tesla stock drop today?"
- "What’s happening with Palantir stock recently?"
- "How has Nvidia stock changed in the last 7 days?"
- "What is the current price of Apple stock?"

## Demo Video
Demo shows real-time agent responses for each query.
