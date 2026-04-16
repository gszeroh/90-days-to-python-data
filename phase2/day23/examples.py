"""Day 23: NumPy — Linear Algebra & Statistics — Examples"""

import numpy as np


# === Dot Product & Matrix Multiplication ===

print("--- Dot Product ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a          :", a)
print("b          :", b)
print("np.dot(a,b):", np.dot(a, b))

print("\n--- Matrix Multiplication (@) ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A:\n", A)
print("B:\n", B)
print("A @ B:\n", A @ B)
print("np.matmul(A, B):\n", np.matmul(A, B))


# === Matrix Operations ===

print("\n--- Transpose ---")
print("A.T:\n", A.T)

print("\n--- Inverse ---")
A_inv = np.linalg.inv(A)
print("inv(A):\n", A_inv)
print("A @ inv(A):\n", A @ A_inv)

print("\n--- Determinant ---")
print("det(A):", np.linalg.det(A))

print("\n--- Matrix Rank ---")
print("rank(A):", np.linalg.matrix_rank(A))


# === Solving Linear Systems ===

print("\n--- Solving Ax = b ---")
A_sys = np.array([[3, 1], [1, 2]])
b_sys = np.array([9, 8])
x = np.linalg.solve(A_sys, b_sys)
print("A:\n", A_sys)
print("b:", b_sys)
print("x:", x)
print("Verify A @ x:", A_sys @ x)


# === Eigenvalues & Eigenvectors ===

print("\n--- Eigenvalues & Eigenvectors ---")
M = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(M)
print("Matrix M:\n", M)
print("Eigenvalues :", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

print("\n--- Verify: M @ v == λ * v ---")
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    print(f"  λ={lam:.1f}  M@v={M @ v}  λ*v={lam * v}")


# === Statistical Functions ===

print("\n--- Basic Statistics ---")
data = np.array([14, 17, 12, 19, 11, 15, 18])
print("data      :", data)
print("mean      :", np.mean(data))
print("median    :", np.median(data))
print("std       :", np.std(data))
print("var       :", np.var(data))
print("min       :", np.min(data))
print("max       :", np.max(data))
print("percentile(25):", np.percentile(data, 25))
print("percentile(75):", np.percentile(data, 75))


# === Aggregation Along Axes ===

print("\n--- Aggregation Along Axes ---")
grid = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("grid:\n", grid)
print("mean (all)   :", np.mean(grid))
print("mean (axis=0):", np.mean(grid, axis=0))
print("mean (axis=1):", np.mean(grid, axis=1))
print("sum  (axis=0):", np.sum(grid, axis=0))
print("sum  (axis=1):", np.sum(grid, axis=1))
print("std  (axis=0):", np.std(grid, axis=0))
print("std  (axis=1):", np.std(grid, axis=1))
