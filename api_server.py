from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from news_fetcher import get_news_headlines
from ai_analyzer import analyze_sentiment

# ✅ Define the app FIRST before using it
app = FastAPI()

# ✅ Allow frontend to connect to this backend (CORS policy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API route for analyzing a stock symbol
@app.get("/analyze")
def analyze(symbol: str):
    headlines = get_news_headlines(symbol)
    if not headlines:
        return {"success": False, "message": "No news found."}
    
    headline_texts = [h["headline"] for h in headlines]
    analysis = analyze_sentiment(headline_texts, symbol)

    return {
        "success": True,
        "symbol": symbol,
        "headlines": headlines,  # 🆗 send both headline + URL
        "analysis": analysis
    }
