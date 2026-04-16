# Day 28: Pandas — Grouping & Aggregation

## Overview

Grouping and aggregation are the backbone of exploratory data analysis.
Pandas implements the **split-apply-combine** pattern through `groupby()`,
giving you the power to slice a DataFrame into groups, apply a function to
each group independently, and then stitch the results back together.

Today you will learn how to summarise data with built-in and custom
aggregation functions, broadcast group-level statistics back to individual
rows with `transform()`, and reshape data with `pivot_table()` and
`crosstab()`.

---

## 1. GroupBy Basics

`DataFrame.groupby()` splits a DataFrame into groups based on one or more
columns and returns a `DataFrameGroupBy` object.

```python
import pandas as pd

df = pd.DataFrame({
    "dept": ["Sales", "Sales", "HR", "HR", "Engineering"],
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "salary": [70000, 80000, 65000, 72000, 95000],
})

grouped = df.groupby("dept")
print(type(grouped))        # <class 'pandas.core.groupby.DataFrameGroupBy'>
print(grouped.ngroups)       # 3
```

### Iterating Over Groups

```python
for name, group_df in grouped:
    print(name)
    print(group_df)
```

### Selecting a Column After Grouping

```python
grouped["salary"].mean()
```

---

## 2. Aggregation Functions

### Single Aggregation

```python
grouped["salary"].sum()
grouped["salary"].mean()
grouped["salary"].count()
```

### Multiple Aggregations with `agg()`

Pass a **list** to compute several statistics at once:

```python
grouped["salary"].agg(["mean", "min", "max", "std"])
```

Pass a **dict** to apply different functions to different columns:

```python
grouped.agg({"salary": ["mean", "sum"], "name": "count"})
```

### Custom Aggregation Functions

```python
grouped["salary"].agg(lambda x: x.max() - x.min())
```

---

## 3. Named Aggregation

`pd.NamedAgg` (or the keyword shorthand) makes output columns explicit and
avoids the multi-level column index:

```python
grouped.agg(
    avg_salary=pd.NamedAgg(column="salary", aggfunc="mean"),
    headcount=pd.NamedAgg(column="name", aggfunc="count"),
    max_salary=pd.NamedAgg(column="salary", aggfunc="max"),
)
```

The tuple shorthand is equivalent:

```python
grouped.agg(
    avg_salary=("salary", "mean"),
    headcount=("name", "count"),
    max_salary=("salary", "max"),
)
```

---

## 4. transform() — Broadcasting Group Results

`transform()` returns a Series the **same size** as the input, which makes
it perfect for adding group-level statistics back to each row.

```python
df["dept_mean"] = grouped["salary"].transform("mean")
```

### Group Z-Scores

```python
df["z_score"] = grouped["salary"].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

### Filtering with transform

```python
# Keep rows where the group mean salary exceeds 70 000
df[grouped["salary"].transform("mean") > 70000]
```

---

## 5. pivot_table()

`pivot_table()` creates a spreadsheet-style summary with one or more index
rows, columns, and aggregation functions.

```python
sales = pd.DataFrame({
    "region": ["East", "East", "West", "West", "East", "West"],
    "product": ["Widget", "Gadget", "Widget", "Gadget", "Widget", "Widget"],
    "revenue": [100, 200, 150, 250, 130, 170],
    "quantity": [10, 15, 12, 20, 11, 14],
})

sales.pivot_table(
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0,
)
```

| product | Gadget | Widget |
|---------|--------|--------|
| East    | 200    | 230    |
| West    | 250    | 320    |

### Multiple Aggregations

```python
sales.pivot_table(
    values="revenue",
    index="region",
    columns="product",
    aggfunc=["sum", "mean"],
    fill_value=0,
    margins=True,          # adds All row/column
)
```

---

## 6. crosstab()

`pd.crosstab()` computes a frequency table (and optionally other
aggregations) from two or more array-like objects.

```python
pd.crosstab(sales["region"], sales["product"])
```

### Normalised Cross-Tabulation

```python
pd.crosstab(
    sales["region"],
    sales["product"],
    normalize="index",     # row percentages
)
```

### Aggregated Cross-Tabulation

```python
pd.crosstab(
    sales["region"],
    sales["product"],
    values=sales["revenue"],
    aggfunc="mean",
)
```

---

## Key Takeaways

- **`groupby()`** implements split-apply-combine: split by key columns,
  apply a function, combine the results.
- **`agg()`** accepts strings, lists, dicts, or callables; **named
  aggregation** produces clean single-level column names.
- **`transform()`** broadcasts group results back to the original index —
  ideal for group z-scores, percentages, or filters.
- **`pivot_table()`** reshapes data into a spreadsheet-style summary with
  flexible row/column/value/aggregation settings.
- **`crosstab()`** is a convenience for frequency tables and quick
  cross-tabulations of categorical variables.

---

## Further Reading

- [pandas GroupBy documentation](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [pandas pivot_table documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html)
- [pandas crosstab documentation](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)
- [Real Python — Pandas GroupBy](https://realpython.com/pandas-groupby/)
