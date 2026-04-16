"""
Day 21: NumPy — Arrays & Operations — Examples
"""

import numpy as np
import time

# === 1. What Is NumPy & Why It Matters ===

print("--- Why NumPy? ---")
py_list = [1, 2, 3, 4, 5]
np_arr = np.array([1, 2, 3, 4, 5])

# With a list you need a loop or comprehension:
doubled_list = [x * 2 for x in py_list]
print("List doubled:", doubled_list)

# With NumPy it's one expression:
doubled_arr = np_arr * 2
print("Array doubled:", doubled_arr)


# === 2. Creating Arrays ===

print("\n--- Creating Arrays ---")

# From Python sequences
a = np.array([1, 2, 3])
print("1-D array:", a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D array:\n", b)

c = np.array([1, 2, 3], dtype=float)
print("Explicit float dtype:", c)

# Filled arrays
print("\nzeros(2,3):\n", np.zeros((2, 3)))
print("ones(4):", np.ones(4))
print("full(2,2, 7):\n", np.full((2, 2), 7))

# Ranges
print("\narange(0,10,2):", np.arange(0, 10, 2))
print("linspace(0,1,5):", np.linspace(0, 1, 5))

# Random (modern Generator API)
rng = np.random.default_rng(seed=42)
print("\nRandom floats (2x3):\n", rng.random((2, 3)))
print("Random ints [0,10):", rng.integers(0, 10, size=5))
print("Normal samples:", rng.normal(0, 1, size=4))


# === 3. Array Attributes ===

print("\n--- Array Attributes ---")

arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Array:\n", arr)
print("shape:", arr.shape)
print("ndim:", arr.ndim)
print("dtype:", arr.dtype)
print("size:", arr.size)
print("itemsize:", arr.itemsize, "bytes")
print("nbytes:", arr.nbytes, "bytes")

# Changing dtype with astype
float_arr = arr.astype(np.float32)
print("\nAfter astype(float32):", float_arr.dtype, "->", float_arr)


# === 4. Reshaping Arrays ===

print("\n--- Reshaping ---")

flat = np.arange(12)
print("Original:", flat)

reshaped = flat.reshape(3, 4)
print("reshape(3,4):\n", reshaped)

inferred = flat.reshape(-1, 6)
print("reshape(-1,6):\n", inferred)

# Flattening
matrix = np.array([[1, 2], [3, 4]])
print("\nravel():", matrix.ravel())
print("flatten():", matrix.flatten())

# Transpose
m = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal shape:", m.shape)
print("Transposed shape:", m.T.shape)
print("Transposed:\n", m.T)

# View vs copy demonstration
view = flat.reshape(3, 4)
view[0, 0] = 999
print("\nAfter modifying view, original[0]:", flat[0])
flat[0] = 0  # reset


# === 5. Vectorized Operations ===

print("\n--- Vectorized Operations ---")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a ** 2:", a ** 2)

# Boolean comparisons
print("\na > 15:", a > 15)
print("a == 20:", a == 20)

# Universal functions
print("\nsqrt(a):", np.sqrt(a.astype(float)))
print("exp([1,2,3]):", np.exp(np.array([1, 2, 3])))
print("log([1, e, e^2]):", np.log(np.array([1, np.e, np.e**2])))

# Aggregations
grid = np.array([[1, 2], [3, 4]])
print("\nGrid:\n", grid)
print("sum():", grid.sum())
print("sum(axis=0) [col sums]:", grid.sum(axis=0))
print("sum(axis=1) [row sums]:", grid.sum(axis=1))
print("mean():", grid.mean())
print("std():", grid.std())
print("min(), max():", grid.min(), grid.max())


# === 6. Array vs List Performance ===

print("\n--- Performance Benchmark ---")

size = 1_000_000
py_list = list(range(size))
np_arr = np.arange(size)

start = time.perf_counter()
_ = [x * 2 for x in py_list]
list_time = time.perf_counter() - start

start = time.perf_counter()
_ = np_arr * 2
np_time = time.perf_counter() - start

print(f"List comprehension: {list_time:.4f}s")
print(f"NumPy vectorized:   {np_time:.4f}s")
print(f"Speed-up:           {list_time / np_time:.1f}x")
