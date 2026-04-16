"""Day 22: NumPy — Indexing & Broadcasting — Examples"""

import numpy as np

# === 1. Basic Indexing & Slicing ===

print("--- 1-D Slicing ---")
a = np.arange(10)
print("Array:", a)
print("a[2:7]  :", a[2:7])
print("a[::2]  :", a[::2])
print("a[-3:]  :", a[-3:])

print("\n--- 2-D Slicing ---")
m = np.arange(12).reshape(3, 4)
print("Matrix:\n", m)
print("Row 1        :", m[1, :])
print("Column 2     :", m[:, 2])
print("Sub-matrix:\n", m[0:2, 1:3])

print("\n--- Views vs Copies ---")
view = m[0, :]
view[0] = 99
print("After modifying view, original m[0, 0] =", m[0, 0])
m[0, 0] = 0  # restore

# === 2. Fancy Indexing ===

print("\n--- 1-D Fancy Indexing ---")
a = np.array([10, 20, 30, 40, 50])
idx = np.array([0, 3, 4])
print("a          :", a)
print("a[idx]     :", a[idx])

print("\n--- 2-D Fancy Indexing ---")
m = np.arange(12).reshape(3, 4)
rows = np.array([0, 1, 2])
cols = np.array([3, 2, 1])
print("Matrix:\n", m)
print("m[rows, cols]:", m[rows, cols])

print("\n--- Fancy Indexing Returns a Copy ---")
subset = a[idx]
subset[0] = -1
print("After modifying subset, original a[0] =", a[0])

# === 3. Boolean Indexing / Masks ===

print("\n--- Boolean Mask ---")
a = np.array([5, -3, 8, -1, 7])
mask = a > 0
print("a       :", a)
print("mask    :", mask)
print("a[mask] :", a[mask])

print("\n--- Combined Conditions ---")
nums = np.arange(20)
combined = nums[(nums > 5) & (nums < 15)]
print("nums where 5 < x < 15:", combined)

print("\n--- Setting Values with a Mask ---")
arr = np.array([1, -2, 3, -4, 5])
arr[arr < 0] = 0
print("Negatives clipped to 0:", arr)

# === 4. np.where ===

print("\n--- np.where with Replacement ---")
a = np.array([1, -2, 3, -4, 5])
result = np.where(a > 0, a, 0)
print("a      :", a)
print("result :", result)

print("\n--- np.where — Index-Only Form ---")
indices = np.where(a > 0)
print("Indices where a > 0:", indices[0])

print("\n--- np.where with Two Arrays ---")
x = np.array([10, 20, 30, 40])
y = np.array([1, 2, 3, 4])
cond = np.array([True, False, True, False])
print("np.where(cond, x, y):", np.where(cond, x, y))

# === 5. Broadcasting Rules ===

print("\n--- Rule 1: Shape Padding ---")
a = np.ones((3, 4))
b = np.arange(4)
print(f"a shape: {a.shape}, b shape: {b.shape}")
print(f"(a + b) shape: {(a + b).shape}")
print("a + b:\n", a + b)

print("\n--- Rule 2: Stretch Size-1 Dimensions ---")
col = np.array([[1], [2], [3]])
row = np.array([10, 20, 30, 40])
print(f"col shape: {col.shape}, row shape: {row.shape}")
print("col + row:\n", col + row)

print("\n--- Rule 3: Incompatible Shapes ---")
try:
    x = np.ones((3,))
    y = np.ones((4,))
    _ = x + y
except ValueError as e:
    print(f"ValueError: {e}")

# === 6. Broadcasting in Practice ===

print("\n--- Row-wise Normalisation (Zero Mean) ---")
np.random.seed(42)
data = np.random.randint(0, 100, size=(3, 5))
print("Original:\n", data)
means = data.mean(axis=1, keepdims=True)
centred = data - means
print("Row means after centring:", centred.mean(axis=1).round(10))

print("\n--- Outer Product via Broadcasting ---")
x = np.array([1, 2, 3])
y = np.array([10, 20])
outer = x[:, np.newaxis] * y
print("Outer product:\n", outer)

print("\n--- Distance Matrix via Broadcasting ---")
pts = np.array([0.0, 1.0, 3.0, 6.0])
diff = pts[:, np.newaxis] - pts[np.newaxis, :]
dist = np.abs(diff)
print("Points:", pts)
print("Distance matrix:\n", dist)
