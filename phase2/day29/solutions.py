"""Day 29: Pandas — Merging & Joining — Solutions

Complete each function below according to its docstring.
"""

import pandas as pd
import numpy as np


# === Exercise 1: Concat Vertically with Reset Index ===

def concat_vertical(df1, df2):
    """Concatenate two DataFrames vertically with a clean integer index.

    Stack df1 on top of df2 and reset the index so that the resulting
    DataFrame has a continuous 0-based integer index.

    Args:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame (same columns as df1).

    Returns:
        pd.DataFrame: Combined DataFrame with reset index.

    Examples:
        df1 = pd.DataFrame({"A": [1, 2]})
        df2 = pd.DataFrame({"A": [3, 4]})
        concat_vertical(df1, df2)
        ->    A
           0  1
           1  2
           2  3
           3  4
    """
    return pd.concat([df1, df2], ignore_index=True)


# === Exercise 2: Inner Merge ===

def inner_merge(left, right, key):
    """Perform an inner merge on a single key column.

    Return only the rows where the key exists in both DataFrames.

    Args:
        left (pd.DataFrame): Left DataFrame.
        right (pd.DataFrame): Right DataFrame.
        key (str): Column name to join on.

    Returns:
        pd.DataFrame: Inner-merged result.

    Examples:
        left  = pd.DataFrame({"id": [1, 2, 3], "v": ["a", "b", "c"]})
        right = pd.DataFrame({"id": [2, 3, 4], "w": ["x", "y", "z"]})
        inner_merge(left, right, "id")
        ->    id  v  w
           0   2  b  x
           1   3  c  y
    """
    return pd.merge(left, right, on=key, how="inner")


# === Exercise 3: Left Merge with Indicator ===

def left_merge_with_indicator(left, right, key):
    """Left-merge two DataFrames and add a merge indicator column.

    Perform a left join on the given key column with indicator=True so
    that the result contains a '_merge' column showing match status.

    Args:
        left (pd.DataFrame): Left DataFrame.
        right (pd.DataFrame): Right DataFrame.
        key (str): Column name to join on.

    Returns:
        pd.DataFrame: Left-merged result with '_merge' column.

    Examples:
        left  = pd.DataFrame({"id": [1, 2, 3], "v": ["a", "b", "c"]})
        right = pd.DataFrame({"id": [2, 3, 4], "w": ["x", "y", "z"]})
        left_merge_with_indicator(left, right, "id")
        ->    id  v    w      _merge
           0   1  a  NaN   left_only
           1   2  b    x        both
           2   3  c    y        both
    """
    return pd.merge(left, right, on=key, how="left", indicator=True)


# === Exercise 4: Multi-key Merge ===

def multi_key_merge(left, right, keys):
    """Merge two DataFrames on multiple key columns using an inner join.

    Args:
        left (pd.DataFrame): Left DataFrame.
        right (pd.DataFrame): Right DataFrame.
        keys (list[str]): List of column names to join on.

    Returns:
        pd.DataFrame: Inner-merged result on the given keys.

    Examples:
        left  = pd.DataFrame({"year": [2023, 2023], "qtr": ["Q1", "Q2"], "rev": [100, 200]})
        right = pd.DataFrame({"year": [2023, 2023], "qtr": ["Q1", "Q2"], "target": [90, 180]})
        multi_key_merge(left, right, ["year", "qtr"])
        ->    year qtr  rev  target
           0  2023  Q1  100      90
           1  2023  Q2  200     180
    """
    return pd.merge(left, right, on=keys, how="inner")


# === Exercise 5: Combine Three Tables ===

def combine_three_tables(orders, customers, products):
    """Combine orders with customer names and product names.

    1. Left-merge orders with customers on 'customer_id'.
    2. Left-merge the result with products on 'product_id'.
    Return the final combined DataFrame.

    Args:
        orders (pd.DataFrame): Must contain 'customer_id' and 'product_id'.
        customers (pd.DataFrame): Must contain 'customer_id' and 'name'.
        products (pd.DataFrame): Must contain 'product_id' and 'product'.

    Returns:
        pd.DataFrame: Orders enriched with customer name and product name.

    Examples:
        orders = pd.DataFrame({"order_id": [1], "customer_id": [10], "product_id": [100]})
        customers = pd.DataFrame({"customer_id": [10], "name": ["Alice"]})
        products = pd.DataFrame({"product_id": [100], "product": ["Widget"]})
        combine_three_tables(orders, customers, products)
        ->    order_id  customer_id  product_id   name  product
           0         1           10         100  Alice   Widget
    """
    merged = pd.merge(orders, customers, on="customer_id", how="left")
    return pd.merge(merged, products, on="product_id", how="left")
