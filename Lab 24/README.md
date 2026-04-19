# Lab 24: Causal ML — DML and Causal Forests for Policy Evaluation

## Objective

Diagnose and fix a broken Double Machine Learning pipeline, then extend to individual-level treatment effect estimation using Causal Forests on 401(k) pension data.

## Methodology

- Identified and fixed three bugs in a manual 2-fold cross-fitting DML implementation: in-sample prediction (data leakage), missing treatment residualization, and wrong theta formula (np.mean vs IV-style ratio)
- Verified the corrected pipeline recovers the true ATE (≈5.0) on a simulated DGP with 5,000 observations and 100 covariates
- Estimated the ATE of 401(k) eligibility on net financial assets using the DoubleML package with Random Forest nuisance learners and 5-fold cross-fitting
- Ran sensitivity analysis (cf_y=0.03, cf_d=0.03) to assess robustness to unmeasured confounders
- Fit a CausalForestDML (EconML) with 500 causal trees to estimate individual-level CATEs across 9,915 observations
- Profiled high-response subgroup (top 25% CATE) against the rest of the sample
- Compared quartile-level subgroup DML to Causal Forest heterogeneity detection

## Key Findings

- Fixed DML recovered ATE = 5.17 on simulated data (true = 5.0, bias = +0.17)
- 401(k) ATE = -$1,000 (p = 0.038), with robustness value RV = 1.68%
- Causal Forest mean CATE ≈ -$31 with large individual variation (std = $4,057)
- Within-quartile std ($3,699) was 19x the between-quartile std ($192), showing that income-quartile DML misses substantial heterogeneity that Causal Forests capture at the individual level

## Tools

Python, scikit-learn, DoubleML, EconML (CausalForestDML), pandas, matplotlib
