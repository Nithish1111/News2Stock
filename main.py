# This file is the starting point of the program.
# It asks the user for a stock symbol, fetches recent news, and uses AI to analyze that news.

# Import the function that gets recent headlines from Finnhub
from news_fetcher import get_news_headlines

# Import the function that analyzes the sentiment using AI (Cohere)
from ai_analyzer import analyze_sentiment


# Ask the user to type in a stock ticker (like "AAPL" for Apple or "TSLA" for Tesla)
# .upper() makes sure the letters are capitalized (standard format for stock symbols)
symbol = input("Enter a stock symbol (e.g., AAPL, TSLA): ").upper()

# Get the latest news headlines for that stock symbol
headlines = get_news_headlines(symbol)

# If no headlines were returned, show an error message
if not headlines:
    print("❌ Could not fetch news. Check the symbol or API key.")
else:
    # If headlines were found, print them out one by one
    print("\n📰 Latest Headlines:")
    for h in headlines:
        print("- " + h)

    # Let the user know that the AI is now analyzing the headlines
    print("\n🤖 Analyzing sentiment...\n")

    # Use the AI to analyze the sentiment (bullish, bearish, neutral + reasoning)
    result = analyze_sentiment(headlines, symbol)

    # Show the AI's result to the user
    print(result)
