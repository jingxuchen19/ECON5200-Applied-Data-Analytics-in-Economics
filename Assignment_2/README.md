# Audit 02: Deconstructing Statistical Lies

## Overview

This project conducts a multi-phase statistical audit to uncover how data can mislead when distribution shape, base rates, or selection bias are ignored.

Through simulations and probability modeling, this analysis examines three common statistical traps:

- **Latency Skew** (Outlier Distortion)  
- **False Positive Paradox** (Base Rate Neglect)  
- **Survivorship Bias** (Selective Visibility)  

Each phase demonstrates how seemingly valid metrics can collapse under deeper statistical scrutiny.

---

## Phase 1: The Latency Trap  
### Robustness Audit — SD vs. MAD

A simulated traffic dataset was constructed with:

- 980 normal observations  
- 20 extreme outliers  

The objective was to compare:

- Standard Deviation (SD)  
- Median Absolute Deviation (MAD)  

### Key Finding

Standard Deviation increased dramatically due to extreme outliers, while MAD remained stable.

This demonstrates:

> SD is highly sensitive to extreme values.  
> MAD is robust under skewed distributions.

In heavy-tailed environments (e.g., latency systems or financial returns), relying solely on SD can distort risk assessment.

---

## Phase 2: The False Positive Paradox  
### Bayesian Audit — Posterior Probability

A plagiarism detection model claims:

- Sensitivity = 98%  
- Specificity = 98%  

However, in an Honors Seminar:

- Base rate of cheating = 0.1%  

We compute the posterior probability:

P(Cheater | Flagged)

### Results

| Scenario | Base Rate | Posterior Probability |
|----------|-----------|----------------------|
| Bootcamp | 50%       | 0.98                 |
| Econ Class | 5%      | ~0.72                |
| Honors Seminar | 0.1% | ~0.047              |

### Key Finding

Even a 98% accurate model produces mostly false positives when the base rate is extremely low.

This illustrates the **Base Rate Fallacy**:

> Accuracy metrics without prevalence context are statistically misleading.

---

## Phase 3: Detecting Sample Ratio Mismatch (SRM)

An A/B test claims a 50/50 allocation:

- Observed: 50,250 Control  
- Observed: 49,750 Treatment  

A manual Chi-Square Goodness-of-Fit test was performed using:

Chi-Square = sum((Observed - Expected)^2 / Expected)

### Result

- Chi-Square Statistic = 2.5  
- Critical Value (df = 1, alpha = 0.05) = 3.84  

Conclusion:

> No statistically significant SRM detected.

Even small allocation differences must be formally tested before trusting experimental results.

---

## Phase 4: The MemeCoin Graveyard  
### Survivorship Bias Simulation

10,000 token launches were simulated using a Pareto (Power Law) distribution:

- 99% near zero  
- 1% extreme winners  

Two datasets were created:

- `df_all` → Entire population  
- `df_survivors` → Top 1% only  

### Mean Comparison

- Mean (All Tokens): Low  
- Mean (Top 1% Only): Artificially inflated  

### Key Finding

Filtering out failures dramatically inflates average performance.

This demonstrates **Survivorship Bias**:

> Analyzing only winners creates a statistical illusion.

---

## Tools & Methods

- Python (NumPy, Pandas, Matplotlib)  
- Manual statistical implementations:
  - Median & MAD (no SciPy)  
  - Bayes’ Theorem  
  - Chi-Square Test  
- Pareto distribution simulation  

---

## Final Reflection

Statistical models fail not because the math is wrong —  
but because assumptions go unquestioned.

This audit highlights:

- How skew distorts volatility metrics  
- How base rates redefine model accuracy  
- How selection bias fabricates performance  

Robust statistical thinking is foundational to ethical data science.
