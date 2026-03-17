# AI Capex Diagnostic Modeling

## Objective
Diagnose structural failures in an OLS model predicting AI Software Revenue — specifically heteroscedasticity and multicollinearity — and apply HC3 Robust Standard Errors to strip away false statistical confidence and reveal the true significance of deployment metrics.

## The Data
2026 Nvidia AI Capital Expenditure and Deployment Data — A synthetic cross-sectional dataset of 250 observations containing `AI_Software_Revenue`, `Hardware_Capex`, `Data_Center_Power_MW`, and `Cloud_GPU_Deployments`, engineered to exhibit expanding residual variance at higher capital expenditure tiers.

## Tech Stack
Python, pandas, statsmodels, matplotlib, seaborn, Plotly

## Methodology
- **Naive Baseline OLS:** Constructed a multivariate regression predicting `AI_Software_Revenue` from `Hardware_Capex`, `Data_Center_Power_MW`, and `Cloud_GPU_Deployments`. The baseline model returned a deceptively high R² of 0.972 with extremely low p-values, projecting an illusion of model perfection.
- **Visual Residual Forensics:** Plotted residuals against fitted values and observed a clear expanding cone pattern — residual errors flare outward as predicted revenue increases, indicating severe heteroscedasticity. The algorithm's mistakes grow proportionally with the scale of the data.
- **White Test (Formal Diagnosis):** Executed the White Test to statistically confirm heteroscedasticity. The LM-Test p-value returned at effectively zero (4.46e-09), decisively rejecting the null hypothesis of constant variance and corroborating the visual diagnosis.
- **Variance Inflation Factor (VIF) Analysis:** Calculated VIF scores for each regressor to detect multicollinearity. Identified redundant covariance between predictors, informing the decision to drop `Data_Center_Power_MW` from the final specification.
- **HC3 Robust Standard Error Correction:** Re-fitted the model with heteroscedasticity-consistent (HC3) robust covariance estimation. This correction appropriately widened the standard errors to reflect the true uncertainty in the coefficients, producing conservative and reliable significance thresholds.
- **Interactive Diagnostic Dashboard (AI Expansion):** Built an interactive Plotly dashboard featuring residual scatter plots with outlier highlighting, a side-by-side coefficient comparison between Naive OLS and HC3 Robust models, and a VIF bar chart with a multicollinearity threshold indicator.

## Key Findings
- The naive OLS model exhibited severe heteroscedasticity, confirmed both visually (expanding cone of residual errors) and statistically (White Test p-value ≈ 0). This means the baseline model's tight confidence intervals and low p-values were mathematically inflated — a dangerous illusion of precision.
- `Data_Center_Power_MW` was statistically insignificant (p = 0.555) in the baseline model and was removed from the final robust specification to reduce multicollinearity.
- After applying HC3 correction, `Hardware_Capex` (+$1.74 per unit) and `Cloud_GPU_Deployments` (+$4.01 per unit) remained highly significant predictors of AI Software Revenue, with appropriately widened standard errors reflecting the true uncertainty structure of the data.
- The diagnostic workflow demonstrates that a high R² alone is insufficient — without residual forensics and robust covariance correction, algorithmic confidence can be a costly illusion in high-stakes capital allocation decisions.
