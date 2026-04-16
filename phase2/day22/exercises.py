"""Day 22: NumPy — Indexing & Broadcasting — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import numpy as np


# === Exercise 1: Extract a Sub-array with Slicing ===

def extract_subarray(arr, row_start, row_end, col_start, col_end):
    """Return a sub-array from a 2-D array using slicing.

    The slice includes ``row_start`` up to (but not including) ``row_end``
    and ``col_start`` up to (but not including) ``col_end``.

    Args:
        arr (np.ndarray): 2-D input array.
        row_start (int): Starting row index (inclusive).
        row_end (int): Ending row index (exclusive).
        col_start (int): Starting column index (inclusive).
        col_end (int): Ending column index (exclusive).

    Returns:
        np.ndarray: The sliced sub-array.

    Examples:
        extract_subarray(np.arange(20).reshape(4, 5), 1, 3, 2, 5)
        -> array([[ 7,  8,  9],
                  [12, 13, 14]])

        extract_subarray(np.arange(9).reshape(3, 3), 0, 2, 0, 2)
        -> array([[0, 1],
                  [3, 4]])
    """
    pass


# === Exercise 2: Filter with a Boolean Mask ===

def filter_between(arr, low, high):
    """Return elements of *arr* that are strictly between *low* and *high*.

    Args:
        arr (np.ndarray): 1-D input array of numbers.
        low (float): Lower bound (exclusive).
        high (float): Upper bound (exclusive).

    Returns:
        np.ndarray: 1-D array of elements satisfying low < x < high.

    Examples:
        filter_between(np.array([1, 5, 10, 15, 20]), 4, 16)
        -> array([ 5, 10, 15])

        filter_between(np.array([-3, 0, 3, 6, 9]), 0, 7)
        -> array([3, 6])
    """
    pass


# === Exercise 3: Fancy Index Selection ===

def select_by_indices(arr, row_idx, col_idx):
    """Use fancy indexing to select elements from a 2-D array.

    For each pair ``(row_idx[i], col_idx[i])``, return the corresponding
    element from *arr*.

    Args:
        arr (np.ndarray): 2-D input array.
        row_idx (np.ndarray): 1-D array of row indices.
        col_idx (np.ndarray): 1-D array of column indices.

    Returns:
        np.ndarray: 1-D array of selected elements.

    Examples:
        m = np.arange(12).reshape(3, 4)
        select_by_indices(m, np.array([0, 1, 2]), np.array([3, 2, 1]))
        -> array([3, 6, 9])

        m = np.arange(9).reshape(3, 3)
        select_by_indices(m, np.array([0, 2]), np.array([0, 2]))
        -> array([0, 8])
    """
    pass


# === Exercise 4: Replace Negatives with np.where ===

def replace_negatives(arr, replacement=0):
    """Replace all negative values in *arr* with *replacement* using np.where.

    Args:
        arr (np.ndarray): Input array of numbers.
        replacement (float): Value to substitute for negatives. Default 0.

    Returns:
        np.ndarray: New array with negatives replaced.

    Examples:
        replace_negatives(np.array([1, -2, 3, -4, 5]))
        -> array([1, 0, 3, 0, 5])

        replace_negatives(np.array([-1, -2, -3]), replacement=99)
        -> array([99, 99, 99])
    """
    pass


# === Exercise 5: Row-wise Demean via Broadcasting ===

def demean_rows(arr):
    """Subtract each row's mean from that row using broadcasting.

    The result should have approximately zero mean along each row.

    Args:
        arr (np.ndarray): 2-D input array of shape (m, n).

    Returns:
        np.ndarray: 2-D array of the same shape where each row has
            been centred to zero mean.

    Examples:
        demean_rows(np.array([[10, 20, 30], [4, 4, 4]]))
        -> array([[-10.,   0.,  10.],
                  [  0.,   0.,   0.]])

        demean_rows(np.array([[1, 2], [3, 4]]))
        -> array([[-0.5,  0.5],
                  [-0.5,  0.5]])
    """
    pass
