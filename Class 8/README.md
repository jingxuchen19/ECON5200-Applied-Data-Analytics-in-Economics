# Hypothesis Testing & Causal Evidence Architecture

## Overview
This lab implements the logic of scientific falsification on the Lalonde (1986) job training dataset.  
Rather than treating statistics as a tool for producing estimates, the goal is to evaluate competing causal narratives and determine whether the observed treatment effect can survive adversarial scrutiny.

The project reframes hypothesis testing as an evidence architecture problem:  
we do not try to *prove* a model correct — we attempt to break it.  
Only results that survive multiple independent tests are considered credible.

---

## Objective — From Estimation to Falsification
Traditional data analysis focuses on estimating effects.  
However, estimation alone cannot distinguish signal from coincidence.

This lab pivots toward falsification:

> Instead of asking *"What is the effect size?"*  
> We ask *"Could randomness plausibly generate this result?"*

The objective is to operationalize the scientific method:
1. Formulate a null hypothesis (no treatment effect)
2. Attempt to invalidate it using independent statistical tests
3. Accept the result only if multiple methods reject randomness

---

## Technical Approach

### Parametric Evidence (Welch’s T-Test)
- Estimated Average Treatment Effect (ATE) using unequal-variance t-test
- Computed signal-to-noise ratio
- Controlled Type I error rate (α = 0.05)
- Interpreted p-value as probability of observing evidence under the null, not probability the null is true

### Non-Parametric Evidence (Permutation Test)
- 10,000 resamples of treatment labels
- No distributional assumptions (robust to heavy-tailed earnings)
- Constructed empirical null distribution
- Verified statistical significance independently of normality

### Validation Logic
A causal claim is accepted **only if both tests reject the null**.  
This prevents model-assumption dependence.

---

## Key Findings
The analysis detects a statistically significant increase in real earnings:

**Estimated treatment lift ≈ $1,795**

Both parametric and non-parametric tests reject the null hypothesis.  
The result therefore survives distributional stress testing and qualifies as robust evidence rather than model artifact.

---

## Business Insight — Hypothesis Testing as a Safety Valve
In modern data products, most false discoveries do not come from bad models — they come from selective interpretation.

Without rigorous testing:
- Random noise becomes KPI improvement
- A/B tests ship regressions
- Models learn spurious correlations
- Companies optimize dashboards instead of reality

Hypothesis testing acts as the **safety valve of the algorithmic economy**:
it prevents data grubbing and guards decision systems against accidental overfitting to history.

Robust experimentation frameworks do not accelerate decisions —  
they prevent confidently wrong decisions.

---

## Takeaway
Statistical significance is not proof of truth.  
It is evidence that randomness failed an adversarial trial.

Reliable analytics is therefore not estimation, but survival:
only effects that withstand multiple attempts at refutation should influence real-world action.
