import pandas as pd
import plotly.express as px
import streamlit as st

# ✅ Fix: Skip 2 non-data rows and parse dates
df = pd.read_csv("data/nifty50.csv", skiprows=3, names=["Date", "Close", "High", "Low", "Open", "Volume"], parse_dates=["Date"])


# ✅ Convert Date to just date object (no time part)
df["Date"] = df["Date"].dt.date

st.title("📈 Nifty 50 Historical Dashboard")
st.sidebar.header("📅 Filter Options")

# Filter by date
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[df["Date"].min(), df["Date"].max()],
    min_value=df["Date"].min(),
    max_value=df["Date"].max()
)

# Metric selection
metric = st.sidebar.selectbox("Select Metric", ["Close", "Open", "High", "Low", "Volume"])

# Filter data
if len(date_range) == 2:
    start_date, end_date = date_range
    df_filtered = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
else:
    df_filtered = df

# Main chart
st.subheader(f"Nifty 50 - {metric} Over Time")
fig = px.line(df_filtered, x="Date", y=metric, title=f"{metric} Trend")
st.plotly_chart(fig)

# Optional: Volume
if metric != "Volume":
    with st.expander("Show Volume Traded"):
        fig_vol = px.bar(df_filtered, x="Date", y="Volume", title="Volume Traded")
        st.plotly_chart(fig_vol)
