# High-Dimensional GDP Growth Forecasting with Regularized Regression

## Objective
Forecast 5-year average GDP per capita growth for 120+ countries using 50+ World Development Indicators, demonstrating how OLS overfits in high dimensions and how Ridge and Lasso regularization improve out-of-sample prediction.

## Methodology
- Downloaded 35+ WDI indicators (trade, macro, education, infrastructure, health, finance, natural resources, agriculture, governance) for 2013–2019 via the `wbgapi` Python API
- Averaged indicators across years to create a single cross-sectional observation per country, with median imputation for missing values
- Split data into 70/30 train/test sets and standardized all features using `StandardScaler`
- Fit an OLS baseline to demonstrate overfitting (high training R², negative test R²)
- Applied `RidgeCV` and `LassoCV` from scikit-learn with 5-fold cross-validation to select optimal regularization parameters
- Visualized the Lasso Path using `lasso_path()` to identify which predictors enter the model first as the penalty decreases
- Built an interactive Plotly dashboard with a lambda slider and grouped coefficient comparison chart

## Key Findings
- OLS severely overfitted: Training R² = 0.600, Test R² = -0.849. The model memorized noise rather than learning generalizable patterns.
- Ridge (λ* = 47.15) improved test performance to R² = -0.051 by shrinking all 28 coefficients toward zero while keeping every predictor in the model.
- Lasso (λ* = 0.066) selected 17 of 28 predictors, zeroing out the rest. The top predictors of GDP growth included inflation, population growth, and natural resource rents.
- Predictors zeroed out by Lasso are conditionally redundant given other correlated indicators — not necessarily economically irrelevant.
- Extension: Switching the outcome to infant mortality yielded much stronger results (Test R² ≈ 0.845), suggesting that health outcomes have a more stable cross-country relationship with development indicators than GDP growth does.

## Tech Stack
Python (pandas, numpy, scikit-learn, matplotlib, plotly, wbgapi)
