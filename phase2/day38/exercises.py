"""
Day 38: Statistics — Correlation & Regression Basics — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import numpy as np
from scipy import stats


# === Exercise 1: Pearson & Spearman Correlation ===

def compute_correlations(x, y):
    """Compute Pearson and Spearman correlation between two arrays.

    Parameters
    ----------
    x : array-like
        First variable (1-D).
    y : array-like
        Second variable (1-D), same length as *x*.

    Returns
    -------
    dict
        Dictionary with keys:
        - ``"pearson_r"`` (float): Pearson correlation coefficient.
        - ``"pearson_p"`` (float): Two-sided p-value for Pearson test.
        - ``"spearman_r"`` (float): Spearman rank correlation coefficient.
        - ``"spearman_p"`` (float): Two-sided p-value for Spearman test.

    Examples
    --------
    >>> result = compute_correlations([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
    >>> isinstance(result, dict)
    True
    >>> all(k in result for k in ("pearson_r", "pearson_p", "spearman_r", "spearman_p"))
    True
    >>> 0 < result["pearson_r"] < 1
    True
    """
    pass


# === Exercise 2: Correlation Matrix ===

def correlation_matrix(df, method="pearson"):
    """Build a correlation matrix for a DataFrame's numeric columns.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing at least two numeric columns.
    method : str, optional
        Correlation method — ``"pearson"`` (default) or ``"spearman"``.

    Returns
    -------
    pandas.DataFrame
        Square DataFrame of pairwise correlation coefficients for all
        numeric columns.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    >>> cm = correlation_matrix(df)
    >>> cm.shape
    (3, 3)
    >>> float(cm.loc["a", "a"])
    1.0
    """
    pass


# === Exercise 3: Simple Linear Regression ===

def simple_linear_regression(x, y):
    """Perform simple linear regression on *x* and *y*.

    Use ``scipy.stats.linregress`` to fit the model ŷ = slope · x + intercept.

    Parameters
    ----------
    x : array-like
        Independent variable (1-D).
    y : array-like
        Dependent variable (1-D), same length as *x*.

    Returns
    -------
    dict
        Dictionary with keys:
        - ``"slope"`` (float): Estimated slope (b₁).
        - ``"intercept"`` (float): Estimated intercept (b₀).
        - ``"r_value"`` (float): Pearson correlation coefficient.
        - ``"r_squared"`` (float): Coefficient of determination (r²).
        - ``"p_value"`` (float): Two-sided p-value for the slope.
        - ``"std_err"`` (float): Standard error of the slope estimate.

    Examples
    --------
    >>> res = simple_linear_regression([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
    >>> isinstance(res, dict)
    True
    >>> 0 < res["slope"] < 2
    True
    >>> 0 <= res["r_squared"] <= 1
    True
    """
    pass


# === Exercise 4: Predict with Regression ===

def predict(slope, intercept, x_new):
    """Predict y values using a fitted linear regression.

    Parameters
    ----------
    slope : float
        Slope of the regression line.
    intercept : float
        Intercept of the regression line.
    x_new : array-like
        New x values for which to predict y.

    Returns
    -------
    numpy.ndarray
        Predicted y values (same length as *x_new*).

    Examples
    --------
    >>> import numpy as np
    >>> preds = predict(2.0, 1.0, [3, 4, 5])
    >>> np.allclose(preds, [7.0, 9.0, 11.0])
    True
    """
    pass


# === Exercise 5: Residuals & R² ===

def regression_diagnostics(y_actual, y_predicted):
    """Compute residuals, R², and MSE for a regression.

    Parameters
    ----------
    y_actual : array-like
        Observed y values.
    y_predicted : array-like
        Predicted y values from the model, same length as *y_actual*.

    Returns
    -------
    dict
        Dictionary with keys:
        - ``"residuals"`` (numpy.ndarray): Array of residuals (y − ŷ).
        - ``"r_squared"`` (float): Coefficient of determination.
        - ``"mse"`` (float): Mean squared error.

    Examples
    --------
    >>> import numpy as np
    >>> diag = regression_diagnostics([3, 5, 7], [2.8, 5.1, 7.2])
    >>> len(diag["residuals"])
    3
    >>> diag["r_squared"] > 0.9
    True
    """
    pass
