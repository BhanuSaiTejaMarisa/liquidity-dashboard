import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
df = pd.read_csv("data/nifty50.csv", parse_dates=["Date"])

st.title("📈 Nifty 50 Historical Dashboard")

# Line chart of closing price
st.subheader("Nifty 50 - Closing Price")
fig = px.line(df, x="Date", y="Close", title="Nifty 50 Closing Price")
st.plotly_chart(fig)

# Optional: Volume chart
with st.expander("Show Volume Traded"):
    fig_vol = px.bar(df, x="Date", y="Volume", title="Volume Traded")
    st.plotly_chart(fig_vol)



# -- Load FII/DII data --
fii_dii_df = pd.read_csv("data/fii_dii.csv")

# Rename columns for clarity (if not already done)
fii_dii_df.columns = ["Date", "FII_Buy", "FII_Sell", "FII_Net", "DII_Buy", "DII_Sell", "DII_Net"]

# Parse Date
fii_dii_df["Date"] = pd.to_datetime(fii_dii_df["Date"], format="%B %Y")

# Optional: Sort by date if needed
fii_dii_df = fii_dii_df.sort_values("Date")

# -- Plot FII Net Flow --
st.subheader("📊 FII Net Purchases Over Time")
fig_fii = px.line(fii_dii_df, x="Date", y="FII_Net", title="FII Net Flow")
st.plotly_chart(fig_fii)

# -- Plot DII Net Flow --
st.subheader("📊 DII Net Purchases Over Time")
fig_dii = px.line(fii_dii_df, x="Date", y="DII_Net", title="DII Net Flow")
st.plotly_chart(fig_dii)
