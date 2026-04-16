"""Day 26: Pandas — Data Cleaning — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import pandas as pd
import numpy as np


# === Exercise 1: Fill Missing Values with Strategy ===
def fill_missing(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """Fill missing numeric values using the given strategy.

    Non-numeric columns are left unchanged. Missing values in numeric
    columns are replaced according to *strategy*:
      - "mean"   → column mean
      - "median" → column median
      - "zero"   → 0

    Args:
        df: DataFrame that may contain NaN values.
        strategy: One of "mean", "median", or "zero".

    Returns:
        A new DataFrame with numeric NaN values filled.

    Examples:
        >>> df = pd.DataFrame({"a": [1, np.nan, 3], "b": ["x", "y", None]})
        >>> fill_missing(df, "mean")["a"].tolist()
        [1.0, 2.0, 3.0]
    """
    pass


# === Exercise 2: Remove Duplicates by Subset ===
def dedup_by_columns(df: pd.DataFrame, subset: list[str], keep: str = "first") -> pd.DataFrame:
    """Remove duplicate rows based on a subset of columns.

    Args:
        df: Input DataFrame.
        subset: Column names to consider when identifying duplicates.
        keep: Which occurrence to keep — "first", "last", or False.

    Returns:
        A new DataFrame with duplicates removed and the index reset
        (drop=True).

    Examples:
        >>> df = pd.DataFrame({"a": [1, 2, 1], "b": [10, 20, 30]})
        >>> dedup_by_columns(df, subset=["a"], keep="last")
           a   b
        0  2  20
        1  1  30
    """
    pass


# === Exercise 3: Clean a String Column ===
def clean_string_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Strip whitespace and convert a string column to lowercase.

    Args:
        df: Input DataFrame.
        column: Name of the column to clean.

    Returns:
        A new DataFrame where *column* values are stripped and lowercased.

    Examples:
        >>> df = pd.DataFrame({"name": ["  Alice ", "BOB", " Charlie "]})
        >>> clean_string_column(df, "name")["name"].tolist()
        ['alice', 'bob', 'charlie']
    """
    pass


# === Exercise 4: Convert Mixed-Type Column to Numeric ===
def safe_to_numeric(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Convert a column with mixed types to numeric, coercing errors to NaN.

    Args:
        df: Input DataFrame.
        column: Name of the column to convert.

    Returns:
        A new DataFrame where *column* is numeric (float64). Values that
        cannot be converted are set to NaN.

    Examples:
        >>> df = pd.DataFrame({"val": ["1", "2.5", "bad", "4"]})
        >>> safe_to_numeric(df, "val")["val"].tolist()
        [1.0, 2.5, nan, 4.0]
    """
    pass


# === Exercise 5: Full Cleaning Pipeline ===
def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Apply a complete cleaning pipeline to a DataFrame.

    Steps (in order):
      1. Strip and lowercase all string/object column values.
      2. Drop exact duplicate rows (keep first).
      3. Convert columns named "price" or "quantity" to numeric
         (coerce errors).
      4. Fill remaining NaN values in numeric columns with 0.

    Args:
        df: Raw input DataFrame.

    Returns:
        A cleaned DataFrame with the index reset (drop=True).

    Examples:
        >>> df = pd.DataFrame({
        ...     "product": ["  Widget ", "widget", " GADGET"],
        ...     "price": ["10.5", "10.5", "bad"],
        ...     "quantity": ["3", "3", "5"],
        ... })
        >>> cleaned = clean_pipeline(df)
        >>> len(cleaned)
        2
        >>> cleaned["price"].tolist()
        [10.5, 0.0]
    """
    pass
