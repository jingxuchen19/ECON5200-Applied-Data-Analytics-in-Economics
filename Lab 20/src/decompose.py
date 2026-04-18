"""
decompose.py — Time Series Decomposition & Diagnostics Module
Extended version with MSTL and block bootstrap support.
Author: Jingxu Chen
Course: ECON 5200, Lab 20
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL, MSTL
from statsmodels.tsa.stattools import adfuller, kpss
import ruptures as rpt
from typing import Optional


def run_stl(
    series: pd.Series,
    period: int = 12,
    log_transform: bool = True,
    robust: bool = True
):
    """Apply STL decomposition with optional log-transform.

    Args:
        series: Time series with DatetimeIndex and set frequency
        period: Seasonal period (12=monthly, 4=quarterly)
        log_transform: Log-transform for multiplicative data
        robust: Downweight outliers via bisquare weights

    Returns:
        STL result object

    Raises:
        ValueError: if series contains non-positive values with log_transform=True
    """
    if log_transform:
        if (series <= 0).any():
            raise ValueError("Series has non-positive values, cannot log-transform.")
        series = np.log(series)
    result = STL(series, period=period, robust=robust).fit()
    return result


def test_stationarity(
    series: pd.Series,
    alpha: float = 0.05
) -> dict:
    """Run ADF + KPSS and return the 2x2 decision table verdict.

    Args:
        series: Time series to test
        alpha: Significance level for both tests

    Returns:
        dict with 'adf_stat', 'adf_p', 'kpss_stat', 'kpss_p', 'verdict'
    """
    adf_stat, adf_p, _, _, _, _ = adfuller(series, autolag='AIC', regression='ct')
    kpss_stat, kpss_p, _, _ = kpss(series, regression='ct', nlags='auto')

    adf_rej = adf_p < alpha
    kpss_rej = kpss_p < alpha

    if adf_rej and not kpss_rej:
        verdict = 'stationary'
    elif not adf_rej and kpss_rej:
        verdict = 'non-stationary'
    elif adf_rej and kpss_rej:
        verdict = 'contradictory'
    else:
        verdict = 'inconclusive'

    return {
        'adf_stat': adf_stat,
        'adf_p': adf_p,
        'kpss_stat': kpss_stat,
        'kpss_p': kpss_p,
        'verdict': verdict
    }


def detect_breaks(
    series: pd.Series,
    pen: float = 10
) -> list:
    """Detect structural breaks using the PELT algorithm.

    Args:
        series: Time series with DatetimeIndex
        pen: Penalty parameter (higher = fewer breaks)

    Returns:
        List of break dates as pd.Timestamp
    """
    signal = series.values
    algo = rpt.Pelt(model='rbf').fit(signal)
    breakpoints = algo.predict(pen=pen)

    dates = []
    for bp in breakpoints:
        if bp < len(series):
            dates.append(series.index[bp])
    return dates


def run_mstl(
    series: pd.Series,
    periods: list
):
    """Apply MSTL decomposition for multiple seasonal periods.

    MSTL iteratively removes seasonal components one at a time,
    starting from the shortest period.

    Args:
        series: Time series with DatetimeIndex and set frequency
        periods: List of seasonal periods (e.g. [24, 168])

    Returns:
        MSTL result object with .trend, .seasonal (DataFrame), .resid
    """
    mstl = MSTL(series, periods=periods)
    result = mstl.fit()
    return result


def block_bootstrap_trend(
    series: pd.Series,
    n_bootstrap: int = 200,
    block_size: int = 8,
    period: int = 4,
    log_transform: bool = True,
    robust: bool = True
) -> dict:
    """Compute bootstrap confidence bands for STL trend.

    Uses moving block bootstrap on residuals to preserve
    autocorrelation. i.i.d. bootstrap would destroy the
    time-dependence structure.

    Args:
        series: Time series with DatetimeIndex
        n_bootstrap: Number of bootstrap iterations
        block_size: Size of each block (in observations)
        period: Seasonal period for STL
        log_transform: Log-transform before STL
        robust: Use robust STL fitting

    Returns:
        dict with 'trend', 'lower', 'upper', 'ci_width'
    """
    np.random.seed(42)

    work = np.log(series) if log_transform else series.copy()
    stl = STL(work, period=period, robust=robust).fit()

    n = len(work)
    original_trend = stl.trend.values
    original_seasonal = stl.seasonal.values
    original_resid = stl.resid.values

    boot_trends = np.zeros((n_bootstrap, n))

    for b in range(n_bootstrap):
        boot_resid = np.zeros(n)
        idx = 0
        while idx < n:
            start = np.random.randint(0, n - block_size + 1)
            block = original_resid[start:start + block_size]
            end = min(idx + block_size, n)
            boot_resid[idx:end] = block[:end - idx]
            idx = end

        boot_series = pd.Series(
            original_trend + original_seasonal + boot_resid,
            index=series.index
        )
        boot_series.index.freq = series.index.freq
        boot_stl = STL(boot_series, period=period, robust=robust).fit()
        boot_trends[b, :] = boot_stl.trend.values

    lower = np.percentile(boot_trends, 5, axis=0)
    upper = np.percentile(boot_trends, 95, axis=0)

    return {
        'trend': original_trend,
        'lower': lower,
        'upper': upper,
        'ci_width': upper - lower
    }


if __name__ == '__main__':
    print('decompose.py loaded successfully.')
    print('Functions: run_stl(), test_stationarity(), detect_breaks(),')
    print('           run_mstl(), block_bootstrap_trend()')
