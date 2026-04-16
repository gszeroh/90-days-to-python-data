"""Day 29: Pandas — Merging & Joining — Examples"""

import pandas as pd
import numpy as np


# === 1. pd.concat() — Stacking DataFrames ===

print("--- Vertical concat (axis=0) ---")
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

stacked = pd.concat([df1, df2], ignore_index=True)
print(stacked)

print("\n--- Vertical concat without ignore_index ---")
print(pd.concat([df1, df2]))  # indices 0,1,0,1

print("\n--- Horizontal concat (axis=1) ---")
print(pd.concat([df1, df2], axis=1))

print("\n--- concat with keys (MultiIndex) ---")
multi = pd.concat([df1, df2], keys=["first", "second"])
print(multi)
print("\nAccess 'first' group:")
print(multi.loc["first"])


# === 2. pd.merge() — SQL-style Joins ===

print("\n--- Setting up orders & customers ---")
orders = pd.DataFrame({
    "order_id": [1, 2, 3],
    "customer_id": [10, 20, 30],
    "amount": [100.0, 250.0, 50.0],
})
customers = pd.DataFrame({
    "customer_id": [10, 20, 40],
    "name": ["Alice", "Bob", "Diana"],
})
print("Orders:\n", orders)
print("Customers:\n", customers)

print("\n--- Inner join (default) ---")
inner = pd.merge(orders, customers, on="customer_id")
print(inner)

print("\n--- Left join ---")
left = pd.merge(orders, customers, on="customer_id", how="left")
print(left)

print("\n--- Right join ---")
right = pd.merge(orders, customers, on="customer_id", how="right")
print(right)

print("\n--- Outer join ---")
outer = pd.merge(orders, customers, on="customer_id", how="outer")
print(outer)


# === 3. Merge on Multiple Keys & Suffixes ===

print("\n--- Merge on multiple keys ---")
sales_q = pd.DataFrame({
    "year": [2023, 2023, 2024],
    "quarter": ["Q1", "Q2", "Q1"],
    "revenue": [1000, 1500, 1200],
})
targets_q = pd.DataFrame({
    "year": [2023, 2023, 2024],
    "quarter": ["Q1", "Q2", "Q1"],
    "target": [900, 1400, 1100],
})
merged_multi = pd.merge(sales_q, targets_q, on=["year", "quarter"])
print(merged_multi)

print("\n--- Merge with left_on / right_on ---")
employees = pd.DataFrame({"emp_id": [1, 2], "name": ["Alice", "Bob"]})
reviews = pd.DataFrame({"employee_id": [1, 2], "score": [4.5, 3.8]})
merged_diff = pd.merge(employees, reviews, left_on="emp_id", right_on="employee_id")
print(merged_diff)

print("\n--- Custom suffixes ---")
jan = pd.DataFrame({"product": ["A", "B"], "sales": [100, 200]})
feb = pd.DataFrame({"product": ["A", "B"], "sales": [120, 180]})
merged_suf = pd.merge(jan, feb, on="product", suffixes=("_jan", "_feb"))
print(merged_suf)


# === 4. .join() — Index-based Joining ===

print("\n--- DataFrame.join() on index ---")
df_left = pd.DataFrame(
    {"salary": [70_000, 80_000, 65_000]},
    index=["Alice", "Bob", "Carol"],
)
df_right = pd.DataFrame(
    {"dept": ["Eng", "Sales", "Eng"]},
    index=["Alice", "Bob", "Diana"],
)
print("Left:\n", df_left)
print("Right:\n", df_right)

print("\n--- Left join (default for .join()) ---")
print(df_left.join(df_right))

print("\n--- Inner join via .join() ---")
print(df_left.join(df_right, how="inner"))

print("\n--- .join() with on= (column to index) ---")
staff = pd.DataFrame({"name": ["Alice", "Bob"], "years": [5, 3]})
dept_info = pd.DataFrame(
    {"budget": [500_000, 300_000]},
    index=["Eng", "Sales"],
)
dept_lookup = pd.DataFrame({"name": ["Alice", "Bob"], "dept": ["Eng", "Sales"]})
print(dept_lookup.join(dept_info, on="dept"))


# === 5. Merge Indicator (_merge column) ===

print("\n--- Merge with indicator=True ---")
result = pd.merge(
    orders, customers,
    on="customer_id",
    how="outer",
    indicator=True,
)
print(result)

print("\n--- Filter unmatched rows ---")
left_only = result[result["_merge"] == "left_only"]
print("Left-only rows (orders without customers):")
print(left_only)

right_only = result[result["_merge"] == "right_only"]
print("Right-only rows (customers without orders):")
print(right_only)


# === 6. Handling Duplicates & Validation ===

print("\n--- Many-to-many merge (Cartesian product) ---")
df_m = pd.DataFrame({"key": ["A", "A", "B"], "val_left": [1, 2, 3]})
df_n = pd.DataFrame({"key": ["A", "A", "B"], "val_right": [10, 20, 30]})
many_many = pd.merge(df_m, df_n, on="key")
print(many_many)
print(f"Left rows: {len(df_m)}, Right rows: {len(df_n)}, Merged rows: {len(many_many)}")

print("\n--- validate parameter ---")
unique_left = pd.DataFrame({"key": [1, 2, 3], "val": ["a", "b", "c"]})
unique_right = pd.DataFrame({"key": [1, 2, 3], "info": ["x", "y", "z"]})

valid = pd.merge(unique_left, unique_right, on="key", validate="one_to_one")
print("one_to_one validation passed:")
print(valid)

# Demonstrating validation failure
print("\n--- validate catches duplicates ---")
dup_right = pd.DataFrame({"key": [1, 1, 2], "info": ["x1", "x2", "y"]})
try:
    pd.merge(unique_left, dup_right, on="key", validate="one_to_one")
except pd.errors.MergeError as e:
    print(f"MergeError: {e}")
