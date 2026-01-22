import plotly.express as px

def rating_chart(df):
    c = df["rating"].value_counts().sort_index()
    return px.bar(x=c.index, y=c.values)