"""Day 28: Pandas — Grouping & Aggregation — Examples"""

import pandas as pd
import numpy as np


# === 1. GroupBy Basics ===

print("=" * 60)
print("1. GroupBy Basics")
print("=" * 60)

employees = pd.DataFrame({
    "dept": ["Sales", "Sales", "HR", "HR", "Engineering", "Engineering"],
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"],
    "salary": [70000, 80000, 65000, 72000, 95000, 88000],
    "years": [3, 5, 2, 7, 4, 6],
})

print("\nEmployee DataFrame:")
print(employees)

grouped = employees.groupby("dept")
print(f"\nNumber of groups: {grouped.ngroups}")
print(f"Group keys: {list(grouped.groups.keys())}")

print("\nIterating over groups:")
for dept_name, dept_df in grouped:
    print(f"\n  {dept_name} ({len(dept_df)} employees):")
    print(dept_df.to_string(index=False))


# === 2. Aggregation Functions ===

print("\n" + "=" * 60)
print("2. Aggregation Functions")
print("=" * 60)

print("\nMean salary by department:")
print(grouped["salary"].mean())

print("\nMultiple aggregations on salary:")
print(grouped["salary"].agg(["mean", "min", "max", "std"]))

print("\nDifferent aggregations per column (dict):")
print(grouped.agg({"salary": ["mean", "sum"], "years": "max"}))

print("\nCustom aggregation — salary range per department:")
print(grouped["salary"].agg(lambda x: x.max() - x.min()))


# === 3. Named Aggregation ===

print("\n" + "=" * 60)
print("3. Named Aggregation")
print("=" * 60)

summary = grouped.agg(
    avg_salary=("salary", "mean"),
    headcount=("name", "count"),
    max_years=("years", "max"),
    salary_range=("salary", lambda x: x.max() - x.min()),
)

print("\nNamed aggregation result:")
print(summary)
print(f"\nColumn names: {list(summary.columns)}")


# === 4. transform() — Broadcasting Group Results ===

print("\n" + "=" * 60)
print("4. transform() — Broadcasting Group Results")
print("=" * 60)

employees["dept_mean_salary"] = grouped["salary"].transform("mean")
print("\nDataFrame with department mean broadcast to each row:")
print(employees[["name", "dept", "salary", "dept_mean_salary"]])

employees["pct_of_dept"] = (
    employees["salary"] / grouped["salary"].transform("sum") * 100
).round(1)
print("\nEach employee's share of department salary budget:")
print(employees[["name", "dept", "salary", "pct_of_dept"]])

employees["z_score"] = grouped["salary"].transform(
    lambda x: (x - x.mean()) / x.std() if len(x) > 1 else 0.0
).round(3)
print("\nGroup z-scores:")
print(employees[["name", "dept", "salary", "z_score"]])

# Clean up helper columns
employees.drop(columns=["dept_mean_salary", "pct_of_dept", "z_score"],
               inplace=True)


# === 5. pivot_table() ===

print("\n" + "=" * 60)
print("5. pivot_table()")
print("=" * 60)

sales = pd.DataFrame({
    "region": ["East", "East", "West", "West", "East", "West"],
    "product": ["Widget", "Gadget", "Widget", "Gadget", "Widget", "Widget"],
    "revenue": [100, 200, 150, 250, 130, 170],
    "quantity": [10, 15, 12, 20, 11, 14],
})

print("\nSales DataFrame:")
print(sales)

pivot = sales.pivot_table(
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0,
)
print("\nPivot table — total revenue by region and product:")
print(pivot)

pivot_margins = sales.pivot_table(
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0,
    margins=True,
)
print("\nPivot table with margins (totals):")
print(pivot_margins)

pivot_multi = sales.pivot_table(
    values=["revenue", "quantity"],
    index="region",
    aggfunc={"revenue": "sum", "quantity": "mean"},
)
print("\nPivot table — different aggregations per value:")
print(pivot_multi)


# === 6. crosstab() ===

print("\n" + "=" * 60)
print("6. crosstab()")
print("=" * 60)

print("\nFrequency cross-tabulation (region × product):")
ct = pd.crosstab(sales["region"], sales["product"])
print(ct)

print("\nRow-normalised cross-tabulation (proportions):")
ct_norm = pd.crosstab(sales["region"], sales["product"], normalize="index")
print(ct_norm.round(3))

print("\nAggregated cross-tab — mean revenue:")
ct_agg = pd.crosstab(
    sales["region"],
    sales["product"],
    values=sales["revenue"],
    aggfunc="mean",
)
print(ct_agg)

print("\nCross-tab with margins:")
ct_margins = pd.crosstab(
    sales["region"], sales["product"], margins=True,
)
print(ct_margins)
