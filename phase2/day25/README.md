# Day 25: Pandas — Data Loading & Inspection

## Overview

Before any analysis can begin you need to **load** data into a Pandas DataFrame
and **inspect** it to understand its shape, types, missing values, and statistical
properties. Today we cover the most common I/O functions (`read_csv`,
`read_excel`, `read_json`) and the essential inspection methods that should be
part of every exploratory workflow.

---

## 1. Reading CSV Files

`pd.read_csv()` is the workhorse for tabular data. Key parameters:

| Parameter | Purpose | Example |
|---|---|---|
| `filepath_or_buffer` | File path, URL, or file-like object | `"data.csv"` or `StringIO(text)` |
| `sep` / `delimiter` | Column separator (default `","`) | `sep="\t"` |
| `header` | Row number for column names | `header=0` |
| `names` | Explicit column names | `names=["a","b"]` |
| `index_col` | Column(s) to use as row index | `index_col=0` |
| `usecols` | Subset of columns to read | `usecols=["name","age"]` |
| `dtype` | Per-column data types | `dtype={"zip": str}` |
| `parse_dates` | Columns to parse as datetime | `parse_dates=["date"]` |
| `na_values` | Additional strings to treat as NaN | `na_values=["N/A","--"]` |
| `nrows` | Number of rows to read | `nrows=100` |
| `skiprows` | Rows to skip at the start | `skiprows=2` |
| `encoding` | File encoding | `encoding="utf-8"` |

```python
import pandas as pd
from io import StringIO

csv_text = "name,age,city\nAlice,30,NYC\nBob,25,LA"
df = pd.read_csv(StringIO(csv_text))
```

---

## 2. Reading Excel & JSON

### Excel

```python
df = pd.read_excel("report.xlsx", sheet_name="Q1")
```

Requires the `openpyxl` (`.xlsx`) or `xlrd` (`.xls`) engine.

### JSON

```python
# Record-oriented JSON
df = pd.read_json('data.json', orient='records')

# From a Python list of dicts
df = pd.DataFrame([{"a": 1, "b": 2}, {"a": 3, "b": 4}])
```

The `orient` parameter controls how keys map to rows/columns (`"records"`,
`"columns"`, `"index"`, `"split"`, `"values"`).

---

## 3. Quick Inspection (head, tail, shape, columns, dtypes)

After loading, run these immediately:

```python
df.head()        # first 5 rows
df.tail(3)       # last 3 rows
df.shape         # (rows, columns)
df.columns       # column labels
df.dtypes        # data type of each column
df.index         # row index
len(df)          # total number of rows
```

These calls are cheap and give you an instant picture of the data.

---

## 4. Statistical Summary (describe, info)

### `df.describe()`

Returns count, mean, std, min, 25%, 50%, 75%, max for numeric columns.
Pass `include="all"` to include non-numeric columns as well.

```python
df.describe()               # numeric only
df.describe(include="all")  # all dtypes
```

### `df.info()`

Prints a concise summary: column names, non-null counts, data types, and
memory usage.

```python
df.info()
df.info(memory_usage="deep")  # accurate memory including object dtypes
```

---

## 5. Value Counts & Unique Values

```python
df["city"].value_counts()             # frequency table (descending)
df["city"].value_counts(normalize=True)  # proportions
df["city"].nunique()                  # number of unique values
df["city"].unique()                   # array of unique values
```

`value_counts()` is invaluable for understanding categorical distributions
before grouping or encoding.

---

## 6. Memory Usage & Optimization

```python
df.memory_usage()                # bytes per column (shallow)
df.memory_usage(deep=True)       # includes object/string overhead
df.memory_usage(deep=True).sum() # total bytes
```

### Quick optimisation tips

| Technique | When to use |
|---|---|
| `df["col"].astype("category")` | Low-cardinality string columns |
| `pd.to_numeric(df["col"], downcast="integer")` | Integers that fit in `int8`/`int16` |
| `usecols` on read | Skip columns you don't need |
| `dtype` on read | Prevent upcasting at load time |

---

## Key Takeaways

- **`read_csv`** is highly configurable — learn its parameters to avoid
  post-load clean-up.
- Always inspect with **`head()`**, **`shape`**, **`dtypes`**, and **`info()`**
  before analysis.
- **`describe()`** gives a fast statistical overview; use `include="all"` for
  mixed-type DataFrames.
- **`value_counts()`** reveals categorical distributions instantly.
- Check **`memory_usage(deep=True)`** on large datasets to find optimisation
  opportunities.

---

## Further Reading

- [pandas I/O documentation](https://pandas.pydata.org/docs/user_guide/io.html)
- [pandas `read_csv` API reference](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [pandas `DataFrame.describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- [Enhancing performance — pandas docs](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)
