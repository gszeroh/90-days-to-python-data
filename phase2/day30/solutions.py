"""Day 30: Pandas — Time Series — Solutions

Complete each function below according to its docstring.
"""

import pandas as pd
import numpy as np


# === Exercise 1: Create a Date-Range Series ===

def create_date_series(start, periods, freq, values):
    """Build a Series with a DatetimeIndex.

    Create a pandas Series whose index is a date range beginning at *start*
    with the given number of *periods* and *freq*, and whose values come from
    the *values* list.

    Args:
        start (str): Start date string, e.g. "2024-01-01".
        periods (int): Number of periods to generate.
        freq (str): Frequency alias, e.g. "D", "ME", "W".
        values (list): Data values (same length as *periods*).

    Returns:
        pd.Series: Series indexed by the generated DatetimeIndex.

    Examples:
        create_date_series("2024-01-01", 3, "D", [10, 20, 30])
        -> 2024-01-01    10
           2024-01-02    20
           2024-01-03    30
           Freq: D, dtype: int64
    """
    return pd.Series(values, index=pd.date_range(start, periods=periods, freq=freq))


# === Exercise 2: Extract Date Components ===

def extract_components(s):
    """Return a DataFrame with year, month, and day_name columns.

    Given a Series of datetime values, produce a DataFrame with three
    columns derived from the Series' values:
      - ``"year"``  — the year component
      - ``"month"`` — the month component (1-12)
      - ``"day_name"`` — the English day name (e.g. ``"Monday"``)

    Args:
        s (pd.Series): Series with datetime64 dtype.

    Returns:
        pd.DataFrame: DataFrame with columns ``year``, ``month``,
            ``day_name`` and the same index as *s*.

    Examples:
        s = pd.Series(pd.date_range("2024-01-01", periods=2, freq="D"))
        extract_components(s)
        ->    year  month  day_name
           0  2024      1    Monday
           1  2024      1   Tuesday
    """
    return pd.DataFrame({
        "year": s.dt.year,
        "month": s.dt.month,
        "day_name": s.dt.day_name(),
    })


# === Exercise 3: Monthly Resample ===

def monthly_total(s):
    """Resample a daily Series to month-end totals.

    Down-sample the daily Series *s* (which must have a DatetimeIndex) to
    monthly frequency using the ``"ME"`` rule, summing the values in each
    month.

    Args:
        s (pd.Series): Daily-frequency Series with a DatetimeIndex.

    Returns:
        pd.Series: Month-end indexed Series of summed values.

    Examples:
        idx = pd.date_range("2024-01-01", periods=60, freq="D")
        s = pd.Series(range(60), index=idx)
        monthly_total(s)
        -> 2024-01-31    465
           2024-02-29    1275
           Freq: ME, dtype: int64
    """
    return s.resample("ME").sum()


# === Exercise 4: Rolling Average ===

def rolling_mean(s, window):
    """Compute a rolling mean over the given window size.

    Return a new Series of the same length as *s* containing the rolling
    mean with the specified *window*.  The first ``window - 1`` values will
    be ``NaN``.

    Args:
        s (pd.Series): Numeric Series.
        window (int): Number of observations in the rolling window.

    Returns:
        pd.Series: Rolling mean Series.

    Examples:
        s = pd.Series([1, 3, 5, 7, 9])
        rolling_mean(s, 3)
        -> 0    NaN
           1    NaN
           2    3.0
           3    5.0
           4    7.0
           dtype: float64
    """
    return s.rolling(window=window).mean()


# === Exercise 5: Period-over-Period Growth Rate ===

def growth_rate(s, periods=1):
    """Calculate the period-over-period percentage change.

    Compute the fractional change between each element and the element
    *periods* steps earlier.  The first *periods* values will be ``NaN``.

    Args:
        s (pd.Series): Numeric Series (daily, monthly, etc.).
        periods (int): Number of periods to look back (default 1).

    Returns:
        pd.Series: Series of fractional changes (e.g. 0.10 for +10 %).

    Examples:
        s = pd.Series([100, 110, 121])
        growth_rate(s)
        -> 0         NaN
           1    0.100000
           2    0.100000
           dtype: float64
    """
    return s.pct_change(periods=periods)
