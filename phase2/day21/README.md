# Day 21: NumPy — Arrays & Operations

## Overview

NumPy (Numerical Python) is the foundational library for scientific computing
in Python. It introduces the **ndarray**, a fast, memory-efficient
multi-dimensional array that supports vectorized operations — replacing slow
Python loops with optimized C-level computation.

---

## 1. What Is NumPy & Why It Matters

Python lists are flexible but **slow** for numerical work because every element
is a full Python object. NumPy solves this by storing data in contiguous blocks
of memory with a single, fixed data type.

| Feature | Python List | NumPy ndarray |
|---|---|---|
| Element types | Mixed | Homogeneous |
| Memory layout | Scattered pointers | Contiguous block |
| Math operations | Manual loops | Vectorized (C-level) |
| Speed (large data) | Slow | 10–100× faster |

```python
import numpy as np

nums = np.array([1, 2, 3, 4, 5])
print(nums * 2)  # array([ 2,  4,  6,  8, 10])
```

> 💡 Convention: `import numpy as np` is universally used in the data-science
> community — always follow it.

---

## 2. Creating Arrays

NumPy provides many factory functions for array creation:

### From an existing sequence

```python
a = np.array([1, 2, 3])              # 1-D from list
b = np.array([[1, 2], [3, 4]])       # 2-D from nested lists
c = np.array([1, 2, 3], dtype=float) # explicit dtype
```

### Filled arrays

```python
np.zeros((2, 3))       # 2×3 array of 0.0
np.ones((3,))          # 1-D array of 1.0
np.full((2, 2), 7)     # 2×2 array filled with 7
np.empty((2, 3))       # uninitialized (fast, but values are garbage)
```

### Ranges and sequences

```python
np.arange(0, 10, 2)        # array([0, 2, 4, 6, 8])  — like range()
np.linspace(0, 1, 5)       # array([0. , 0.25, 0.5, 0.75, 1. ]) — N evenly spaced
```

### Random arrays

```python
rng = np.random.default_rng(seed=42)
rng.random((2, 3))         # 2×3 of uniform floats in [0, 1)
rng.integers(0, 10, (3,))  # 3 random ints in [0, 10)
rng.normal(0, 1, (4,))     # 4 samples from standard normal
```

> ⚠️ Prefer `np.random.default_rng()` over the legacy `np.random.rand` /
> `np.random.randn` functions — the new Generator API is faster and more
> statistically robust.

---

## 3. Array Attributes

Every ndarray carries metadata you can inspect:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape      # (2, 3) — rows × cols
a.ndim       # 2      — number of dimensions
a.dtype      # dtype('int64') — element type
a.size       # 6      — total element count
a.itemsize   # 8      — bytes per element
a.nbytes     # 48     — total bytes (size × itemsize)
```

### Common dtypes

| dtype | Description |
|---|---|
| `np.int32`, `np.int64` | Signed integers |
| `np.float32`, `np.float64` | Floating point |
| `np.bool_` | Boolean |
| `np.complex128` | Complex numbers |
| `np.str_` | Fixed-length strings |

You can convert between types with `.astype()`:

```python
a = np.array([1, 2, 3])
a_float = a.astype(np.float64)   # array([1., 2., 3.])
```

---

## 4. Reshaping Arrays

Reshaping changes the **view** of data without copying it (when possible).

```python
a = np.arange(12)               # array([ 0,  1,  2, ..., 11])

b = a.reshape(3, 4)             # 3×4 matrix — same data
c = a.reshape(2, 2, 3)          # 2×2×3 tensor

a.reshape(-1, 4)                # -1 = "infer this dimension" → (3, 4)
```

### Flattening

```python
b = np.array([[1, 2], [3, 4]])

b.ravel()       # array([1, 2, 3, 4]) — returns a view (when possible)
b.flatten()     # array([1, 2, 3, 4]) — always returns a copy
```

### Transpose

```python
m = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2, 3)
m.T                                      # shape (3, 2)
```

> 💡 `reshape` returns a **view** — modifying the reshaped array also modifies
> the original. Use `.copy()` if you need independence.

---

## 5. Vectorized Operations

Vectorized operations apply an operation to **every element** without writing a
Python loop.

### Element-wise arithmetic

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

a + b     # array([11, 22, 33])
a - b     # array([ 9, 18, 27])
a * b     # array([ 10,  40,  90])
a / b     # array([10., 10., 10.])
a ** 2    # array([100, 400, 900])
a % 4     # array([2, 0, 2])
```

### Comparison (returns boolean array)

```python
a > 15    # array([False,  True,  True])
a == 20   # array([False,  True, False])
```

### Universal functions (ufuncs)

NumPy ships optimized C implementations of common math:

```python
np.sqrt(a)        # array([3.162..., 4.472..., 5.477...])
np.exp(a)         # element-wise e^x
np.log(a)         # natural log
np.sin(a)         # trigonometric
np.abs(a)         # absolute value
```

### Aggregations

```python
a = np.array([[1, 2], [3, 4]])

a.sum()           # 10 — total
a.sum(axis=0)     # array([4, 6]) — column sums
a.sum(axis=1)     # array([3, 7]) — row sums
a.mean()          # 2.5
a.std()           # 1.118...
a.min(), a.max()  # (1, 4)
```

---

## 6. Array vs List Performance

A quick benchmark shows why NumPy matters for numeric work:

```python
import time

size = 1_000_000
py_list = list(range(size))
np_arr  = np.arange(size)

# Python list comprehension
start = time.perf_counter()
result_list = [x * 2 for x in py_list]
list_time = time.perf_counter() - start

# NumPy vectorized
start = time.perf_counter()
result_np = np_arr * 2
np_time = time.perf_counter() - start

print(f"List: {list_time:.4f}s | NumPy: {np_time:.4f}s")
# Typical output — NumPy is 20–100× faster
```

The speed-up comes from:

1. **No per-element type checking** — dtype is fixed.
2. **Contiguous memory** — better CPU cache utilisation.
3. **C-level loops** — bypasses the Python interpreter.

---

## Key Takeaways

- NumPy's `ndarray` stores homogeneous data in contiguous memory, making it
  far faster than Python lists for numerical work.
- Use factory functions (`zeros`, `ones`, `arange`, `linspace`,
  `default_rng`) to create arrays efficiently.
- Every array carries metadata: `shape`, `ndim`, `dtype`, `size`.
- `reshape` returns a view (no copy); `flatten` always copies.
- Vectorized operations and ufuncs replace explicit Python loops with
  optimized C code.
- Always `import numpy as np` — it is the universal convention.

---

## Further Reading

- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Array Creation Routines](https://numpy.org/doc/stable/reference/routines.array-creation.html)
- [Universal Functions (ufuncs)](https://numpy.org/doc/stable/reference/ufuncs.html)
- [NumPy Random Generator](https://numpy.org/doc/stable/reference/random/generator.html)
