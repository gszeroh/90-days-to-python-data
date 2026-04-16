"""
Day 40: Mini-Project — Sales Data Dashboard (Exercises)

These extension exercises build on top of the Sales Data Dashboard from
examples.py.  Each exercise asks you to add a new analytical capability.
Replace ``pass`` with your implementation.
"""

import numpy as np
import pandas as pd


# === Exercise 1: Monthly Summary Report ===

def monthly_summary_report(df: pd.DataFrame) -> pd.DataFrame:
    """Build a monthly summary report from the sales DataFrame.

    The returned DataFrame must have one row per calendar month and the
    following columns (in order):

        month           — Period string, e.g. "2023-01"
        total_revenue   — Sum of revenue in that month
        total_quantity  — Sum of quantity sold
        avg_order_value — Mean revenue per transaction
        top_product     — Product with the highest total revenue that month

    Args:
        df: Sales DataFrame with at least the columns
            ``date``, ``revenue``, ``quantity``, ``product``.

    Returns:
        A DataFrame sorted by *month* ascending.

    Examples:
        >>> report = monthly_summary_report(df)
        >>> list(report.columns)
        ['month', 'total_revenue', 'total_quantity', 'avg_order_value', 'top_product']
        >>> len(report)  # 12 months for a full year
        12
    """
    pass


# === Exercise 2: Customer Segmentation ===

def customer_segmentation(df: pd.DataFrame) -> pd.DataFrame:
    """Segment customers by age group and compute per-segment statistics.

    Age groups (inclusive bounds):
        "18-24", "25-34", "35-44", "45-54", "55+"

    The returned DataFrame must have one row per age group and the
    following columns:

        age_group       — The label above
        customer_count  — Number of unique customers in the segment
        total_revenue   — Sum of revenue
        avg_revenue     — Mean revenue per transaction
        avg_quantity    — Mean quantity per transaction
        top_category    — Category with the highest total revenue in the segment

    Args:
        df: Sales DataFrame with at least the columns
            ``customer_id``, ``customer_age``, ``revenue``, ``quantity``,
            ``category``.

    Returns:
        A DataFrame sorted by age group order (youngest first).

    Examples:
        >>> seg = customer_segmentation(df)
        >>> seg.columns.tolist()
        ['age_group', 'customer_count', 'total_revenue', 'avg_revenue', 'avg_quantity', 'top_category']
    """
    pass


# === Exercise 3: Anomaly Detection ===

def detect_anomalous_days(
    df: pd.DataFrame,
    threshold: float = 2.0,
) -> pd.DataFrame:
    """Detect days with anomalously high or low total revenue.

    Steps:
        1. Aggregate revenue by date (sum per day).
        2. Compute the z-score for each day's total revenue.
        3. Flag days where ``abs(z_score) > threshold``.

    The returned DataFrame must have the following columns:

        date          — The anomalous date
        daily_revenue — Total revenue on that date
        z_score       — The z-score (positive = unusually high)
        direction     — "high" if z_score > threshold, "low" if < -threshold

    Args:
        df: Sales DataFrame with ``date`` and ``revenue`` columns.
        threshold: Z-score absolute value above which a day is anomalous.
                   Defaults to 2.0.

    Returns:
        A DataFrame of anomalous days sorted by z_score descending.

    Examples:
        >>> anomalies = detect_anomalous_days(df, threshold=2.0)
        >>> "z_score" in anomalies.columns
        True
    """
    pass


# === Exercise 4: Month-over-Month Growth ===

def month_over_month_growth(df: pd.DataFrame) -> pd.DataFrame:
    """Compute month-over-month revenue growth rates.

    The returned DataFrame must have one row per month (excluding the
    first month, which has no prior month for comparison) and columns:

        month          — Period string, e.g. "2023-02"
        revenue        — Total revenue in that month
        prev_revenue   — Total revenue in the prior month
        growth_rate    — Percentage change: (revenue - prev) / prev * 100
        accelerating   — Boolean: True if growth_rate > previous growth_rate

    Args:
        df: Sales DataFrame with ``date`` and ``revenue`` columns.

    Returns:
        A DataFrame sorted by month ascending.

    Examples:
        >>> growth = month_over_month_growth(df)
        >>> growth["growth_rate"].dtype
        dtype('float64')
    """
    pass


# === Exercise 5: Product Recommendations ===

def product_recommendations(
    df: pd.DataFrame,
    product: str,
    top_n: int = 3,
) -> pd.DataFrame:
    """Find products frequently co-purchased with *product*.

    "Co-purchase" means the same ``customer_id`` bought both *product*
    and another product (in any transaction, not necessarily the same
    order).

    The returned DataFrame must have columns:

        recommended_product — Product name
        co_purchase_count   — Number of unique customers who bought both
        confidence          — co_purchase_count / total customers who bought *product*

    Args:
        df: Sales DataFrame with ``customer_id`` and ``product`` columns.
        product: The reference product to find recommendations for.
        top_n: Number of recommendations to return.

    Returns:
        A DataFrame sorted by *co_purchase_count* descending, limited
        to *top_n* rows.

    Raises:
        ValueError: If *product* is not found in the dataset.

    Examples:
        >>> recs = product_recommendations(df, "Laptop", top_n=3)
        >>> list(recs.columns)
        ['recommended_product', 'co_purchase_count', 'confidence']
    """
    pass
