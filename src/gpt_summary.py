import os, openai, streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_data(ttl=86400)
def gpt_summary(df):
    text = "\n".join(df["content"].dropna().tolist())[:12000]
    res = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize product reviews."},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )
    return res.choices[0].message.content

def clear_gpt_cache():
    st.cache_data.clear()