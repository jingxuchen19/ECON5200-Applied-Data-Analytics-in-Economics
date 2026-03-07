# Assignment 3: The Causal Architecture

## Course
ECON 5200 — Applied Data Analytics in Econ 

## Overview
This project tackles three real-world operational questions at a fictional logistics company, SwiftCart Logistics. Instead of relying on traditional parametric assumptions, we use bootstrapping, permutation testing, and propensity score matching to build empirical evidence and isolate true causal effects from spurious correlation. All bootstrap and permutation engines were written manually using `for` loops and native NumPy to demonstrate understanding of the underlying statistical machinery.

## Phases

### Phase 1: Bootstrapping Non-Parametric Uncertainty
**Problem:** A labor union is challenging SwiftCart's claim about median driver compensation. Tip data is zero-inflated and heavily right-skewed, making the Central Limit Theorem unreliable for small-sample inference.

**Approach:** Simulated 250 driver tips (100 zero-tips + 150 drawn from an Exponential distribution with scale=5.0). Built a manual bootstrap engine that resamples with replacement 10,000 times, computes the median for each resample, and extracts the 2.5th and 97.5th percentiles to form a 95% confidence interval. The resulting CI is asymmetric, reflecting the true skewed shape of the data — something a standard parametric interval would miss.

### Phase 2: Falsification in Logistics A/B Testing
**Problem:** The engineering team claims their new "Batch Routing" algorithm reduces delivery times, but the treatment group contains extreme outliers from software crash loops, violating the homoscedasticity assumption of a standard T-test.

**Approach:** Generated 500 Control deliveries (Normal, mean=35, sd=5) and 500 Treatment deliveries (Log-Normal, mean=3.4, sigma=0.4). Computed the observed difference in means, then ran a manual permutation test with 5,000 iterations — shuffling all 1,000 observations, splitting into two pseudo-groups, and recording the simulated difference each time. The empirical p-value measures what proportion of random permutations produced a difference as extreme as or more extreme than the observed one.

### Phase 3: Causal Control and Selection Bias Mitigation
**Problem:** The marketing team claims SwiftPass subscribers spend 300% more and wants to double the acquisition budget. However, this comparison suffers from severe selection bias — high-volume "power users" naturally self-select into the program to save on delivery fees.

**Approach:** Loaded the `swiftcart_loyalty.csv` dataset and first calculated the naive Simple Difference in Outcomes (SDO) between subscribers and non-subscribers. Then applied Propensity Score Matching (PSM): used Logistic Regression to estimate each user's probability of subscribing based on pre-treatment covariates (pre_spend, account_age, support_tickets), and used Nearest Neighbors to match each subscriber with the most similar non-subscriber. The resulting Average Treatment Effect on the Treated (ATT) is substantially smaller than the naive SDO, confirming that selection bias was inflating the apparent effect of SwiftPass.

### Phase 4: AI-Assisted Visualization
**Approach:** Generated a Love Plot (Standardized Mean Differences) to visually verify covariate balance before and after matching. The plot shows that all three covariates (pre_spend, account_age, support_tickets) moved significantly closer to zero after PSM, providing visual evidence that the matching procedure successfully reduced selection bias.

## Key Results
| Metric | Value |
|--------|-------|
| Bootstrap 95% CI for median tip | [0.26, 1.36] |
| Observed median tip | $0.76 |
| Permutation test p-value | 0.0004 |
| Observed difference (Control - Treatment) | 2.26 minutes |
| Naive SDO (SwiftPass) | $17.57 |
| ATT after PSM | $9.91 |
| Selection bias inflation | ~77% |

## Tools
Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn (LogisticRegression, NearestNeighbors)

## Environment
Google Colab
