import streamlit as st
import pandas as pd
from src.scraper import fetch_reviews, clear_review_cache
from src.analyzer import analyze_reviews
from src.gpt_summary import gpt_summary, clear_gpt_cache
from src.visuals import rating_chart

st.set_page_config("Amazon Review Analyzer", layout="wide")
st.title("Amazon Review Analyzer")

with st.sidebar:
    asin = st.text_input("ASIN", "B08N5WRWNW")
    country = st.selectbox("Country", ["US", "IN", "UK"])
    pages = st.slider("Pages", 1, 50, 10)
    refresh = st.checkbox("Force Refresh")
    run = st.button("Analyze")
    if st.button("Clear Cache"):
        clear_review_cache()
        clear_gpt_cache()
        st.success("Cache cleared")

if run:
    df = pd.DataFrame(fetch_reviews(asin, country, pages, refresh))
    if not df.empty:
        stats = analyze_reviews(df)
        st.metric("Average Rating", stats["avg_rating"])
        st.metric("Total Reviews", stats["count"])
        st.plotly_chart(rating_chart(df))
        if st.button("GPT Summary"):
            st.markdown(gpt_summary(df))