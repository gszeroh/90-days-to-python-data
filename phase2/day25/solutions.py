"""
Day 25: Pandas — Data Loading & Inspection — Solutions
"""

import pandas as pd
import numpy as np
from io import StringIO


# === Exercise 1: Parse CSV from StringIO ===

def parse_csv_string(csv_string, parse_dates_cols=None):
    """Read a CSV-formatted string into a DataFrame.

    Parameters
    ----------
    csv_string : str
        A valid CSV string (with header row).
    parse_dates_cols : list[str] or None
        Column names to parse as datetime. None means no date parsing.

    Returns
    -------
    pd.DataFrame

    Example:
        csv = "name,age\\nAlice,30\\nBob,25"
        parse_csv_string(csv) -> DataFrame with 2 rows, 2 columns
    """
    kwargs = {}
    if parse_dates_cols is not None:
        kwargs["parse_dates"] = parse_dates_cols
    return pd.read_csv(StringIO(csv_string), **kwargs)


# === Exercise 2: Inspection Summary Dict ===

def inspection_summary(df):
    """Return a dictionary summarising key properties of a DataFrame.

    The dictionary must contain exactly these keys:
        "nrows"   : int — number of rows
        "ncols"   : int — number of columns
        "columns" : list[str] — column names
        "dtypes"  : dict — mapping of column name to dtype string (e.g. "int64")
        "null_counts" : dict — mapping of column name to count of null values

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    dict

    Example:
        inspection_summary(df)["nrows"] -> 100
    """
    return {
        "nrows": df.shape[0],
        "ncols": df.shape[1],
        "columns": df.columns.tolist(),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "null_counts": df.isnull().sum().to_dict(),
    }


# === Exercise 3: Columns with Nulls ===

def columns_with_nulls(df):
    """Return a list of column names that contain at least one null value,
    sorted alphabetically.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    list[str]

    Example:
        columns_with_nulls(df) -> ["age", "city"]
    """
    null_counts = df.isnull().sum()
    return sorted(null_counts[null_counts > 0].index.tolist())


# === Exercise 4: Value Counts Analysis ===

def top_n_values(series, n=3):
    """Return the top *n* most frequent values in a Series as a dictionary.

    Keys are the values from the Series, and dict values are their counts.

    Parameters
    ----------
    series : pd.Series
    n : int
        Number of top values to return (default 3).

    Returns
    -------
    dict

    Example:
        top_n_values(pd.Series(["a","b","a","a","b","c"]), n=2)
        -> {"a": 3, "b": 2}
    """
    return series.value_counts().head(n).to_dict()


# === Exercise 5: Memory Usage Report ===

def memory_usage_report(df):
    """Return a dictionary with memory-usage information for *df*.

    The dictionary must contain exactly these keys:
        "per_column" : dict — column name -> deep memory in bytes (int)
        "total_bytes" : int — total deep memory usage in bytes
        "total_mb"    : float — total deep memory usage in megabytes,
                        rounded to 4 decimal places

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    dict

    Example:
        memory_usage_report(df)["total_bytes"] -> 12400
    """
    mem = df.memory_usage(deep=True)
    # Exclude the index entry for per-column breakdown
    per_column = mem.iloc[1:].to_dict()
    total_bytes = mem.sum()
    return {
        "per_column": {col: int(val) for col, val in per_column.items()},
        "total_bytes": int(total_bytes),
        "total_mb": round(total_bytes / (1024 * 1024), 4),
    }
