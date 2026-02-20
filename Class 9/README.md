# Recovering Experimental Truths via Propensity Score Matching

## Objective

This project examines how observational data can distort causal inference when treatment assignment is non-random. Using the Lalonde dataset, I demonstrate how naive estimation can produce misleading conclusions, and how Propensity Score Matching (PSM) can restore credible causal interpretation.

Rather than stopping at mean comparisons, this lab focuses on correcting selection bias and reconstructing experimental balance.

---

## Methodology

- Estimated treatment assignment using logistic regression to compute individual propensity scores.
- Diagnosed structural selection bias in the observational subsample.
- Applied Nearest Neighbor Matching on propensity scores to construct a counterfactual control group.
- Re-estimated the Average Treatment Effect (ATE) using matched samples.
- Compared naive difference-in-means estimates against bias-adjusted causal estimates.

This workflow explicitly models the assignment mechanism before estimating causal effects.

---

## Key Findings

**Naive Observational Estimate**

- Earnings Difference: -$635  
- P-value: 0.334  

The raw comparison suggests a negative and statistically insignificant effect, reflecting selection bias rather than true program impact.

**Matched Causal Estimate (After PSM)**

- Earnings Difference: +$1,850  
- P-value: 0.011  

After matching, the treatment effect becomes positive and statistically significant, closely aligning with experimental benchmarks.

---

## Interpretation

Propensity Score Matching functions as a bias-correction architecture. In observational environments where randomized control trials are infeasible, modeling the treatment assignment process is essential to prevent spurious conclusions.

This lab reinforces a foundational principle of causal inference:

> When treatment is not randomly assigned, modeling why someone received treatment is as important as measuring what happened afterward.
