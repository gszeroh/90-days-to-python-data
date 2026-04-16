"""Day 28: Pandas — Grouping & Aggregation — Solutions"""

import pandas as pd
import numpy as np


# === Exercise 1: Group and Sum ===

def total_salary_by_dept(df: pd.DataFrame) -> pd.Series:
    """Return total salary for each department, sorted by department name.

    Parameters:
        df: DataFrame with columns 'dept' and 'salary'.

    Returns:
        A Series indexed by 'dept' with the sum of 'salary' per group,
        sorted alphabetically by department name.

    Example:
        >>> data = pd.DataFrame({
        ...     "dept": ["Sales", "HR", "Sales", "HR"],
        ...     "salary": [50000, 60000, 70000, 55000],
        ... })
        >>> total_salary_by_dept(data)
        dept
        HR       115000
        Sales    120000
        Name: salary, dtype: int64
    """
    return df.groupby("dept")["salary"].sum().sort_index()


# === Exercise 2: Multi-Aggregation with Named Aggregation ===

def department_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a summary DataFrame with named aggregation columns.

    Parameters:
        df: DataFrame with columns 'dept', 'salary', and 'name'.

    Returns:
        A DataFrame indexed by 'dept' with the following columns:
        - avg_salary: mean of 'salary'
        - max_salary: max of 'salary'
        - headcount:  count of 'name'

    Example:
        >>> data = pd.DataFrame({
        ...     "dept": ["Sales", "Sales", "HR"],
        ...     "name": ["Alice", "Bob", "Carol"],
        ...     "salary": [70000, 80000, 65000],
        ... })
        >>> department_summary(data)
              avg_salary  max_salary  headcount
        dept
        HR       65000.0       65000          1
        Sales    75000.0       80000          2
    """
    return df.groupby("dept").agg(
        avg_salary=("salary", "mean"),
        max_salary=("salary", "max"),
        headcount=("name", "count"),
    )


# === Exercise 3: Group Z-Scores with transform ===

def add_group_zscore(df: pd.DataFrame) -> pd.DataFrame:
    """Add a 'z_score' column with each row's z-score within its department.

    The z-score is (value - group_mean) / group_std.  For groups with only
    one member (std == 0), the z-score should be 0.0.

    Parameters:
        df: DataFrame with columns 'dept' and 'salary'.

    Returns:
        A *copy* of df with an additional column 'z_score' (float, rounded
        to 4 decimal places).

    Example:
        >>> data = pd.DataFrame({
        ...     "dept": ["A", "A", "B"],
        ...     "salary": [50000, 70000, 60000],
        ... })
        >>> add_group_zscore(data)["z_score"].tolist()
        [-0.7071, 0.7071, 0.0]
    """
    result = df.copy()
    grouped = result.groupby("dept")["salary"]
    result["z_score"] = grouped.transform(
        lambda x: (x - x.mean()) / x.std() if len(x) > 1 else 0.0
    ).round(4)
    return result


# === Exercise 4: Pivot Table ===

def revenue_pivot(df: pd.DataFrame) -> pd.DataFrame:
    """Create a pivot table of total revenue by region and product.

    Parameters:
        df: DataFrame with columns 'region', 'product', and 'revenue'.

    Returns:
        A pivot table with 'region' as index, 'product' as columns, total
        revenue as values, and 0 for missing combinations.

    Example:
        >>> data = pd.DataFrame({
        ...     "region": ["East", "East", "West"],
        ...     "product": ["Widget", "Gadget", "Widget"],
        ...     "revenue": [100, 200, 150],
        ... })
        >>> revenue_pivot(data)
        product  Gadget  Widget
        region
        East        200     100
        West          0     150
    """
    return df.pivot_table(
        values="revenue",
        index="region",
        columns="product",
        aggfunc="sum",
        fill_value=0,
    )


# === Exercise 5: Cross-Tabulation Analysis ===

def normalised_crosstab(
    s1: pd.Series, s2: pd.Series
) -> pd.DataFrame:
    """Return a row-normalised cross-tabulation of two categorical Series.

    Parameters:
        s1: Series used as the index of the cross-tabulation.
        s2: Series used as the columns of the cross-tabulation.

    Returns:
        A DataFrame of row proportions (each row sums to 1.0), rounded to
        4 decimal places.

    Example:
        >>> s1 = pd.Series(["A", "A", "B", "B", "B"])
        >>> s2 = pd.Series(["X", "Y", "X", "X", "Y"])
        >>> normalised_crosstab(s1, s2)
             X       Y
        A  0.5000  0.5000
        B  0.6667  0.3333
    """
    return pd.crosstab(s1, s2, normalize="index").round(4)
