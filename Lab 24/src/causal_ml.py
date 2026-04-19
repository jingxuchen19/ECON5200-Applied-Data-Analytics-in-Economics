"""Causal ML utilities for Lab 24."""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold


def manual_dml(Y, D, X, random_state=42):
    """
    Manual 2-fold cross-fitting DML.

    Parameters
    ----------
    Y : array, outcome
    D : array, treatment
    X : array, covariates
    random_state : int

    Returns
    -------
    float : estimated ATE
    """
    n = len(Y)
    kf = KFold(n_splits=2, shuffle=True, random_state=random_state)

    Y_tilde = np.zeros(n)
    V_tilde = np.zeros(n)

    for train_idx, test_idx in kf.split(X):
        # outcome model
        ml_l = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42)
        ml_l.fit(X[train_idx], Y[train_idx])
        Y_hat = ml_l.predict(X[test_idx])
        Y_tilde[test_idx] = Y[test_idx] - Y_hat

        # treatment model
        ml_m = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42)
        ml_m.fit(X[train_idx], D[train_idx])
        D_hat = ml_m.predict(X[test_idx])
        V_tilde[test_idx] = D[test_idx] - D_hat

    theta = np.sum(V_tilde * Y_tilde) / np.sum(V_tilde * D)
    return theta


def cate_by_subgroup(data, cate_predictions, group_col, q=4):
    """
    Compute mean CATE by subgroup quartile.

    Parameters
    ----------
    data : DataFrame
    cate_predictions : array of individual CATEs
    group_col : str, column to group by
    q : int, number of quartiles

    Returns
    -------
    DataFrame with mean, std, count per group
    """
    import pandas as pd

    data = data.copy()
    data['cate'] = cate_predictions
    data['group'] = pd.qcut(data[group_col], q=q, labels=[f'Q{i+1}' for i in range(q)])
    stats = data.groupby('group')['cate'].agg(['mean', 'std', 'count'])
    return stats
