# Lab 20: Time Series Diagnostics & Advanced Decomposition

## Objective

Diagnose and fix common time series decomposition pitfalls, then extend the analysis with MSTL, block bootstrap, and structural break detection on FRED economic data.

## Methodology

- Diagnosed broken STL decomposition on multiplicative retail sales data and fixed it with log-transform
- Corrected a misspecified ADF test (regression='n' → 'ct') and applied the ADF/KPSS 2x2 decision table
- Applied MSTL to simulated hourly electricity demand with daily (24h) and weekly (168h) seasonal cycles
- Implemented moving block bootstrap to quantify GDP trend uncertainty with 90% confidence bands
- Detected structural breaks in GDP growth using PELT and ran per-regime stationarity tests
- Built a reusable decompose.py module with run_stl(), test_stationarity(), detect_breaks(), run_mstl(), and block_bootstrap_trend()
- Created an interactive Streamlit app for FRED time series analysis

## Key Findings

- Retail sales require log-transform before STL because seasonality is multiplicative
- Real GDP is I(1) non-stationary: ADF p=0.96 with regression='ct', KPSS p=0.01
- MSTL cleanly separates daily and weekly cycles with residual std close to true noise level
- Bootstrap CI is wider during recessions (2008, 2020) due to larger residuals
- GDP growth is stationary within regimes identified by PELT

## How to Reproduce

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Open `notebooks/lab_20_time_series.ipynb` and run all cells
4. For the Streamlit app: `streamlit run src/app.py`
