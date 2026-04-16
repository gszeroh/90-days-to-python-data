"""
Day 35: Statistics — Descriptive Statistics — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import numpy as np
import pandas as pd
from scipy import stats


# === Exercise 1: Summary Statistics ===

def summary_stats(data):
    """Return a dictionary of basic descriptive statistics for *data*.

    The dictionary must contain the following keys with numeric values:
        - "mean"   : arithmetic mean
        - "median" : median
        - "mode"   : mode (smallest mode if multimodal)
        - "std"    : sample standard deviation (ddof=1)
        - "var"    : sample variance (ddof=1)

    Parameters
    ----------
    data : list[int | float]
        A non-empty list of numbers.

    Returns
    -------
    dict
        Dictionary with keys "mean", "median", "mode", "std", "var".

    Example
    -------
        summary_stats([4, 8, 6, 5, 3, 8, 9, 8, 2, 6])
        -> {"mean": 5.9, "median": 6.0, "mode": 8,
            "std": 2.2828..., "var": 5.2111...}
    """
    pass


# === Exercise 2: IQR and Outliers ===

def iqr_outliers(data):
    """Compute the IQR and detect outliers using the 1.5 × IQR rule.

    An outlier is any value strictly below Q1 − 1.5·IQR or strictly
    above Q3 + 1.5·IQR.

    Parameters
    ----------
    data : list[int | float]
        A non-empty list of numbers.

    Returns
    -------
    tuple[float, list]
        A 2-tuple of (iqr_value, outliers_list) where *outliers_list*
        contains outlier values in the order they appear in *data*.

    Example
    -------
        iqr_outliers([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
        -> (5.0, [100])
    """
    pass


# === Exercise 3: Skewness and Kurtosis ===

def shape_stats(data):
    """Compute the skewness and excess kurtosis for *data*.

    Use the default bias setting from ``scipy.stats``.

    Parameters
    ----------
    data : list[int | float]
        A list of numbers with at least 3 elements.

    Returns
    -------
    dict
        Dictionary with keys "skewness" and "kurtosis" (excess / Fisher).

    Example
    -------
        shape_stats([1, 2, 2, 3, 3, 3, 4, 4, 5])
        -> {"skewness": 0.0, "kurtosis": -0.8161...}
    """
    pass


# === Exercise 4: Percentile Ranks ===

def percentile_ranks(data):
    """Return the percentile rank of every element in *data*.

    The percentile rank of a value *v* is the percentage of values in
    *data* that are less than or equal to *v*.  Use
    ``scipy.stats.percentileofscore`` with ``kind='rank'``.

    Parameters
    ----------
    data : list[int | float]
        A non-empty list of numbers.

    Returns
    -------
    list[float]
        A list of percentile ranks (0–100), one per element, in the
        same order as the input.

    Example
    -------
        percentile_ranks([10, 20, 30, 40, 50])
        -> [20.0, 40.0, 60.0, 80.0, 100.0]
    """
    pass


# === Exercise 5: Frequency Distribution Table ===

def frequency_table(data):
    """Build a frequency distribution table from *data*.

    Parameters
    ----------
    data : list
        A list of discrete / categorical values.

    Returns
    -------
    pandas.DataFrame
        A DataFrame sorted by *value* (ascending) with the columns:
            - "value"          : unique data values
            - "frequency"      : absolute count of each value
            - "relative_freq"  : frequency / total (rounded to 4 decimals)
            - "cumulative_freq": running total of frequency

    Example
    -------
        frequency_table([1, 2, 2, 3, 3, 3])
        ->    value  frequency  relative_freq  cumulative_freq
           0      1          1         0.1667                1
           1      2          2         0.3333                3
           2      3          3         0.5000                6
    """
    pass
