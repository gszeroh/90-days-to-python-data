# Day 26: Pandas — Data Cleaning

## Overview

Real-world data is messy. Columns arrive with missing entries, duplicate rows,
inconsistent types, and untidy strings. **Pandas** provides a rich toolkit for
detecting and correcting these problems so your analysis starts from a solid
foundation. Today we cover the six most common cleaning operations you will
reach for on every project.

---

## 1. Detecting Missing Values

Pandas represents missing data as `NaN` (float) or `pd.NaT` (datetime).

| Method | Returns |
|---|---|
| `df.isnull()` / `df.isna()` | Boolean DataFrame — `True` where missing |
| `df.notnull()` / `df.notna()` | Boolean DataFrame — `True` where present |
| `df.isnull().sum()` | Count of missing values per column |
| `df.isnull().mean()` | Fraction of missing values per column |

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Alice", None, "Charlie"],
    "score": [90, np.nan, 85],
})

print(df.isnull())
#     name  score
# 0  False  False
# 1   True   True
# 2  False  False
```

💡 `isnull()` and `isna()` are aliases — use whichever reads better to you.

---

## 2. Handling Missing Values

Once detected, you can **drop** or **fill** missing values.

### Drop rows / columns

```python
df.dropna()                # drop rows with any NaN
df.dropna(how="all")       # drop rows where every value is NaN
df.dropna(subset=["score"])  # drop only when 'score' is NaN
```

### Fill with a constant, statistic, or method

```python
df["score"].fillna(0)                  # constant
df["score"].fillna(df["score"].mean()) # column mean
df["score"].interpolate()              # linear interpolation
```

⚠️ `fillna` and `interpolate` return new objects by default. Pass
`inplace=True` or reassign the result.

---

## 3. Removing Duplicates

```python
df.duplicated()              # Boolean Series — True for duplicate rows
df.duplicated(subset=["name"])  # check only the 'name' column
df.drop_duplicates()         # keep first occurrence by default
df.drop_duplicates(subset=["name"], keep="last")
```

| `keep` | Behaviour |
|---|---|
| `"first"` (default) | Keep the first occurrence |
| `"last"` | Keep the last occurrence |
| `False` | Drop **all** occurrences |

---

## 4. Type Conversion

Columns often arrive as `object` (string) when they should be numeric or
datetime.

```python
df["price"] = df["price"].astype(float)          # hard cast
df["price"] = pd.to_numeric(df["price"], errors="coerce")  # NaN on failure
df["date"]  = pd.to_datetime(df["date"])          # parse dates
```

| Function | Use case |
|---|---|
| `astype(dtype)` | When you are sure every value can convert |
| `pd.to_numeric(s, errors="coerce")` | Mixed data — bad values become `NaN` |
| `pd.to_datetime(s)` | Parse date strings into `Timestamp` |

💡 After `to_numeric` with `errors="coerce"`, always check for newly
introduced `NaN` values.

---

## 5. String Operations

The **`.str`** accessor exposes vectorized string methods on a Series.

```python
s = pd.Series(["  Alice ", "BOB", "charlie"])

s.str.lower()          # -> ["  alice ", "bob", "charlie"]
s.str.upper()          # -> ["  ALICE ", "BOB", "CHARLIE"]
s.str.strip()          # -> ["Alice", "BOB", "charlie"]
s.str.strip().str.lower()  # chain: ["alice", "bob", "charlie"]

s.str.contains("li")  # -> [True, False, False]
s.str.replace("li", "LI")  # -> ["  ALIce ", "BOB", "charLIe"]
```

### Extracting with regex

```python
emails = pd.Series(["alice@example.com", "bob@test.org"])
emails.str.extract(r"@(.+)\.")
#          0
# 0  example
# 1     test
```

---

## 6. Renaming & Replacing Values

### Rename columns

```python
df.rename(columns={"old_name": "new_name"})
df.columns = ["col_a", "col_b"]           # bulk rename
df.columns = df.columns.str.lower().str.replace(" ", "_")  # clean headers
```

### Replace values

```python
df["status"].replace({"Y": True, "N": False})
df.replace({-999: np.nan})                  # sentinel → NaN
```

💡 Combine renaming and replacing early in your pipeline so downstream code
works with clean, consistent names and values.

---

## Key Takeaways

| Concept | Go-to Method |
|---|---|
| Find missing data | `isnull()`, `notnull()` |
| Remove / fill gaps | `dropna()`, `fillna()`, `interpolate()` |
| Deduplicate | `duplicated()`, `drop_duplicates()` |
| Fix types | `astype()`, `to_numeric()`, `to_datetime()` |
| Clean strings | `.str.lower()`, `.str.strip()`, `.str.replace()` |
| Rename / remap | `rename()`, `replace()` |

---

## Further Reading

- [Pandas — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Pandas — Working with text data](https://pandas.pydata.org/docs/user_guide/text.html)
- [Pandas — Duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
- [Pandas — `to_numeric`](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)
- [Pandas — `to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
