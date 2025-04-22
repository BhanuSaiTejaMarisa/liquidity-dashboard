import yfinance as yf
import pandas as pd

# Download historical Nifty 50 data for the past 3 years
nifty = yf.download("^NSEI", period="3y", interval="1d")

# Save to CSV
nifty.to_csv("data/nifty50.csv")
print("Nifty 50 data saved to data/nifty50.csv")
