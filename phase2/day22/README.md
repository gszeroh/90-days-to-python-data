# Day 22: NumPy — Indexing & Broadcasting

## Overview

NumPy's power goes far beyond basic element access. **Fancy indexing** lets you
select arbitrary elements with integer arrays, **boolean masks** filter data by
condition, and **broadcasting** eliminates the need for explicit loops when
combining arrays of different shapes. Mastering these three ideas is the key to
writing fast, readable numerical code.

---

## 1. Basic Indexing & Slicing

NumPy supports the familiar Python slice syntax for both one-dimensional and
multi-dimensional arrays.

### 1-D Slicing

```python
import numpy as np

a = np.arange(10)          # [0, 1, 2, ..., 9]
print(a[2:7])              # [2 3 4 5 6]
print(a[::2])              # [0 2 4 6 8]  — every other element
```

### 2-D Slicing

```python
m = np.arange(12).reshape(3, 4)
print(m[1, :])             # entire second row
print(m[:, 2])             # entire third column
print(m[0:2, 1:3])         # 2×2 sub-matrix
```

> 💡 Basic slicing returns a **view** — modifications affect the original array.

---

## 2. Fancy Indexing

Fancy (or *advanced*) indexing uses **integer arrays** to pick elements at
arbitrary positions.

```python
a = np.array([10, 20, 30, 40, 50])
idx = np.array([0, 3, 4])
print(a[idx])              # [10 40 50]
```

For 2-D arrays, pass separate row and column index arrays:

```python
m = np.arange(12).reshape(3, 4)
rows = np.array([0, 1, 2])
cols = np.array([3, 2, 1])
print(m[rows, cols])       # [ 3  6  9]
```

> ⚠️ Fancy indexing always returns a **copy**, not a view.

---

## 3. Boolean Indexing / Masks

A comparison on an array produces a boolean array that can be used as a mask:

```python
a = np.array([5, -3, 8, -1, 7])
mask = a > 0
print(mask)                # [ True False  True False  True]
print(a[mask])             # [5 8 7]
```

Combine conditions with `&` (and), `|` (or), `~` (not):

```python
a = np.arange(20)
print(a[(a > 5) & (a < 15)])   # [ 6  7  8  9 10 11 12 13 14]
```

> 💡 Boolean indexing also returns a **copy**.

---

## 4. np.where

`np.where(condition, x, y)` returns elements from `x` where the condition is
`True`, and from `y` otherwise — like a vectorised *if/else*:

```python
a = np.array([1, -2, 3, -4, 5])
result = np.where(a > 0, a, 0)
print(result)              # [1 0 3 0 5]
```

Called with only a condition, `np.where` returns the **indices** where the
condition is `True`:

```python
idx = np.where(a > 0)
print(idx)                 # (array([0, 2, 4]),)
```

---

## 5. Broadcasting Rules

Broadcasting lets NumPy perform element-wise operations on arrays with
**different shapes** without copying data.

NumPy compares shapes element-wise, starting from the **trailing** dimensions:

| Rule | Description |
|------|-------------|
| **Rule 1** | If the arrays differ in number of dimensions, the shape of the smaller array is padded with 1s on the **left**. |
| **Rule 2** | Arrays with a size of 1 along a particular dimension act as if they had the size of the largest array in that dimension. |
| **Rule 3** | If sizes disagree and neither is 1, a `ValueError` is raised. |

### Example Walk-Through

```python
a = np.ones((3, 4))       # shape (3, 4)
b = np.arange(4)           # shape (4,)

# Step 1 — Rule 1: pad b → shape (1, 4)
# Step 2 — Rule 2: stretch b → shape (3, 4)
# Result: element-wise addition works
print((a + b).shape)       # (3, 4)
```

---

## 6. Broadcasting in Practice

### Adding a Column Vector to Every Column

```python
m = np.zeros((3, 4))
col = np.array([[1], [2], [3]])   # shape (3, 1)
print(m + col)
# [[1. 1. 1. 1.]
#  [2. 2. 2. 2.]
#  [3. 3. 3. 3.]]
```

### Outer Product via Broadcasting

```python
x = np.array([1, 2, 3])
y = np.array([10, 20])
outer = x[:, np.newaxis] * y      # (3,1) * (2,) → (3,2)
print(outer)
# [[10 20]
#  [20 40]
#  [30 60]]
```

### Normalising Rows to Zero Mean

```python
data = np.random.rand(4, 5)
centred = data - data.mean(axis=1, keepdims=True)
print(centred.mean(axis=1))        # ~[0, 0, 0, 0]
```

> 💡 Use `keepdims=True` so the result retains the right shape for
> broadcasting.

---

## Key Takeaways

- **Basic slicing** returns a view; **fancy** and **boolean** indexing return
  copies.
- Fancy indexing with integer arrays selects elements at arbitrary positions.
- Boolean masks are the idiomatic way to filter array data by condition.
- `np.where(cond, x, y)` is a vectorised *if/else* — avoid Python loops.
- Broadcasting aligns shapes from the right and stretches dimensions of size 1.
- Use `keepdims=True` when reducing an axis to preserve broadcastable shapes.

---

## Further Reading

- [NumPy — Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)
- [NumPy — Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [NumPy — np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
- [Jake VanderPlas — Fancy Indexing (PythonDataScienceHandbook)](https://jakevdp.github.io/PythonDataScienceHandbook/02.07-fancy-indexing.html)
