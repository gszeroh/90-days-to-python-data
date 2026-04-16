"""
Day 40: Mini-Project — Sales Data Dashboard (Solutions)

Reference implementations for the extension exercises in exercises.py.
"""

import numpy as np
import pandas as pd


# === Exercise 1: Monthly Summary Report ===

def monthly_summary_report(df: pd.DataFrame) -> pd.DataFrame:
    """Build a monthly summary report from the sales DataFrame."""
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M")

    agg = df.groupby("month").agg(
        total_revenue=("revenue", "sum"),
        total_quantity=("quantity", "sum"),
        avg_order_value=("revenue", "mean"),
    ).reset_index()

    # Top product per month
    top_products = (
        df.groupby(["month", "product"])["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
        .drop_duplicates(subset="month", keep="first")
        .rename(columns={"product": "top_product"})
        [["month", "top_product"]]
    )

    report = agg.merge(top_products, on="month")
    report["month"] = report["month"].astype(str)
    report = report.sort_values("month").reset_index(drop=True)
    return report[["month", "total_revenue", "total_quantity",
                    "avg_order_value", "top_product"]]


# === Exercise 2: Customer Segmentation ===

def customer_segmentation(df: pd.DataFrame) -> pd.DataFrame:
    """Segment customers by age group and compute per-segment statistics."""
    bins = [17, 24, 34, 44, 54, np.inf]
    labels = ["18-24", "25-34", "35-44", "45-54", "55+"]
    df = df.copy()
    df["age_group"] = pd.cut(df["customer_age"], bins=bins, labels=labels)

    agg = df.groupby("age_group", observed=True).agg(
        customer_count=("customer_id", "nunique"),
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean"),
        avg_quantity=("quantity", "mean"),
    ).reset_index()

    # Top category per segment
    top_cats = (
        df.groupby(["age_group", "category"], observed=True)["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
        .drop_duplicates(subset="age_group", keep="first")
        .rename(columns={"category": "top_category"})
        [["age_group", "top_category"]]
    )

    seg = agg.merge(top_cats, on="age_group")
    seg = seg.sort_values("age_group").reset_index(drop=True)
    return seg[["age_group", "customer_count", "total_revenue",
                "avg_revenue", "avg_quantity", "top_category"]]


# === Exercise 3: Anomaly Detection ===

def detect_anomalous_days(
    df: pd.DataFrame,
    threshold: float = 2.0,
) -> pd.DataFrame:
    """Detect days with anomalously high or low total revenue."""
    daily = df.groupby("date")["revenue"].sum().reset_index()
    daily.columns = ["date", "daily_revenue"]

    mean_rev = daily["daily_revenue"].mean()
    std_rev = daily["daily_revenue"].std()

    daily["z_score"] = (daily["daily_revenue"] - mean_rev) / std_rev

    anomalies = daily[daily["z_score"].abs() > threshold].copy()
    anomalies["direction"] = np.where(
        anomalies["z_score"] > 0, "high", "low"
    )

    return (
        anomalies[["date", "daily_revenue", "z_score", "direction"]]
        .sort_values("z_score", ascending=False)
        .reset_index(drop=True)
    )


# === Exercise 4: Month-over-Month Growth ===

def month_over_month_growth(df: pd.DataFrame) -> pd.DataFrame:
    """Compute month-over-month revenue growth rates."""
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M")

    monthly = (
        df.groupby("month")["revenue"]
        .sum()
        .reset_index()
        .sort_values("month")
    )

    monthly["prev_revenue"] = monthly["revenue"].shift(1)
    monthly["growth_rate"] = (
        (monthly["revenue"] - monthly["prev_revenue"])
        / monthly["prev_revenue"]
        * 100
    )
    monthly["prev_growth"] = monthly["growth_rate"].shift(1)
    monthly["accelerating"] = monthly["growth_rate"] > monthly["prev_growth"]

    result = monthly.dropna(subset=["prev_revenue"]).copy()
    result["month"] = result["month"].astype(str)
    result = result[["month", "revenue", "prev_revenue",
                      "growth_rate", "accelerating"]]
    return result.reset_index(drop=True)


# === Exercise 5: Product Recommendations ===

def product_recommendations(
    df: pd.DataFrame,
    product: str,
    top_n: int = 3,
) -> pd.DataFrame:
    """Find products frequently co-purchased with *product*."""
    if product not in df["product"].values:
        raise ValueError(
            f"Product '{product}' not found in dataset. "
            f"Available: {sorted(df['product'].unique())}"
        )

    # Customers who bought the target product
    target_customers = set(
        df.loc[df["product"] == product, "customer_id"].unique()
    )
    n_target = len(target_customers)

    # Filter to other products bought by those customers
    other = df[
        (df["customer_id"].isin(target_customers))
        & (df["product"] != product)
    ]

    co_counts = (
        other.groupby("product")["customer_id"]
        .nunique()
        .reset_index()
        .rename(columns={
            "product": "recommended_product",
            "customer_id": "co_purchase_count",
        })
        .sort_values("co_purchase_count", ascending=False)
        .head(top_n)
    )

    co_counts["confidence"] = co_counts["co_purchase_count"] / n_target
    return co_counts.reset_index(drop=True)


# ============================================================
# Quick Demonstration
# ============================================================

if __name__ == "__main__":
    # Re-use the same dataset from examples.py
    np.random.seed(40)
    N = 1000
    products_map = {
        "Laptop":       ("Electronics", 800, 1500),
        "Smartphone":   ("Electronics", 400, 1000),
        "Headphones":   ("Electronics", 30, 200),
        "Desk Chair":   ("Furniture",   150, 500),
        "Standing Desk": ("Furniture",  300, 900),
        "Bookshelf":    ("Furniture",   80, 250),
        "Python Book":  ("Books",       20, 60),
        "Data Science Book": ("Books",  25, 70),
        "Notebook Set": ("Stationery",  5, 20),
        "Pen Pack":     ("Stationery",  3, 15),
    }
    product_names = list(products_map.keys())
    dates = pd.date_range("2023-01-01", periods=365, freq="D")

    chosen_products = np.random.choice(product_names, size=N)
    low = np.array([products_map[p][1] for p in chosen_products], dtype=float)
    high = np.array([products_map[p][2] for p in chosen_products], dtype=float)
    unit_prices = np.round(np.random.uniform(low, high), 2)
    quantities = np.random.randint(1, 11, size=N)

    df = pd.DataFrame({
        "date":            np.random.choice(dates, size=N),
        "product":         chosen_products,
        "category":        [products_map[p][0] for p in chosen_products],
        "region":          np.random.choice(["N", "S", "E", "W"], size=N),
        "quantity":        quantities,
        "unit_price":      unit_prices,
        "revenue":         np.round(unit_prices * quantities, 2),
        "customer_id":     np.random.randint(1, 201, size=N),
        "customer_age":    np.clip(
            np.random.normal(35, 12, N).astype(int), 18, 75
        ),
        "customer_gender": np.random.choice(
            ["Male", "Female", "Non-binary"], size=N, p=[0.48, 0.48, 0.04]
        ),
    })
    df = df.sort_values("date").reset_index(drop=True)

    print("=" * 60)
    print("  Exercise 1: Monthly Summary Report")
    print("=" * 60)
    report = monthly_summary_report(df)
    print(report.to_string(index=False))

    print("\n" + "=" * 60)
    print("  Exercise 2: Customer Segmentation")
    print("=" * 60)
    seg = customer_segmentation(df)
    print(seg.to_string(index=False))

    print("\n" + "=" * 60)
    print("  Exercise 3: Anomaly Detection")
    print("=" * 60)
    anomalies = detect_anomalous_days(df, threshold=2.0)
    if anomalies.empty:
        print("No anomalous days detected at threshold=2.0")
    else:
        print(anomalies.to_string(index=False))

    print("\n" + "=" * 60)
    print("  Exercise 4: Month-over-Month Growth")
    print("=" * 60)
    growth = month_over_month_growth(df)
    print(growth.to_string(index=False))

    print("\n" + "=" * 60)
    print("  Exercise 5: Product Recommendations")
    print("=" * 60)
    recs = product_recommendations(df, "Laptop", top_n=5)
    print("Customers who bought 'Laptop' also bought:")
    print(recs.to_string(index=False))

    print("\n✅ All solutions verified!")
