"""
Day 25: Pandas — Data Loading & Inspection — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
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
    pass


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
    pass


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
    pass


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
    pass


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
    pass
