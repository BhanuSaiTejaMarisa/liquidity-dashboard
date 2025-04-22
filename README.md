# Liquidity Dashboard & Cash Allocation Tool for Indian Equities

## 👋 Overview

This is a prototype tool built to visualize and monitor market liquidity trends in the Indian equity market. The dashboard is implemented using **Streamlit**, with backend logic in **Python**, and focuses on displaying relevant financial data through interactive charts and filters.

As a frontend-focused developer with limited exposure to finance or backend-heavy stacks, I implemented the essential parts (Step 1 & 2) of the assignment while learning about the domain in parallel.

---

## ✅ Implemented Features

### 1. 📊 Data Collection & Visualization
- Collected historical data from **NSE India** and **FII/DII flows** using public data CSVs.
- Plotted 2 key time-series charts:
  - Nifty 50 Index Trend
  - FII/DII Net Flow over time
- Stored data in structured CSV format
- Implemented basic data validation and fallbacks

### 2. 💻 Hosted Interactive Dashboard
- Built using [Streamlit](https://streamlit.io)
- Hosted on [Streamlit Cloud](https://liquidity-dashboard-ckkcfj6vrimspbovxw82yd.streamlit.app/)
- Features:
  - Interactive line charts for key metrics
  - Date filtering capability (basic)
  - Visual exploration of liquidity trends

---

## ❌ Step 3 (Not Implemented)

**Cash Allocation Modeling and Feature Engineering**
- Due to time constraints and unfamiliarity with financial modeling, this section was skipped.
- Suggestions like calculating 30-day volatility, market breadth, or risk tolerance toggles were noted but not implemented.

---

## ⚙️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/BhanuSaiTejaMarisa/liquidity-dashboard.git
   cd liquidity-dashboard

2. Install dependencies:
   ```bash
   pip install -r requirements.txt     

3. Start the app:
   ```bash
   streamlit run app.py

## 📎 Resources Used
- NSE India (https://www.nseindia.com/)
- Public CSVs for FII/DII flows
- ChatGPT for technical guidance and explanations

