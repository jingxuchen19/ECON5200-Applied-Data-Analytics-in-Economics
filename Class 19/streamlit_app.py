
"""
Streamlit Dashboard — Lab 19: Random Forest SHAP Explorer
ECON 5200
"""

import streamlit as st
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_squared_error

st.set_page_config(page_title="Lab 19: RF SHAP Explorer", layout="wide")
st.title("Lab 19: Random Forest SHAP Explorer")

# load data
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# sidebar sliders
st.sidebar.header("Hyperparameters")
n_estimators = st.sidebar.slider("n_estimators", 10, 500, 100, step=10)
max_features = st.sidebar.slider("max_features", 1, 8, 4)

# fit models
rf = RandomForestRegressor(n_estimators=n_estimators, max_features=max_features, random_state=42)
rf.fit(X_train, y_train)

ridge = Ridge(alpha=1.0).fit(X_train, y_train)
gbr = GradientBoostingRegressor(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42)
gbr.fit(X_train, y_train)

# model comparison
st.subheader("Model Comparison")
results = {}
for name, model in [("Ridge", ridge), ("Random Forest", rf), ("GBR", gbr)]:
    r2 = r2_score(y_test, model.predict(X_test))
    rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
    results[name] = {"R²": round(r2, 4), "RMSE": round(rmse, 4)}
st.dataframe(pd.DataFrame(results).T)

# SHAP analysis on small sample
st.subheader("SHAP Analysis")
X_sample = X_test.iloc[:50]
explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_sample)

# beeswarm
st.write("**Beeswarm Plot (Global Feature Importance)**")
fig_bee, ax_bee = plt.subplots()
shap.plots.beeswarm(shap.Explanation(
    values=shap_values, base_values=explainer.expected_value, data=X_sample
), show=False)
st.pyplot(fig_bee)

# waterfall for selected observation
obs_idx = st.slider("Select observation for waterfall plot", 0, 49, 0)
st.write(f"**Waterfall Plot — Observation {obs_idx}**")
fig_wf, ax_wf = plt.subplots()
shap.plots.waterfall(shap.Explanation(
    values=shap_values[obs_idx],
    base_values=explainer.expected_value,
    data=X_sample.iloc[obs_idx]
), show=False)
st.pyplot(fig_wf)

# importance ranking toggle
st.subheader("Feature Importance Ranking")
method = st.radio("Select method:", ["MDI", "SHAP"])
if method == "MDI":
    imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
else:
    imp = pd.Series(np.abs(shap_values).mean(axis=0), index=X.columns).sort_values(ascending=False)
st.bar_chart(imp)
