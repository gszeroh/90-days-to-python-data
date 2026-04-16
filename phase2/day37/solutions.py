"""
Day 37: Statistics — Hypothesis Testing — Solutions
"""

import numpy as np
from scipy import stats


# === Exercise 1: One-Sample t-Test ===

def one_sample_ttest(data, hypothesized_mean, alpha=0.05):
    """Perform a one-sample t-test.

    Test whether the mean of *data* differs significantly from
    *hypothesized_mean*.

    Parameters
    ----------
    data : array-like
        1-D array of sample observations.
    hypothesized_mean : float
        The population mean under the null hypothesis (H₀: μ = hypothesized_mean).
    alpha : float, optional
        Significance level (default 0.05).

    Returns
    -------
    dict
        Dictionary with keys:
        - ``"t_stat"`` (float): The t test-statistic.
        - ``"p_value"`` (float): Two-sided p-value.
        - ``"reject"`` (bool): True if H₀ is rejected at the given *alpha*.

    Examples
    --------
    >>> result = one_sample_ttest([102, 98, 104, 101, 97, 105, 99, 103], 100)
    >>> isinstance(result, dict)
    True
    >>> all(k in result for k in ("t_stat", "p_value", "reject"))
    True
    """
    t_stat, p_value = stats.ttest_1samp(data, popmean=hypothesized_mean)
    return {
        "t_stat": float(t_stat),
        "p_value": float(p_value),
        "reject": bool(p_value < alpha),
    }


# === Exercise 2: Independent Two-Sample t-Test ===

def independent_ttest(sample_a, sample_b, alpha=0.05):
    """Perform an independent (unpaired) two-sample t-test.

    Uses Welch's t-test (does not assume equal variances).

    Parameters
    ----------
    sample_a : array-like
        Observations from group A.
    sample_b : array-like
        Observations from group B.
    alpha : float, optional
        Significance level (default 0.05).

    Returns
    -------
    dict
        Dictionary with keys:
        - ``"t_stat"`` (float): The t test-statistic.
        - ``"p_value"`` (float): Two-sided p-value.
        - ``"reject"`` (bool): True if H₀ (equal means) is rejected.

    Examples
    --------
    >>> result = independent_ttest([23, 25, 28, 22, 27], [30, 33, 29, 35, 31])
    >>> result["reject"]
    True
    """
    t_stat, p_value = stats.ttest_ind(sample_a, sample_b, equal_var=False)
    return {
        "t_stat": float(t_stat),
        "p_value": float(p_value),
        "reject": bool(p_value < alpha),
    }


# === Exercise 3: Chi-Square Test of Independence ===

def chi_square_independence(table, alpha=0.05):
    """Perform a chi-square test of independence on a contingency table.

    Parameters
    ----------
    table : array-like
        2-D array (at least 2×2) of observed frequencies.
    alpha : float, optional
        Significance level (default 0.05).

    Returns
    -------
    dict
        Dictionary with keys:
        - ``"chi2"`` (float): The chi-square test statistic.
        - ``"p_value"`` (float): The p-value of the test.
        - ``"dof"`` (int): Degrees of freedom.
        - ``"reject"`` (bool): True if H₀ (independence) is rejected.

    Examples
    --------
    >>> table = [[30, 10], [5, 25]]
    >>> result = chi_square_independence(table)
    >>> result["reject"]
    True
    >>> result["dof"]
    1
    """
    chi2, p_value, dof, _ = stats.chi2_contingency(table)
    return {
        "chi2": float(chi2),
        "p_value": float(p_value),
        "dof": int(dof),
        "reject": bool(p_value < alpha),
    }


# === Exercise 4: Confidence Interval for a Mean ===

def confidence_interval(data, confidence=0.95):
    """Compute a confidence interval for the population mean.

    Uses the t-distribution to account for unknown population variance.

    Parameters
    ----------
    data : array-like
        1-D array of sample observations (n ≥ 2).
    confidence : float, optional
        Confidence level between 0 and 1 (default 0.95).

    Returns
    -------
    tuple of (float, float)
        ``(lower, upper)`` bounds of the confidence interval.

    Examples
    --------
    >>> lo, hi = confidence_interval([12.1, 11.8, 12.5, 12.0, 11.9, 12.3])
    >>> bool(lo < 12.1 < hi)
    True
    >>> lo95, hi95 = confidence_interval([10, 20, 30], 0.95)
    >>> bool(lo95 < 20.0 < hi95)
    True
    """
    arr = np.asarray(data, dtype=float)
    n = len(arr)
    mean = arr.mean()
    se = stats.sem(arr)
    lo, hi = stats.t.interval(confidence, df=n - 1, loc=mean, scale=se)
    return (float(lo), float(hi))


# === Exercise 5: Multiple Hypothesis Correction ===

def correct_pvalues(p_values, method="bonferroni"):
    """Apply a multiple-testing correction to a list of p-values.

    Supported methods:
    - ``"bonferroni"``: Multiply each p-value by the number of tests,
      capping at 1.0.

    Parameters
    ----------
    p_values : list of float
        Raw p-values from multiple hypothesis tests.
    method : str, optional
        Correction method (default ``"bonferroni"``).

    Returns
    -------
    tuple of (list of float, list of bool)
        A 2-tuple where the first element is the list of adjusted p-values
        and the second element is a list of booleans indicating whether
        each null hypothesis is rejected at α = 0.05.

    Examples
    --------
    >>> adj, reject = correct_pvalues([0.01, 0.04, 0.03, 0.20], "bonferroni")
    >>> adj
    [0.04, 0.16, 0.12, 0.8]
    >>> reject
    [True, False, False, False]
    """
    m = len(p_values)
    if method == "bonferroni":
        adjusted = [min(p * m, 1.0) for p in p_values]
    else:
        raise ValueError(f"Unsupported method: {method!r}")
    reject = [p < 0.05 for p in adjusted]
    return (adjusted, reject)
