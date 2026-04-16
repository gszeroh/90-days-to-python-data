"""Day 24: Pandas — Series & DataFrames — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import pandas as pd
import numpy as np


# === Exercise 1: Create a Series from a Dictionary ===

def series_from_dict(data):
    """Create a pandas Series from a dictionary.

    Args:
        data (dict): Mapping of index labels to values.
            Example: {"a": 10, "b": 20, "c": 30}

    Returns:
        pd.Series: A Series whose index comes from the dict keys and
            whose values come from the dict values.

    Examples:
        series_from_dict({"x": 1, "y": 2, "z": 3})
        -> pd.Series({"x": 1, "y": 2, "z": 3})
    """
    pass


# === Exercise 2: Build a DataFrame from a Dict of Lists ===

def dataframe_from_dict(columns_dict):
    """Build a DataFrame from a dictionary of lists.

    Each key becomes a column name and each list becomes the column values.

    Args:
        columns_dict (dict): Mapping of column names to lists of equal length.
            Example: {"name": ["Alice", "Bob"], "age": [25, 30]}

    Returns:
        pd.DataFrame: A DataFrame with the specified columns.

    Examples:
        dataframe_from_dict({"a": [1, 2], "b": [3, 4]})
        ->    a  b
           0  1  3
           1  2  4
    """
    pass


# === Exercise 3: Select Rows and Columns with loc/iloc ===

def select_rows_cols(df, row_start, row_stop, col_name):
    """Select a range of rows and a single column using label-based indexing.

    Use `.loc[]` to select rows from *row_start* to *row_stop* (inclusive)
    and the column *col_name*.

    Args:
        df (pd.DataFrame): Input DataFrame with a default integer index.
        row_start (int): Starting row label (inclusive).
        row_stop (int): Ending row label (inclusive).
        col_name (str): Name of the column to select.

    Returns:
        pd.Series: The selected slice as a Series.

    Examples:
        df = pd.DataFrame({"x": [10, 20, 30, 40], "y": [1, 2, 3, 4]})
        select_rows_cols(df, 1, 3, "x")
        -> pd.Series([20, 30, 40], index=[1, 2, 3], name="x")
    """
    pass


# === Exercise 4: Add a Computed Column ===

def add_computed_column(df, new_col, col_a, col_b):
    """Add a new column that is the product of two existing columns.

    The original DataFrame must **not** be modified; return a copy with the
    new column appended.

    Args:
        df (pd.DataFrame): Input DataFrame.
        new_col (str): Name for the new column.
        col_a (str): First source column name.
        col_b (str): Second source column name.

    Returns:
        pd.DataFrame: A new DataFrame with the additional column.

    Examples:
        df = pd.DataFrame({"price": [10, 20], "qty": [2, 5]})
        add_computed_column(df, "total", "price", "qty")
        ->    price  qty  total
           0     10    2     20
           1     20    5    100
    """
    pass


# === Exercise 5: Convert Column Data Types ===

def convert_dtypes(df, col_name, target_dtype):
    """Convert a single column to the specified dtype.

    Return a **new** DataFrame (do not modify the original) where the
    column *col_name* has been cast to *target_dtype* using `.astype()`.

    Args:
        df (pd.DataFrame): Input DataFrame.
        col_name (str): Column to convert.
        target_dtype (str): Target dtype string, e.g. "float64", "int64",
            "str", "bool".

    Returns:
        pd.DataFrame: A new DataFrame with the converted column.

    Examples:
        df = pd.DataFrame({"val": [1, 2, 3]})
        result = convert_dtypes(df, "val", "float64")
        result["val"].dtype  # dtype('float64')
    """
    pass
