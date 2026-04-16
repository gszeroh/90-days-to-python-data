"""Day 39: Exploratory Data Analysis (EDA) — Solutions"""

import numpy as np
import pandas as pd


# === Exercise 1: EDA Summary Report ===

def eda_summary(df):
    """Return a comprehensive EDA summary report for a DataFrame.

    The returned dictionary must contain exactly these keys:
      - "shape": tuple of (rows, columns)
      - "dtypes": dict mapping column name to dtype string
      - "missing_counts": dict mapping column name to int count of NaN values
      - "numeric_summary": DataFrame produced by df.describe() on numeric cols
      - "categorical_summary": dict mapping each non-numeric column name
        to a dict of its value counts (value -> count)

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict

    Examples
    --------
    >>> df = pd.DataFrame({"a": [1, 2, None], "b": ["x", "y", "x"]})
    >>> result = eda_summary(df)
    >>> result["shape"]
    (3, 2)
    >>> result["missing_counts"]["a"]
    1
    >>> "b" in result["categorical_summary"]
    True
    """
    numeric_summary = df.describe()
    categorical_cols = df.select_dtypes(exclude="number").columns
    categorical_summary = {
        col: df[col].value_counts().to_dict() for col in categorical_cols
    }

    return {
        "shape": df.shape,
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_counts": {col: int(df[col].isnull().sum()) for col in df.columns},
        "numeric_summary": numeric_summary,
        "categorical_summary": categorical_summary,
    }


# === Exercise 2: IQR Outlier Detection ===

def detect_outliers_iqr(df):
    """Detect outliers in every numeric column using the IQR method.

    For each numeric column, compute Q1 (25th percentile) and Q3 (75th
    percentile). A value is an outlier if it falls below Q1 - 1.5 * IQR
    or above Q3 + 1.5 * IQR.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
        Mapping of column name (str) to a sorted list of outlier values.
        Only include columns that have at least one outlier.

    Examples
    --------
    >>> df = pd.DataFrame({"x": [1, 2, 3, 4, 100], "y": [10, 20, 30, 40, 50]})
    >>> result = detect_outliers_iqr(df)
    >>> "x" in result
    True
    >>> result["x"]
    [100]
    """
    result = {}
    for col in df.select_dtypes(include="number").columns:
        series = df[col].dropna()
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = sorted(series[(series < lower) | (series > upper)].tolist())
        if outliers:
            result[col] = outliers
    return result


# === Exercise 3: Correlation Analysis ===

def analyze_correlations(df, threshold=0.7):
    """Compute the correlation matrix and find highly correlated pairs.

    Parameters
    ----------
    df : pandas.DataFrame
        Must contain at least two numeric columns.
    threshold : float, optional
        Absolute correlation value above which a pair is considered
        highly correlated. Default is 0.7.

    Returns
    -------
    tuple[pandas.DataFrame, list[tuple[str, str, float]]]
        A 2-element tuple:
          - The full correlation matrix (DataFrame).
          - A list of tuples (col_a, col_b, r) for every unique pair
            where |r| > threshold, sorted by |r| descending.
            Each pair appears only once (col_a < col_b alphabetically).

    Examples
    --------
    >>> df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 4, 6], "c": [9, 7, 5]})
    >>> corr_matrix, pairs = analyze_correlations(df, threshold=0.9)
    >>> isinstance(corr_matrix, pd.DataFrame)
    True
    >>> len(pairs) > 0
    True
    >>> all(abs(r) > 0.9 for _, _, r in pairs)
    True
    """
    corr_matrix = df.corr(numeric_only=True)
    cols = corr_matrix.columns.tolist()
    pairs = []

    for i, col_a in enumerate(cols):
        for j in range(i + 1, len(cols)):
            col_b = cols[j]
            r = float(corr_matrix.loc[col_a, col_b])
            if abs(r) > threshold:
                a, b = sorted([col_a, col_b])
                pairs.append((a, b, r))

    pairs.sort(key=lambda t: abs(t[2]), reverse=True)
    return corr_matrix, pairs


# === Exercise 4: Univariate Column Summary ===

def univariate_summary(series):
    """Return a univariate summary for a single pandas Series.

    If the Series is **numeric**, return a dict with keys:
      "mean", "median", "mode", "std", "skew", "kurtosis"
    (all floats; if mode has multiple values, use the first).

    If the Series is **categorical / object**, return a dict with keys:
      "mode", "nunique", "value_counts"
    where "value_counts" is a dict of value -> count and "mode" is a
    string.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict

    Examples
    --------
    >>> s = pd.Series([1, 2, 2, 3, 4])
    >>> result = univariate_summary(s)
    >>> result["mean"]
    2.4
    >>> result["mode"]
    2.0

    >>> s = pd.Series(["a", "b", "a", "c"])
    >>> result = univariate_summary(s)
    >>> result["mode"]
    'a'
    >>> result["nunique"]
    3
    """
    if pd.api.types.is_numeric_dtype(series):
        return {
            "mean": float(series.mean()),
            "median": float(series.median()),
            "mode": float(series.mode().iloc[0]),
            "std": float(series.std()),
            "skew": float(series.skew()),
            "kurtosis": float(series.kurtosis()),
        }

    return {
        "mode": str(series.mode().iloc[0]),
        "nunique": int(series.nunique()),
        "value_counts": series.value_counts().to_dict(),
    }


# === Exercise 5: Clean DataFrame for Analysis ===

def clean_dataframe(df, config):
    """Clean a DataFrame according to the supplied configuration.

    The *config* dict may contain any combination of these keys:
      - "drop_duplicates" (bool): if True, drop duplicate rows.
      - "drop_columns" (list[str]): column names to drop.
      - "fill_strategy" (dict[str, str]): mapping of column name to a
        fill strategy string — one of "mean", "median", "mode", or
        "drop" (drop rows where this column is NaN).

    Operations should be applied in this order:
      1. drop_columns
      2. drop_duplicates
      3. fill_strategy

    Return a **new** DataFrame; do not modify the original.

    Parameters
    ----------
    df : pandas.DataFrame
    config : dict

    Returns
    -------
    pandas.DataFrame

    Examples
    --------
    >>> df = pd.DataFrame({"a": [1, 2, 2, None], "b": [5, 5, 5, 5]})
    >>> cfg = {"drop_duplicates": True, "fill_strategy": {"a": "mean"}}
    >>> cleaned = clean_dataframe(df, cfg)
    >>> int(cleaned["a"].isnull().sum())
    0
    >>> len(cleaned) <= len(df)
    True
    """
    result = df.copy()

    # 1. Drop columns
    drop_cols = config.get("drop_columns", [])
    result = result.drop(columns=[c for c in drop_cols if c in result.columns])

    # 2. Drop duplicates
    if config.get("drop_duplicates", False):
        result = result.drop_duplicates()

    # 3. Fill strategies
    for col, strategy in config.get("fill_strategy", {}).items():
        if col not in result.columns:
            continue
        if strategy == "mean":
            result[col] = result[col].fillna(result[col].mean())
        elif strategy == "median":
            result[col] = result[col].fillna(result[col].median())
        elif strategy == "mode":
            mode_val = result[col].mode().iloc[0]
            result[col] = result[col].fillna(mode_val)
        elif strategy == "drop":
            result = result.dropna(subset=[col])

    return result.reset_index(drop=True)
