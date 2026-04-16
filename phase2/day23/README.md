# Day 23: NumPy — Linear Algebra & Statistics

## Overview

NumPy ships with a powerful **linear algebra** sub-module (`numpy.linalg`) and a
rich set of **statistical functions** that operate on arrays. Together they let
you solve systems of equations, decompose matrices, and summarise data — all in
a few lines of vectorised code.

---

## 1. Dot Product & Matrix Multiplication

The **dot product** of two 1-D arrays returns a scalar. For 2-D arrays the
operation becomes standard **matrix multiplication**.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Dot product (scalar)
np.dot(a, b)        # 32

# Matrix multiplication with @ operator
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A @ B                # array([[19, 22], [43, 50]])
np.matmul(A, B)      # same result
```

💡 **Tip:** Prefer the `@` operator — it is concise and reads naturally in
mathematical expressions.

---

## 2. Matrix Operations

Common matrix manipulations are available as array methods or `numpy.linalg`
functions.

```python
A = np.array([[1, 2], [3, 4]])

# Transpose
A.T                          # array([[1, 3], [2, 4]])

# Inverse
np.linalg.inv(A)             # array([[-2. ,  1. ], [ 1.5, -0.5]])

# Determinant
np.linalg.det(A)             # -2.0

# Matrix rank
np.linalg.matrix_rank(A)     # 2
```

⚠️ **Warning:** Inverting a singular matrix raises `LinAlgError`. Always check
the determinant or use `np.linalg.pinv` for pseudo-inverse.

---

## 3. Solving Linear Systems

Given **Ax = b**, you can solve for **x** directly:

```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = np.linalg.solve(A, b)    # array([2., 3.])
```

This is numerically more stable and faster than computing `inv(A) @ b`.

---

## 4. Eigenvalues & Eigenvectors

Eigendecomposition is central to PCA, vibration analysis, and many other
applications.

```python
A = np.array([[4, -2], [1,  1]])

eigenvalues, eigenvectors = np.linalg.eig(A)
# eigenvalues  : array([3., 2.])
# eigenvectors : columns of the returned matrix
```

| Function | Description |
|---|---|
| `np.linalg.eig` | Eigenvalues & right eigenvectors |
| `np.linalg.eigh` | For symmetric / Hermitian matrices (faster) |
| `np.linalg.eigvals` | Eigenvalues only |

---

## 5. Statistical Functions

NumPy provides a complete toolkit for descriptive statistics.

```python
data = np.array([14, 17, 12, 19, 11, 15, 18])

np.mean(data)          # 15.142857...
np.median(data)        # 15.0
np.std(data)           # 2.734...
np.var(data)           # 7.469...
np.min(data)           # 11
np.max(data)           # 19
np.percentile(data, 75)  # 17.5
```

---

## 6. Aggregation Along Axes

Statistical functions accept an **`axis`** parameter so you can aggregate across
rows or columns of a 2-D array.

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])

np.mean(A, axis=0)   # column means → array([2.5, 3.5, 4.5])
np.mean(A, axis=1)   # row means    → array([2., 5.])
np.sum(A, axis=0)    # column sums  → array([5, 7, 9])
```

| `axis` Value | Meaning |
|---|---|
| `None` (default) | Flatten, then aggregate |
| `0` | Aggregate **down** each column |
| `1` | Aggregate **across** each row |

---

## Key Takeaways

- Use `@` or `np.dot` for matrix multiplication; choose `@` for readability.
- `np.linalg.solve` is the preferred way to solve **Ax = b** — avoid explicit
  inversion when possible.
- Eigendecomposition with `np.linalg.eig` underpins many data-science methods.
- Statistical helpers like `mean`, `std`, and `percentile` accept an `axis`
  argument for flexible aggregation.

---

## Further Reading

- [NumPy Linear Algebra Docs](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [NumPy Statistics Docs](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [Khan Academy — Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
