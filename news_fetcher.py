# This file is responsible for getting recent news headlines about a stock (like Tesla or Apple)

# This library lets us make requests to websites or APIs
import requests

# These are used to safely get your API key from your .env file
import os
from dotenv import load_dotenv

# These help us calculate the date range (from today and a week ago)
from datetime import datetime, timedelta

# Load the environment variables from the .env file (especially the API key)
load_dotenv()

# Get your Finnhub API key from the environment and store it in a variable
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")


# This function fetches recent news headlines for a given stock symbol (like "TSLA")
# `limit=5` means it will return up to 5 headlines
def get_news_headlines(symbol, limit=5):
    if not FINNHUB_API_KEY:
        print("❌ API key is missing. Check your .env file.")
        return []

    today = datetime.today().date()
    last_week = today - timedelta(days=7)

    url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from={last_week}&to={today}&token={FINNHUB_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Finnhub error:", response.status_code, response.text)
        return []

    news = response.json()
    if not news:
        print("⚠️ No news found for this stock in the last 7 days.")
        return []

    # 🔁 Return a list of dictionaries with both headline and URL
    headlines = [{"headline": item['headline'], "url": item['url']} for item in news[:limit]]
    return headlines
