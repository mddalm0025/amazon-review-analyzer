import os, time, requests, streamlit as st

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
HOST = "real-time-amazon-data.p.rapidapi.com"

@st.cache_data(ttl=86400)
def fetch_reviews(asin, country, pages, refresh=False):
    if refresh:
        st.cache_data.clear()
    reviews = []
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": HOST
    }
    for page in range(1, pages + 1):
        url = f"https://{HOST}/product-reviews"
        params = {"asin": asin, "country": country, "page": page}
        r = requests.get(url, headers=headers, params=params)
        if r.status_code != 200:
            break
        data = r.json().get("data", {}).get("reviews", [])
        if not data:
            break
        for rv in data:
            try:
                reviews.append({
                    "content": rv.get("review_text", ""),
                    "rating": float(rv.get("review_rating", "0").split()[0])
                })
            except:
                pass
        time.sleep(1.2)
    return reviews

def clear_review_cache():
    st.cache_data.clear()