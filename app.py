import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.title("📊 Liquidity Dashboard - Nifty50 + FII/DII Flows")

# ------------------ NIFTY50 -------------------
df = pd.read_csv("data/nifty50.csv",skiprows=3,names=["Date", "Close", "High", "Low", "Open", "Volume"], parse_dates=["Date"])
df = df.sort_values("Date")

# Sidebar - Nifty filters
st.sidebar.header("Nifty50 Filters")
nifty_start, nifty_end = st.sidebar.date_input(
    "Select date range for Nifty50", [df["Date"].min(), df["Date"].max()]
)

nifty_metric = st.sidebar.selectbox("Select Nifty metric to view", df.columns.drop("Date"))

# Filtered Nifty data
filtered_df = df[(df["Date"] >= pd.to_datetime(nifty_start)) & (df["Date"] <= pd.to_datetime(nifty_end))]

st.subheader(f"Nifty50 - {nifty_metric}")
fig = px.line(filtered_df, x="Date", y=nifty_metric, title=f"Nifty 50 {nifty_metric} Over Time")
st.plotly_chart(fig, use_container_width=True)

# ------------------ VOLUME -------------------
with st.expander("📦 Show Volume Traded"):
    fig_vol = px.bar(filtered_df, x="Date", y="Volume", title="Volume Traded")
    st.plotly_chart(fig_vol, use_container_width=True)

# ------------------ FII/DII -------------------
fii_dii_df = pd.read_csv("data/fii_dii.csv")
fii_dii_df.columns = ["Date", "FII_Buy", "FII_Sell", "FII_Net", "DII_Buy", "DII_Sell", "DII_Net"]
fii_dii_df["Date"] = pd.to_datetime(fii_dii_df["Date"], format="%B %Y")
fii_dii_df = fii_dii_df.sort_values("Date")

# Sidebar - FII/DII filters
st.sidebar.header("FII/DII Filters")
fii_start, fii_end = st.sidebar.date_input(
    "Select date range for FII/DII", [fii_dii_df["Date"].min(), fii_dii_df["Date"].max()]
)
fii_dii_df = fii_dii_df[(fii_dii_df["Date"] >= pd.to_datetime(fii_start)) & (fii_dii_df["Date"] <= pd.to_datetime(fii_end))]

show_fii = st.sidebar.checkbox("Show FII Net Flow", value=True)
show_dii = st.sidebar.checkbox("Show DII Net Flow", value=True)

if show_fii:
    st.subheader("FII Net Flow")
    fig_fii = px.line(fii_dii_df, x="Date", y="FII_Net", title="FII Net Purchases")
    st.plotly_chart(fig_fii, use_container_width=True)

if show_dii:
    st.subheader("DII Net Flow")
    fig_dii = px.line(fii_dii_df, x="Date", y="DII_Net", title="DII Net Purchases")
    st.plotly_chart(fig_dii, use_container_width=True)


