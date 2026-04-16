# Day 24: Pandas — Series & DataFrames

## Overview

Pandas is the cornerstone library for data manipulation in Python. It provides
two core data structures — **Series** (1-D labelled array) and **DataFrame**
(2-D labelled table) — that make loading, cleaning, and analysing tabular data
intuitive and fast. This lesson covers how to create these structures, select
data from them, and work with their data types.

---

## 1. What is Pandas & Why

Pandas builds on top of NumPy and adds:

- **Labelled axes** — rows and columns have names, not just integer positions.
- **Heterogeneous columns** — each column in a DataFrame can hold a different
  data type (int, float, string, datetime, …).
- **Rich I/O** — read and write CSV, Excel, SQL, JSON, Parquet, and more.
- **Missing-data handling** — first-class support for `NaN` / `None`.
- **GroupBy & aggregation** — split-apply-combine operations in one line.

```python
import pandas as pd
import numpy as np
```

💡 **Convention:** `pd` is the universally accepted alias for pandas.

---

## 2. Series — Creation, Indexing, Methods

A **Series** is a one-dimensional array with an associated index.

### Creating a Series

```python
# From a list (default integer index)
s = pd.Series([10, 20, 30, 40])

# From a list with a custom index
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# From a dictionary (keys become the index)
s = pd.Series({"x": 100, "y": 200, "z": 300})

# From a scalar (broadcasts to all index labels)
s = pd.Series(5, index=["a", "b", "c"])
```

### Indexing & Slicing

```python
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

s["b"]          # 20            — label-based
s[1]            # 20            — positional (if index is not int)
s["a":"c"]      # a=10, b=20, c=30 — label slice (inclusive!)
s[s > 15]       # boolean mask
```

### Useful Methods

| Method | Description |
|---|---|
| `s.values` | Underlying NumPy array |
| `s.index` | Index object |
| `s.dtype` | Data type |
| `s.head(n)` | First *n* elements |
| `s.describe()` | Summary statistics |
| `s.unique()` | Unique values |
| `s.value_counts()` | Frequency counts |
| `s.isnull()` | Boolean mask of missing values |
| `s.mean()`, `s.sum()` | Aggregations |

---

## 3. DataFrames — Creation from Dicts, Lists, NumPy

A **DataFrame** is a two-dimensional table where each column is a Series.

### From a Dictionary of Lists

```python
df = pd.DataFrame({
    "name":  ["Alice", "Bob", "Charlie"],
    "age":   [25, 30, 35],
    "score": [88.5, 92.0, 78.3],
})
```

### From a List of Dictionaries

```python
records = [
    {"name": "Alice", "age": 25},
    {"name": "Bob",   "age": 30},
]
df = pd.DataFrame(records)
```

### From a NumPy Array

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(arr, columns=["x", "y", "z"])
```

### Inspecting a DataFrame

| Attribute / Method | Description |
|---|---|
| `df.shape` | `(rows, cols)` tuple |
| `df.columns` | Column names |
| `df.index` | Row labels |
| `df.dtypes` | Data type of each column |
| `df.info()` | Concise summary |
| `df.head()` / `df.tail()` | First / last rows |
| `df.describe()` | Summary statistics |

---

## 4. Selecting Data — `[]`, `.loc[]`, `.iloc[]`

### Column Selection

```python
df["name"]            # Single column → Series
df[["name", "age"]]   # Multiple columns → DataFrame
```

### Row Selection with `.loc[]` (Label-Based)

```python
df.loc[0]                    # Row with label 0
df.loc[0:2]                  # Rows 0 through 2 (inclusive)
df.loc[0:2, "name"]          # Rows 0–2, column "name"
df.loc[:, ["name", "score"]] # All rows, selected columns
```

### Row Selection with `.iloc[]` (Integer Position)

```python
df.iloc[0]                # First row
df.iloc[0:2]              # First two rows (exclusive stop)
df.iloc[0:2, 0:2]         # First 2 rows, first 2 columns
df.iloc[:, -1]            # Last column
```

### Boolean Selection

```python
df[df["age"] > 28]                     # Filter rows
df.loc[df["score"] >= 90, "name"]      # Conditional column select
```

| Accessor | Lookup Style | Slice End |
|---|---|---|
| `[]` | Columns (or row slice) | Exclusive |
| `.loc[]` | Label-based | **Inclusive** |
| `.iloc[]` | Integer position | **Exclusive** |

---

## 5. Adding & Removing Columns

### Adding Columns

```python
# Direct assignment
df["passed"] = df["score"] >= 80

# Computed from existing columns
df["score_pct"] = df["score"] / 100

# With insert (specify position)
df.insert(1, "id", [101, 102, 103])
```

### Removing Columns

```python
df = df.drop(columns=["score_pct"])       # Returns new DataFrame
df.drop(columns=["passed"], inplace=True) # Modify in place
```

### Renaming Columns

```python
df = df.rename(columns={"name": "full_name"})
```

---

## 6. Data Types & Conversion (`astype`, `dtypes`)

Every column in a DataFrame has a **dtype** (data type). Pandas infers types on
creation, but you often need to convert them explicitly.

### Checking Types

```python
df.dtypes
# name     object
# age       int64
# score   float64
```

### Converting with `astype`

```python
df["age"] = df["age"].astype(float)          # int → float
df["score"] = df["score"].astype(int)        # float → int (truncates)
df["age_str"] = df["age"].astype(str)        # numeric → string
```

### Common Pandas dtypes

| dtype | Description |
|---|---|
| `int64` | 64-bit integer |
| `float64` | 64-bit float |
| `bool` | Boolean |
| `object` | Python objects (usually strings) |
| `category` | Categorical data |
| `datetime64[ns]` | Timestamps |

### Nullable Integer Types

```python
# Standard int64 cannot hold NaN; use nullable Int64
s = pd.array([1, 2, None], dtype="Int64")
```

---

## Key Takeaways

- **Series** is a labelled 1-D array; **DataFrame** is a labelled 2-D table.
- Create DataFrames from dicts, lists of records, or NumPy arrays.
- Use `.loc[]` for label-based selection and `.iloc[]` for integer-position
  selection — remember that `.loc` slices are **inclusive**.
- Add columns with direct assignment; remove with `df.drop(columns=[...])`.
- Always check `df.dtypes` and convert with `.astype()` when needed.

---

## Further Reading

- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas User Guide — Indexing](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
