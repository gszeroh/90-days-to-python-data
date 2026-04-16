# Day 27: Pandas — Data Transformation

Data transformation is at the heart of every analysis pipeline. Pandas provides a
rich set of methods — `apply`, `map`, `replace`, `rename`, and `assign` — that let
you reshape values, rename labels, and build readable method-chaining workflows
without mutating your original data.

---

## 1. apply() on Series and DataFrames

`apply()` runs a function along an axis of a DataFrame or element-wise on a Series.

### Series.apply()

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4])
s.apply(lambda x: x ** 2)
# 0     1
# 1     4
# 2     9
# 3    16
```

### DataFrame.apply()

By default `apply()` operates column-wise (`axis=0`). Pass `axis=1` to apply
row-wise.

```python
df = pd.DataFrame({"a": [1, 2], "b": [10, 20]})

df.apply(sum)          # column sums → Series
df.apply(sum, axis=1)  # row sums    → Series
```

> 💡 `apply()` is flexible but slower than vectorised operations. Prefer built-in
> methods (`.sum()`, `.mean()`) when they exist.

---

## 2. map() for Element-wise Transformation

`Series.map()` accepts a function, dictionary, or another Series and maps each
value to a new one.

```python
s = pd.Series(["cat", "dog", "cat", "bird"])
s.map({"cat": "feline", "dog": "canine", "bird": "avian"})
# 0    feline
# 1    canine
# 2    feline
# 3     avian
```

Unmapped values become `NaN` by default. Use `na_action="ignore"` to skip
`NaN` inputs.

```python
s.map(str.upper)
# 0     CAT
# 1     DOG
# 2     CAT
# 3    BIRD
```

---

## 3. applymap() / DataFrame.map()

For element-wise operations on an entire DataFrame, use `DataFrame.map()`
(Pandas ≥ 2.1) or the legacy `applymap()`.

```python
df = pd.DataFrame({"x": [1.111, 2.222], "y": [3.333, 4.444]})
df.map(lambda v: round(v, 1))
#      x    y
# 0  1.1  3.3
# 1  2.2  4.4
```

> ⚠️ `applymap()` is deprecated since Pandas 2.1. Prefer `DataFrame.map()`.

---

## 4. replace() for Value Substitution

`replace()` swaps specific values throughout a Series or DataFrame.

```python
s = pd.Series([1, 2, 3, 2, 1])
s.replace({1: 10, 2: 20})
# 0    10
# 1    20
# 2     3
# 3    20
# 4    10
```

You can also use lists or regex patterns:

```python
df = pd.DataFrame({"status": ["Y", "N", "Y", "N"]})
df.replace({"status": {"Y": True, "N": False}})
```

---

## 5. rename() for Columns and Index

`rename()` changes axis labels without touching the data.

```python
df = pd.DataFrame({"old_a": [1], "old_b": [2]})

# Dict mapping
df.rename(columns={"old_a": "new_a", "old_b": "new_b"})

# Function-based rename
df.rename(columns=str.upper)
```

Rename the index the same way:

```python
df.rename(index={0: "row_0"})
```

> 💡 Pass `inplace=True` to mutate the original DataFrame, but returning a new
> DataFrame is generally preferred for readability and safety.

---

## 6. assign() and Method Chaining

`assign()` adds or overwrites columns and returns a **new** DataFrame, making it
ideal for method chaining.

```python
df = pd.DataFrame({"price": [10, 20, 30], "qty": [5, 3, 7]})

result = (
    df
    .assign(total=lambda d: d["price"] * d["qty"])
    .assign(discounted=lambda d: d["total"] * 0.9)
    .rename(columns=str.upper)
)
```

Because each step returns a DataFrame, the entire pipeline reads top-to-bottom
and is easy to extend or debug.

---

## Key Takeaways

- **`apply()`** runs any function along rows or columns; use it when no
  vectorised alternative exists.
- **`Series.map()`** is the go-to for element-wise mapping with dicts,
  functions, or Series.
- **`DataFrame.map()`** (formerly `applymap()`) applies a function to every
  cell in the DataFrame.
- **`replace()`** swaps specific values by scalar, list, dict, or regex.
- **`rename()`** changes column or index labels with a dict or function.
- **`assign()`** creates derived columns and enables clean method chaining.

---

## Further Reading

- [pandas.DataFrame.apply](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)
- [pandas.Series.map](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)
- [pandas.DataFrame.map](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html)
- [pandas.DataFrame.replace](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html)
- [pandas.DataFrame.rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
- [pandas.DataFrame.assign](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html)
