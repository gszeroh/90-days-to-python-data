"""Day 23: NumPy — Linear Algebra & Statistics — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import numpy as np


# === Exercise 1: Matrix Multiply ===

def matrix_multiply(A, B):
    """Return the matrix product of A and B.

    Use the @ operator or np.matmul to multiply two 2-D arrays.

    Args:
        A (np.ndarray): 2-D array of shape (m, n).
        B (np.ndarray): 2-D array of shape (n, p).

    Returns:
        np.ndarray: 2-D array of shape (m, p).

    Examples:
        matrix_multiply(np.array([[1, 2], [3, 4]]),
                        np.array([[5, 6], [7, 8]]))
        -> array([[19, 22], [43, 50]])
    """
    pass


# === Exercise 2: Solve Linear System ===

def solve_linear_system(A, b):
    """Solve the linear system Ax = b and return x.

    Use np.linalg.solve to find the solution vector.

    Args:
        A (np.ndarray): 2-D coefficient matrix of shape (n, n).
        b (np.ndarray): 1-D ordinate vector of length n.

    Returns:
        np.ndarray: 1-D solution vector of length n.

    Examples:
        solve_linear_system(np.array([[3, 1], [1, 2]]),
                            np.array([9, 8]))
        -> array([2., 3.])
    """
    pass


# === Exercise 3: Column Statistics ===

def column_statistics(arr):
    """Compute mean, standard deviation, and min for each column.

    Args:
        arr (np.ndarray): 2-D array of shape (m, n).

    Returns:
        tuple: Three 1-D arrays (means, stds, mins), each of length n.
            means — column-wise mean
            stds  — column-wise standard deviation
            mins  — column-wise minimum

    Examples:
        column_statistics(np.array([[1, 2], [3, 4], [5, 6]]))
        -> (array([3., 4.]), array([1.63299316, 1.63299316]), array([1, 2]))
    """
    pass


# === Exercise 4: Z-Score Normalisation ===

def zscore_normalize(arr):
    """Return the z-score normalised version of a 2-D array (per column).

    Each column should have mean ≈ 0 and std ≈ 1 after normalisation.
    Formula: z = (x - mean) / std, computed independently per column.

    Args:
        arr (np.ndarray): 2-D array of shape (m, n).

    Returns:
        np.ndarray: 2-D array of same shape with z-score normalised values.

    Examples:
        zscore_normalize(np.array([[1, 2], [3, 4], [5, 6]]))
        -> array([[-1.22474487, -1.22474487],
                  [ 0.        ,  0.        ],
                  [ 1.22474487,  1.22474487]])
    """
    pass


# === Exercise 5: Covariance Matrix ===

def covariance_matrix(arr):
    """Compute the covariance matrix for the columns of arr.

    Each column represents a variable and each row an observation.
    Use np.cov with rowvar=False so that columns are treated as variables.

    Args:
        arr (np.ndarray): 2-D array of shape (m, n) where m > 1.

    Returns:
        np.ndarray: 2-D covariance matrix of shape (n, n).

    Examples:
        covariance_matrix(np.array([[1, 2], [3, 4], [5, 6]]))
        -> array([[4., 4.], [4., 4.]])
    """
    pass
