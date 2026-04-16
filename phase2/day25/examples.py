"""
Day 25: Pandas — Data Loading & Inspection — Examples
"""

import pandas as pd
import numpy as np
from io import StringIO

# === 1. Reading CSV Files ===

csv_text = """\
name,age,city,salary
Alice,30,New York,70000
Bob,25,Los Angeles,60000
Charlie,35,Chicago,80000
Diana,28,New York,75000
Eve,32,Los Angeles,72000
"""

# Basic read
df = pd.read_csv(StringIO(csv_text))
print("Basic CSV read:")
print(df)
print()

# Using usecols to select specific columns
df_subset = pd.read_csv(StringIO(csv_text), usecols=["name", "salary"])
print("Only name and salary columns:")
print(df_subset)
print()

# Custom na_values and dtype
csv_with_missing = """\
id,name,score
1,Alice,95
2,Bob,N/A
3,Charlie,--
4,Diana,88
"""

df_missing = pd.read_csv(
    StringIO(csv_with_missing),
    na_values=["N/A", "--"],
    dtype={"id": str},
)
print("CSV with custom na_values and dtype:")
print(df_missing)
print(f"dtypes:\n{df_missing.dtypes}")
print()

# Parsing dates
csv_dates = """\
event,date,attendees
Launch,2024-01-15,200
Demo,2024-03-22,150
Release,2024-06-01,300
"""

df_dates = pd.read_csv(StringIO(csv_dates), parse_dates=["date"])
print("Parsed dates:")
print(df_dates.dtypes)
print()

# === 2. Reading Excel & JSON ===

# JSON from a string (in-memory)
json_text = '[{"fruit": "apple", "count": 5}, {"fruit": "banana", "count": 12}]'
df_json = pd.read_json(StringIO(json_text), orient="records")
print("DataFrame from JSON string:")
print(df_json)
print()

# Building a DataFrame from a list of dicts (equivalent to JSON records)
records = [
    {"product": "Widget", "price": 9.99, "stock": 150},
    {"product": "Gadget", "price": 24.99, "stock": 80},
    {"product": "Doohickey", "price": 4.99, "stock": 300},
]
df_records = pd.DataFrame(records)
print("DataFrame from list of dicts:")
print(df_records)
print()

# === 3. Quick Inspection (head, tail, shape, columns, dtypes) ===

print("head(3):")
print(df.head(3))
print()

print("tail(2):")
print(df.tail(2))
print()

print(f"shape: {df.shape}")
print(f"columns: {df.columns.tolist()}")
print(f"dtypes:\n{df.dtypes}")
print(f"index: {df.index.tolist()}")
print(f"len(df): {len(df)}")
print()

# === 4. Statistical Summary (describe, info) ===

print("describe() — numeric columns:")
print(df.describe())
print()

print("describe(include='all') — all columns:")
print(df.describe(include="all"))
print()

print("info():")
df.info()
print()

# === 5. Value Counts & Unique Values ===

print("value_counts() for city:")
print(df["city"].value_counts())
print()

print("Normalised value_counts():")
print(df["city"].value_counts(normalize=True))
print()

print(f"nunique() for city: {df['city'].nunique()}")
print(f"unique() for city: {df['city'].unique()}")
print()

# === 6. Memory Usage & Optimization ===

print("Memory usage (shallow):")
print(df.memory_usage())
print()

print("Memory usage (deep):")
print(df.memory_usage(deep=True))
print()

total_bytes = df.memory_usage(deep=True).sum()
print(f"Total deep memory: {total_bytes:,} bytes")
print()

# Optimise a string column with category dtype
df_opt = df.copy()
df_opt["city"] = df_opt["city"].astype("category")
print("After converting 'city' to category:")
print(f"  Before: {df['city'].memory_usage(deep=True):,} bytes")
print(f"  After:  {df_opt['city'].memory_usage(deep=True):,} bytes")
