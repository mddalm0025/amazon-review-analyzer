def analyze_reviews(df):
    return {
        "count": len(df),
        "avg_rating": round(df["rating"].mean(), 2)
    }