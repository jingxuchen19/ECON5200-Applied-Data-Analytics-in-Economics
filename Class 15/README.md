# Forecasting Architecture and the Bias-Variance Tradeoff

## Objective

Diagnosed the structural failure modes of polynomial regression models applied to hyper-volatile NVIDIA quarterly revenue data (FY2025–FY2026), quantifying the catastrophic out-of-sample risk of algorithmic overfitting and deploying K-Fold Cross-Validation and Ridge Regularization as corrective mechanisms to restore predictive stability.

## Methodology

- Ingested eight quarters of NVIDIA total corporate revenue data spanning the 2024–2026 AI infrastructure capital expenditure boom, and performed visual exploratory data analysis to identify the non-linear, exponential curvature of revenue growth.
- Established a baseline linear regression model to observe systematic underfitting (high bias), where a rigid straight line failed to capture the accelerating revenue trajectory (Training MSE: 7.91).
- Expanded the feature space to a 7th-degree polynomial using `PolynomialFeatures`, producing a model that achieved near-zero training error (MSE ≈ 0.00) by contorting to memorize every historical data point — a textbook demonstration of overfitting (high variance).
- Forced the overfit model to extrapolate one quarter beyond observed data (Q1 FY27), triggering a hallucinated prediction of −$84.00 billion in revenue — exposing the epistemological collapse of unconstrained polynomial extrapolation.
- Deployed 4-Fold Cross-Validation via `cross_val_score` to rigorously evaluate true out-of-sample performance, revealing a massive cross-validated MSE of 8,641.58 against the artificially perfect training MSE of 0.00.
- Applied Ridge Regression (L2 Regularization) with automated hyperparameter tuning via `RidgeCV` to constrain coefficient variance, selecting an optimal penalty parameter (α = 17.07) through 4-Fold Cross-Validation.

## Key Findings

- The 7th-degree polynomial OLS model achieved perfect training fit (MSE = 0.00) but exhibited catastrophic generalization failure, with a cross-validated MSE of 8,641.58 — a variance gap exceeding 8,600 units, confirming severe overfitting to stochastic noise rather than learning the underlying economic signal.
- Extrapolation to the next unseen quarter produced a physically impossible negative revenue forecast (−$84B), demonstrating that memorizing historical volatility provides zero predictive capability beyond the training window.
- Ridge Regularization dramatically compressed the polynomial coefficient magnitudes (e.g., the x¹ coefficient shrank from −256.43 under OLS to 0.04 under Ridge), yielding a stable, smooth revenue curve while reducing the cross-validated MSE to 4,897.44 — an approximate 43% reduction in true operational error.
- The bias-variance tradeoff was observed empirically: Ridge accepted a marginal increase in training error (0.26 vs 0.00) in exchange for substantially improved out-of-sample stability, confirming that algorithmic regularization is essential when modeling volatile financial time series with limited observations.

## Tech Stack

Python · pandas · NumPy · scikit-learn (`PolynomialFeatures`, `LinearRegression`, `RidgeCV`, `cross_val_score`) · matplotlib
