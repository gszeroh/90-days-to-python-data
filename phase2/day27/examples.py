"""
Day 27: Pandas — Data Transformation — Examples
"""

import pandas as pd
import numpy as np

# === 1. apply() on Series and DataFrames ===

print("\n--- Series.apply() ---")
s = pd.Series([1, 2, 3, 4], name="values")
squared = s.apply(lambda x: x ** 2)
print("Original:\n", s.to_list())
print("Squared via apply:\n", squared.to_list())

print("\n--- DataFrame.apply() column-wise ---")
df = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
print("DataFrame:\n", df)
print("Column sums (axis=0):\n", df.apply(sum))

print("\n--- DataFrame.apply() row-wise ---")
print("Row sums (axis=1):\n", df.apply(sum, axis=1))

print("\n--- apply() with a custom function ---")


def label_size(val):
    """Return a size label based on a numeric value."""
    if val < 10:
        return "small"
    elif val < 25:
        return "medium"
    return "large"


print("Size labels for column b:", df["b"].apply(label_size).to_list())

# === 2. map() for Element-wise Transformation ===

print("\n--- map() with a dictionary ---")
animals = pd.Series(["cat", "dog", "cat", "bird"])
mapping = {"cat": "feline", "dog": "canine", "bird": "avian"}
print("Mapped:", animals.map(mapping).to_list())

print("\n--- map() with a function ---")
print("Upper-cased:", animals.map(str.upper).to_list())

print("\n--- map() unmapped values become NaN ---")
partial = {"cat": "feline", "dog": "canine"}
print("Partial map:", animals.map(partial).to_list())

# === 3. applymap() / DataFrame.map() ===

print("\n--- DataFrame.map() element-wise ---")
df_float = pd.DataFrame({"x": [1.111, 2.222], "y": [3.333, 4.444]})
rounded = df_float.map(lambda v: round(v, 1))
print("Original:\n", df_float)
print("Rounded:\n", rounded)

print("\n--- DataFrame.map() with formatting ---")
formatted = df_float.map(lambda v: f"{v:.2f}")
print("Formatted as strings:\n", formatted)

# === 4. replace() for Value Substitution ===

print("\n--- replace() with a dictionary ---")
s_nums = pd.Series([1, 2, 3, 2, 1])
replaced = s_nums.replace({1: 10, 2: 20})
print("Before:", s_nums.to_list())
print("After: ", replaced.to_list())

print("\n--- replace() on a DataFrame ---")
df_status = pd.DataFrame({"status": ["Y", "N", "Y", "N"], "score": [80, 90, 70, 85]})
df_replaced = df_status.replace({"status": {"Y": True, "N": False}})
print("Original:\n", df_status)
print("Replaced:\n", df_replaced)

print("\n--- replace() with regex ---")
s_text = pd.Series(["foo_1", "bar_2", "baz_3"])
cleaned = s_text.replace(r"_\d+", "", regex=True)
print("Regex replace:", cleaned.to_list())

# === 5. rename() for Columns and Index ===

print("\n--- rename() columns with a dict ---")
df_rename = pd.DataFrame({"old_a": [1, 2], "old_b": [3, 4]})
renamed = df_rename.rename(columns={"old_a": "new_a", "old_b": "new_b"})
print("Before:", df_rename.columns.to_list())
print("After: ", renamed.columns.to_list())

print("\n--- rename() columns with a function ---")
upper_cols = df_rename.rename(columns=str.upper)
print("Upper-cased columns:", upper_cols.columns.to_list())

print("\n--- rename() the index ---")
idx_renamed = df_rename.rename(index={0: "row_0", 1: "row_1"})
print("Renamed index:", idx_renamed.index.to_list())

# === 6. assign() and Method Chaining ===

print("\n--- assign() to add computed columns ---")
df_sales = pd.DataFrame({"price": [10, 20, 30], "qty": [5, 3, 7]})
df_total = df_sales.assign(total=lambda d: d["price"] * d["qty"])
print(df_total)

print("\n--- Method chaining with assign + rename ---")
result = (
    df_sales
    .assign(total=lambda d: d["price"] * d["qty"])
    .assign(discounted=lambda d: d["total"] * 0.9)
    .rename(columns=str.upper)
)
print(result)

print("\n--- Chaining assign, map, and rename ---")
df_grades = pd.DataFrame({"name": ["Alice", "Bob", "Carol"], "score": [92, 67, 85]})

pipeline_result = (
    df_grades
    .assign(letter=lambda d: d["score"].map(
        lambda x: "A" if x >= 90 else "B" if x >= 80 else "C" if x >= 70 else "D"
    ))
    .assign(passed=lambda d: d["score"] >= 70)
    .rename(columns=str.upper)
)
print(pipeline_result)
