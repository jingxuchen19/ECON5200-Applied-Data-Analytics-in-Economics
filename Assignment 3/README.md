# Assignment 3: The Causal Architecture

## Course
ECON 5200 — Statistical & Machine Learning for Economics (Spring 2026)

## Overview
This project explores bootstrapping, permutation testing, and causal inference techniques applied to operational problems at a fictional logistics company, SwiftCart Logistics. The goal is to move beyond simple correlation and isolate true causal effects using non-parametric and matching-based methods.

## Phases

### Phase 1: Bootstrapping Non-Parametric Uncertainty
Simulated a zero-inflated tip distribution (100 zero-tips + 150 exponential tips) to represent real-world gig economy data. Built a manual bootstrap engine with 10,000 iterations to estimate the 95% confidence interval for the median tip, avoiding reliance on the Central Limit Theorem.

### Phase 2: Falsification in Logistics A/B Testing
Generated synthetic A/B test data comparing a legacy routing system (Normal distribution) against a new batch-routing algorithm (Log-Normal distribution with crash-induced outliers). Conducted a manual permutation test with 5,000 iterations to calculate an empirical p-value, bypassing the homoscedasticity assumption required by traditional T-tests.

### Phase 3: Causal Control and Selection Bias Mitigation
Loaded observational data on SwiftCart's "SwiftPass" loyalty program. Calculated the naive Simple Difference in Outcomes (SDO) and identified severe selection bias. Applied Propensity Score Matching (PSM) using Logistic Regression and Nearest Neighbors to isolate the Average Treatment Effect on the Treated (ATT), revealing that the true causal effect of SwiftPass is substantially smaller than the naive estimate.

### Phase 4: AI-Assisted Visualization
Generated a Love Plot to visually confirm covariate balance before and after propensity score matching, demonstrating that selection bias was successfully mitigated across all pre-treatment covariates.

## Key Results
- **Bootstrap 95% CI for median tip:** [0.26, 1.36]
- **Permutation test p-value:** 0.0004 (statistically significant difference between routing algorithms)
- **Naive SDO (SwiftPass):** $17.57
- **ATT after PSM:** $9.91 (selection bias inflated the naive estimate by ~77%)

## Tools
Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

## Environment
Google Colab
