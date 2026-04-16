"""
Day 21: NumPy — Arrays & Operations — Solutions

Complete each function below according to its docstring.
"""

import numpy as np


# === Exercise 1: Create a Specific Array ===

def create_checkerboard(n):
    """Return an n×n checkerboard pattern of 0s and 1s as a NumPy array.

    The top-left element should be 0.

    Args:
        n (int): Size of the square array (n >= 1).

    Returns:
        np.ndarray: An n×n array of dtype int with alternating 0s and 1s.

    Examples:
        create_checkerboard(2)
        -> array([[0, 1],
                  [1, 0]])

        create_checkerboard(3)
        -> array([[0, 1, 0],
                  [1, 0, 1],
                  [0, 1, 0]])
    """
    row = np.arange(n)
    col = np.arange(n)
    return (row[:, np.newaxis] + col[np.newaxis, :]) % 2


# === Exercise 2: Reshape and Transpose ===

def reshape_and_transpose(arr, rows, cols):
    """Reshape a 1-D array to (rows, cols) and return its transpose.

    Args:
        arr (np.ndarray): A 1-D NumPy array whose length equals rows * cols.
        rows (int): Number of rows for the reshaped array.
        cols (int): Number of columns for the reshaped array.

    Returns:
        np.ndarray: The transposed array with shape (cols, rows).

    Examples:
        reshape_and_transpose(np.arange(6), 2, 3)
        -> array([[0, 3],
                  [1, 4],
                  [2, 5]])

        reshape_and_transpose(np.arange(4), 2, 2)
        -> array([[0, 2],
                  [1, 3]])
    """
    return arr.reshape(rows, cols).T


# === Exercise 3: Element-wise Operations ===

def celsius_to_fahrenheit(temps):
    """Convert an array of temperatures from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32

    Args:
        temps (np.ndarray): 1-D array of temperatures in Celsius.

    Returns:
        np.ndarray: Temperatures converted to Fahrenheit (float64).

    Examples:
        celsius_to_fahrenheit(np.array([0, 100]))
        -> array([ 32., 212.])

        celsius_to_fahrenheit(np.array([-40, 37]))
        -> array([-40. ,  98.6])
    """
    return temps.astype(np.float64) * 9 / 5 + 32


# === Exercise 4: dtype Conversion ===

def clip_and_convert(arr, low, high):
    """Clip array values to [low, high] and convert to int32.

    Args:
        arr (np.ndarray): Input array of any numeric dtype.
        low (float): Minimum allowed value.
        high (float): Maximum allowed value.

    Returns:
        np.ndarray: Clipped array with dtype np.int32.

    Examples:
        clip_and_convert(np.array([1.7, 5.2, -3.1, 8.9]), 0, 5)
        -> array([1, 5, 0, 5], dtype=int32)

        clip_and_convert(np.array([10, 20, 30]), 15, 25)
        -> array([15, 20, 25], dtype=int32)
    """
    return np.clip(arr, low, high).astype(np.int32)


# === Exercise 5: Normalize an Array ===

def normalize(arr):
    """Normalize a numeric array to the range [0, 1] using min-max scaling.

    Formula: (x - min) / (max - min)

    If all elements are the same (max == min), return an array of zeros
    with the same shape.

    Args:
        arr (np.ndarray): Input array of any shape with numeric dtype.

    Returns:
        np.ndarray: Array of float64 values in [0, 1] with the same shape.

    Examples:
        normalize(np.array([10, 20, 30, 40, 50]))
        -> array([0.  , 0.25, 0.5 , 0.75, 1.  ])

        normalize(np.array([5, 5, 5]))
        -> array([0., 0., 0.])

        normalize(np.array([[1, 2], [3, 4]]))
        -> array([[0.        , 0.33333333],
                  [0.66666667, 1.        ]])
    """
    arr = arr.astype(np.float64)
    arr_min = arr.min()
    arr_max = arr.max()
    if arr_max == arr_min:
        return np.zeros_like(arr, dtype=np.float64)
    return (arr - arr_min) / (arr_max - arr_min)
