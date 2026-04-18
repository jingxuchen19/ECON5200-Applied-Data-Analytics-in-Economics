# Time Series Forecasting — ARIMA, GARCH & Bootstrap

## Objective

Diagnosed and corrected a broken ARIMA pipeline for CPI forecasting, modeled S&P 500 volatility with GARCH(1,1), and built reusable forecast evaluation tools.

## Methodology

- Identified three errors in a flawed ARIMA pipeline: missing differencing (d=0 on non-stationary CPI), no seasonal component, and skipped Ljung-Box residual diagnostics
- Rebuilt the pipeline as a SARIMA model with proper differencing (d=1, D=1) and seasonal terms (m=12), then verified residuals with the Ljung-Box test
- Fit a GARCH(1,1) model to S&P 500 daily log returns to capture volatility clustering
- Created a reusable forecast_evaluation.py module with compute_mase() for scaled error measurement and backtest_expanding_window() for walk-forward validation
- Implemented block bootstrap forecast intervals as a distribution-free alternative to standard ARIMA confidence bands

## Key Findings

- Raw CPI is non-stationary (ADF p >> 0.05). First + seasonal differencing produces a stationary series (ADF p = 0.0005).
- SARIMA captures seasonal CPI patterns that plain ARIMA misses entirely.
- S&P 500 GARCH(1,1) estimates: alpha = 0.1197, beta = 0.8629, giving alpha + beta = 0.9826 (< 1, variance stationary). Volatility shocks have a half-life of about 39.5 days.
- Block bootstrap intervals are wider than standard parametric CIs, reflecting the real uncertainty that normal-distribution assumptions tend to understate.
