
# Lab 19: Tree-Based Models — Random Forests

## Objective
Compare tree-based models against linear regression on California Housing data, diagnose common evaluation and interpretation errors, and explain predictions using SHAP.

## Methodology
- Loaded California Housing dataset (20,640 observations, 8 features)
- Compared Decision Tree, Ridge Regression, Random Forest, and Gradient Boosting
- Diagnosed a train/test evaluation bug that inflated RF performance
- Critiqued a causal overclaim from MDI feature importance
- Tuned RF hyperparameters with GridSearchCV (n_estimators, max_depth, max_features)
- Generated SHAP waterfall and beeswarm plots for model interpretability
- Built a reusable shap_utils.py module and interactive Streamlit dashboard

## Key Findings
- Random Forest Test R² = 0.8051, Gradient Boosting R² = 0.8288, Ridge R² = 0.5759
- GBR slightly outperforms tuned RF; both substantially beat Ridge
- MedInc is the top predictor in both MDI and SHAP rankings
- Feature importance captures predictive power, not causal effects

## How to Reproduce
```
pip install -r requirements.txt
jupyter notebook notebooks/lab_19_random_forests.ipynb
```

## Repository Structure
```
econ-lab-19-random-forests/
├── README.md
├── requirements.txt
├── notebooks/
│   └── lab_19_random_forests.ipynb
├── src/
│   └── shap_utils.py
├── figures/
│   ├── shap_waterfall.png
│   ├── shap_beeswarm.png
│   └── feature_importance.png
└── verification-log.md
```
