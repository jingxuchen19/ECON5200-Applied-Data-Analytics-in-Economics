"""
shap_utils.py — Reusable SHAP explanation functions for tree-based models.
ECON 5200 Lab 19
"""

import numpy as np
import pandas as pd
import shap
from sklearn.inspection import permutation_importance


def explain_prediction(model, X: pd.DataFrame, idx: int):
    """Generate a SHAP waterfall plot for a single observation.

    Args:
        model: A fitted tree-based model (e.g., RandomForestRegressor).
        X: Feature DataFrame.
        idx: Row index of the observation to explain.

    Returns:
        SHAP waterfall plot for the selected observation.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X.iloc[[idx]])
    shap.plots.waterfall(shap.Explanation(
        values=shap_values[0],
        base_values=explainer.expected_value,
        data=X.iloc[idx]
    ))


def global_importance(model, X: pd.DataFrame):
    """Generate a SHAP beeswarm plot showing global feature importance.

    Args:
        model: A fitted tree-based model.
        X: Feature DataFrame.

    Returns:
        SHAP beeswarm plot.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    shap.plots.beeswarm(shap.Explanation(
        values=shap_values,
        base_values=explainer.expected_value,
        data=X
    ))


def compare_importance(model, X: pd.DataFrame, y):
    """Compare MDI vs SHAP feature importance rankings side by side.

    Args:
        model: A fitted tree-based model.
        X: Feature DataFrame.
        y: Target values.

    Returns:
        DataFrame with MDI and SHAP rankings.
    """
    # MDI importance
    mdi = pd.Series(model.feature_importances_, index=X.columns)

    # SHAP importance
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    shap_imp = pd.Series(np.abs(shap_values).mean(axis=0), index=X.columns)

    comparison = pd.DataFrame({
        'MDI': mdi.round(4),
        'MDI_Rank': mdi.rank(ascending=False).astype(int),
        'SHAP': shap_imp.round(4),
        'SHAP_Rank': shap_imp.rank(ascending=False).astype(int)
    }).sort_values('SHAP_Rank')

    print(comparison)
    return comparison


if __name__ == "__main__":
    from sklearn.datasets import fetch_california_housing
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split

    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    print("=== Waterfall for observation 0 ===")
    explain_prediction(rf, X_test.iloc[:50], 0)

    print("=== Global importance ===")
    global_importance(rf, X_test.iloc[:50])

    print("=== MDI vs SHAP ===")
    compare_importance(rf, X_test.iloc[:50], y_test[:50])
