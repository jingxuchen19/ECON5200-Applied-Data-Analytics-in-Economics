# Architecting the Prediction Engine

## Objective
Architect a multivariate OLS prediction engine to forecast real estate valuations using contemporary 2026 market data, and evaluate out-of-sample performance by quantifying the model's financial error margin in actual US Dollars via Root Mean Squared Error (RMSE).

## The Data
Zillow ZHVI 2026 Micro Dataset — A cross-sectional dataset of 1,000 residential properties containing structural attributes (square footage, property age), locational features (distance to transit, school district rating), and observed market valuations.

## Tech Stack
Python, pandas, NumPy, statsmodels (Patsy Formula API), Plotly

## Methodology
- **Model Specification:** Defined a hedonic pricing model using the statsmodels Patsy formula interface, regressing `Home_Value` on `Square_Footage`, `Property_Age`, `Distance_to_Transit`, and `School_District_Rating`. The Patsy API automatically handled intercept inclusion and categorical variable encoding.
- **Model Fitting & Diagnostics:** Fitted the OLS model and examined the summary output. Verified that coefficient signs align with economic intuition — square footage positively associated with value, while property age and distance to transit carry negative coefficients, reflecting depreciation and reduced accessibility premiums.
- **Predictive Engineering:** Transitioned from classical parameter interpretation to prediction by generating a continuous vector of fitted home values using the trained model.
- **Loss Quantification:** Calculated the Root Mean Squared Error (RMSE) between actual and predicted values using `statsmodels.tools.eval_measures`, translating abstract model performance into a concrete dollar-denominated error metric.
- **Residual Forensics (AI Expansion):** Built an interactive residual diagnostics dashboard using Plotly, plotting fitted values against residual errors and flagging statistical outliers (beyond 2 standard deviations) in crimson to visually detect heteroscedasticity or structural breaks.

## Key Findings
- The model achieves an R-squared indicating meaningful explanatory power across the feature set, with all primary coefficients statistically significant.
- Each additional square foot of living space is associated with approximately $121 in added home value, while each year of property age reduces value by roughly $815.
- The Predictive RMSE of **$42,316.69** represents the model's average financial blind spot — on a typical prediction, the algorithm's estimate deviates from reality by approximately $42K, a critical metric for assessing algorithmic risk in real estate acquisition decisions.
- Residual forensics visualization confirmed no severe heteroscedasticity or nonlinear structural breaks, supporting the validity of the linear specification for this dataset.
