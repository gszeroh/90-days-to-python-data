# Day 29: Pandas — Merging & Joining

## Overview

Real-world analysis rarely lives inside a single table. You will frequently
need to **combine** datasets — appending rows, matching on shared keys, or
aligning on an index. Pandas provides four core tools for this:

| Tool | Purpose |
|------|---------|
| `pd.concat()` | Stack DataFrames vertically or horizontally |
| `pd.merge()` | SQL-style joins on column keys |
| `DataFrame.join()` | Index-based joining (shorthand for merge) |
| Merge indicator | Diagnose which rows matched via `_merge` column |

Mastering these operations is essential for data preparation, ETL pipelines,
and any workflow that pulls data from multiple sources.

---

## 1. pd.concat() — Stacking DataFrames

`pd.concat()` glues DataFrames together along an axis.

### Vertical Stacking (axis=0)

```python
import pandas as pd

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

result = pd.concat([df1, df2], ignore_index=True)
```

- `ignore_index=True` resets the index to 0, 1, 2, …
- Without it, the original indices are preserved (possibly duplicated).

### Horizontal Stacking (axis=1)

```python
pd.concat([df1, df2], axis=1)
```

### Adding Source Keys

```python
pd.concat([df1, df2], keys=["first", "second"])
```

This creates a hierarchical (MultiIndex) so you can trace each row back to
its source DataFrame.

> 💡 **Tip:** `pd.concat()` is the recommended replacement for the deprecated
> `DataFrame.append()` method.

---

## 2. pd.merge() — SQL-style Joins (inner, left, right, outer)

`pd.merge()` performs relational joins similar to SQL.

```python
orders = pd.DataFrame({"order_id": [1, 2, 3], "customer_id": [10, 20, 30]})
customers = pd.DataFrame({"customer_id": [10, 20, 40], "name": ["Alice", "Bob", "Diana"]})

# Inner join (default) — only matching keys
pd.merge(orders, customers, on="customer_id")

# Left join — keep all rows from the left DataFrame
pd.merge(orders, customers, on="customer_id", how="left")

# Right join — keep all rows from the right DataFrame
pd.merge(orders, customers, on="customer_id", how="right")

# Outer join — keep all rows from both
pd.merge(orders, customers, on="customer_id", how="outer")
```

| `how` | SQL Equivalent | Keeps |
|-------|----------------|-------|
| `"inner"` | INNER JOIN | Only matching keys |
| `"left"` | LEFT OUTER JOIN | All left + matching right |
| `"right"` | RIGHT OUTER JOIN | All right + matching left |
| `"outer"` | FULL OUTER JOIN | All keys from both sides |

---

## 3. Merge on Multiple Keys & Suffixes

### Multiple Keys

When two DataFrames share more than one key column, pass a list:

```python
pd.merge(df_a, df_b, on=["year", "quarter"])
```

### Different Column Names

If the key columns have different names, use `left_on` / `right_on`:

```python
pd.merge(df_a, df_b, left_on="emp_id", right_on="employee_id")
```

### Controlling Suffixes

When both DataFrames have overlapping non-key columns, Pandas appends
`_x` / `_y` by default. Customize with `suffixes`:

```python
pd.merge(df_a, df_b, on="id", suffixes=("_left", "_right"))
```

---

## 4. .join() — Index-based Joining

`DataFrame.join()` is a convenience wrapper around `pd.merge()` that
joins on the **index** by default:

```python
df_left = pd.DataFrame({"salary": [70_000, 80_000]}, index=["Alice", "Bob"])
df_right = pd.DataFrame({"dept": ["Eng", "Sales"]}, index=["Alice", "Bob"])

df_left.join(df_right)
```

- Uses the calling DataFrame's index and the other DataFrame's index.
- Accepts `how` (`"left"`, `"right"`, `"inner"`, `"outer"`).
- Use `on=` to join the caller's **column** to the other's **index**.

> ⚠️ **Warning:** `.join()` defaults to a **left join**, while `pd.merge()`
> defaults to an **inner join**.

---

## 5. Merge Indicator (_merge column)

Adding `indicator=True` to `pd.merge()` creates a `_merge` column that tells
you where each row came from:

```python
pd.merge(orders, customers, on="customer_id", how="outer", indicator=True)
```

| `_merge` value | Meaning |
|----------------|---------|
| `"both"` | Key found in both DataFrames |
| `"left_only"` | Key found only in the left DataFrame |
| `"right_only"` | Key found only in the right DataFrame |

This is invaluable for **data quality checks** — quickly find unmatched
records after a join.

---

## 6. Handling Duplicates & Validation

### Duplicate Keys

If a key appears multiple times in **both** DataFrames, the merge produces a
Cartesian product of those rows (many-to-many). This can silently explode
your row count.

### The `validate` Parameter

Use `validate` to enforce expected key relationships:

```python
pd.merge(df_a, df_b, on="id", validate="one_to_one")   # 1:1
pd.merge(df_a, df_b, on="id", validate="one_to_many")   # 1:N
pd.merge(df_a, df_b, on="id", validate="many_to_one")   # N:1
```

A `MergeError` is raised if the relationship is violated, helping you catch
data issues early.

> 💡 **Tip:** Always inspect `.shape` and use `indicator=True` after a merge
> to verify the result is what you expect.

---

## Key Takeaways

- **`pd.concat()`** stacks DataFrames vertically (or horizontally) and is the
  go-to for appending rows.
- **`pd.merge()`** performs SQL-style joins with `how` controlling the join
  type (`inner`, `left`, `right`, `outer`).
- Use **`left_on` / `right_on`** when key column names differ, and
  **`suffixes`** to disambiguate overlapping columns.
- **`.join()`** is a shorthand for index-based merges; remember it defaults
  to a **left** join.
- **`indicator=True`** adds a `_merge` column for easy diagnostics.
- **`validate`** guards against unexpected many-to-many explosions.

---

## Further Reading

- [pandas.concat — pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
- [pandas.merge — pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
- [pandas.DataFrame.join — pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)
- [Merge, join, concatenate — pandas User Guide](https://pandas.pydata.org/docs/user_guide/merging.html)
