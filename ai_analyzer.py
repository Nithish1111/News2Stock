# This file uses an AI model from Cohere to analyze the news and decide if a stock looks good or bad to invest in.

# Load the Cohere AI library (lets us talk to the AI model)
import cohere

# These help us access the API key from a file
import os
from dotenv import load_dotenv

# Load the .env file where we stored our API keys safely
load_dotenv()

# Connect to Cohere using your secret API key from the .env file
co = cohere.Client(os.getenv("COHERE_API_KEY"))


# This function takes in a list of news headlines and a stock symbol (like 'TSLA')
# It asks the AI to give a detailed opinion about that stock
def analyze_sentiment(headlines, symbol):
    # If the list of headlines is empty, there's nothing to analyze, so we return a message
    if not headlines:
        return "No headlines found for analysis."

    # This is the actual instruction we will send to the AI model.
    # We’re telling it:
    # - What the stock symbol is
    # - What it needs to do: decide if the stock is doing well (bullish), badly (bearish), or neutral
    # - That it should explain its reasoning like a human advisor would
    prompt = f"""
You are a professional financial analyst.

You will receive recent news headlines about a stock, in this case: {symbol}.

Your task is to:
1. Determine the **overall sentiment** (Bullish, Bearish, or Neutral)
2. Provide a **detailed explanation** for the sentiment using specific headlines
3. Analyze the **short-term and long-term impact** of the news on the stock price
4. Format your answer clearly and explain it in simple terms for beginner investors
M
ake sure your response is fully complete. Do not end mid-sentence.

Here are the headlines:
{chr(10).join(['- ' + h for h in headlines])}

Respond with clear bullet points and plain language.
"""

    # Send this prompt to the Cohere AI model and ask it to generate a response
    response = co.generate(
        model="command-r-plus",     # The specific AI model from Cohere we're using (good at reasoning and analysis)
        prompt=prompt,              # The instruction and data we’re sending to the AI
        max_tokens=800,             # Limit how long the AI’s answer can be (about 300-400 words)
        temperature=0.4             # Controls how creative the AI is (0.4 = more focused, less random)
    )

    # Get the text that the AI generated, remove any extra spaces, and return it
    return response.generations[0].text.strip()
