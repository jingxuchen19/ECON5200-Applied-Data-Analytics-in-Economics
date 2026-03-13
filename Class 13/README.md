# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Execute a multivariate hedonic pricing model on contemporary California real estate data and manually prove the Frisch-Waugh-Lovell (FWL) theorem to demonstrate how OLS algorithms achieve ceteris paribus by computationally isolating the pure marginal effect of individual regressors.

## The Data
Zillow California 2026 Hedonic Dataset — A synthetic cross-sectional dataset of 1,000 residential properties containing `Sale_Price`, `Property_Age`, and `Distance_to_Tech_Hub`, engineered to exhibit negative correlation between age and distance (older homes cluster near coastal tech hubs while newer developments expand inland).

## Tech Stack
Python 3.10+, pandas, statsmodels (Patsy Formula API), matplotlib, Plotly

## Methodology
- **Naive Bivariate Regression:** Regressed `Sale_Price` strictly on `Property_Age` to establish a baseline estimate. The naive model returned a positive coefficient (+$5,574 per year of age), incorrectly implying that older homes command higher prices — a direct consequence of omitting the location confounder.
- **Multivariate Expansion:** Incorporated `Distance_to_Tech_Hub` as a control variable. The Property_Age coefficient flipped to -$2,063, revealing that once proximity to tech employment centers is absorbed into the hyperplane, older homes depreciate as economic intuition predicts.
- **FWL Theorem — Manual Three-Step Proof:**
  - **Step 3a:** Regressed `Sale_Price` on `Distance_to_Tech_Hub` and extracted residuals, isolating the component of price variation unexplained by location.
  - **Step 3b:** Regressed `Property_Age` on `Distance_to_Tech_Hub` and extracted residuals, isolating the component of age variation uncorrelated with location.
  - **Step 3c:** Regressed the price residuals on the age residuals (suppressing the intercept with `-1`), recovering the pure partial effect of age on price with all shared covariance stripped away.
- **3D Hyperplane Visualization (AI Expansion):** Built an interactive Plotly 3D scatter plot overlaying the actual data points with the fitted OLS regression surface, visually demonstrating how the hyperplane simultaneously controls for both dimensions.

## Key Findings
- **Omitted Variable Bias (OVB) Detected:** The naive bivariate model exhibited severe OVB, falsely attributing a +$5,574/year premium to property age. In reality, the model was stealing mathematical credit from the omitted location variable — older homes are physically closer to high-value coastal tech hubs, and without controlling for distance, the algorithm cannot distinguish between the two signals.
- **Multivariate Correction:** Adding `Distance_to_Tech_Hub` corrected the bias, flipping the age coefficient to -$2,063/year (R² improved from 0.757 to 0.954), confirming that aging homes depreciate once location is held constant.
- **FWL Proof Achieved:** The coefficient extracted via the manual residual-on-residual regression matched the multivariate Property_Age coefficient to multiple decimal places (-2063.13), providing direct algebraic proof that OLS achieves ceteris paribus through systematic partial regression — not assumption, but computation.
