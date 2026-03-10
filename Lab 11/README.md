# Data Wrangling & Engineering Pipeline

## Objective
Engineer structural features and systematically impute missing values to transform a chaotic enterprise HR dataset into a clean, model-ready matrix suitable for econometric estimation.

## The Data
`messy_hr_economics.csv` — A synthetic corporate HR dataset containing 3,200 employee records across 13 variables, including salary information, department classifications, regional economic indicators, and performance metrics. The dataset is intentionally engineered with non-random missingness patterns and high-cardinality categorical variables.

## Tech Stack
Python, pandas, NumPy, statsmodels, missingno, category_encoders

## Methodology
- **Visual Forensics:** Plotted a missingness matrix using `missingno` to expose structural patterns in null values. Identified that `bonus_pay` and `performance_rating` share perfectly aligned missing rows, diagnosing the mechanism as MAR (Missing at Random) rather than random noise.
- **Conditional Imputation:** Imputed missing `base_salary` values using department-level medians via `groupby().transform()`, preserving within-group variance rather than distorting the distribution with a naive global fill.
- **Dummy Variable Trap (Intentional Failure):** Created one-hot encoded department dummies without dropping a reference category, then added a constant intercept — triggering perfect multicollinearity and demonstrating why OLS fails when the design matrix is singular.
- **k-1 Dummy Encoding:** Resolved the trap by applying `drop_first=True`, establishing Engineering as the reference category and successfully running the OLS regression (R² = 0.744).
- **Target Encoding:** Compressed 874 unique ZIP codes into a single continuous feature using `category_encoders.TargetEncoder`, capturing regional salary variation without generating hundreds of sparse dummy columns.

## Key Findings
- Missingness in `bonus_pay` and `performance_rating` is structurally linked (MAR), suggesting a shared underlying HR process drives both gaps simultaneously.
- Conditional median imputation by department preserved the salary distribution across Engineering ($108,667), Marketing ($83,365), and Sales ($80,097).
- The safe OLS model reveals that each additional year of tenure is associated with approximately $3,334 in additional base salary, while Marketing and Sales employees earn roughly $26,200 and $29,000 less than Engineering employees, respectively.
- Target encoding effectively reduced ZIP code dimensionality from 874 columns to 1, making regional economic effects tractable for regression without sacrificing geographic signal.
