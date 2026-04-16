"""
Day 36: Statistics — Probability & Distributions — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import numpy as np
from scipy import stats


# === Exercise 1: Binomial Probability ===

def binomial_probability(n, p, k):
    """Compute the binomial probability P(X = k).

    The probability of getting exactly *k* successes in *n* independent
    Bernoulli trials, each with success probability *p*.

    Parameters
    ----------
    n : int
        Number of trials (n ≥ 1).
    p : float
        Probability of success on a single trial (0 ≤ p ≤ 1).
    k : int
        Number of successes to query (0 ≤ k ≤ n).

    Returns
    -------
    float
        P(X = k) for X ~ Binomial(n, p).

    Examples
    --------
    >>> round(binomial_probability(10, 0.5, 5), 4)
    0.2461
    >>> round(binomial_probability(20, 0.3, 6), 4)
    0.1916
    """
    pass


# === Exercise 2: Normal CDF ===

def normal_cdf(x, mean=0.0, std=1.0):
    """Compute the normal cumulative distribution function P(X ≤ x).

    Parameters
    ----------
    x : float
        The value at which to evaluate the CDF.
    mean : float, optional
        Mean of the normal distribution (default 0).
    std : float, optional
        Standard deviation of the normal distribution (default 1).

    Returns
    -------
    float
        P(X ≤ x) for X ~ Normal(mean, std).

    Examples
    --------
    >>> round(normal_cdf(0.0), 4)
    0.5
    >>> round(normal_cdf(1.96, 0, 1), 4)
    0.975
    >>> round(normal_cdf(115, 100, 15), 4)
    0.8413
    """
    pass


# === Exercise 3: Z-Score Threshold ===

def z_score_threshold(confidence_level):
    """Find the z-score threshold for a symmetric confidence interval.

    For a given confidence level (e.g. 0.95), return the positive z-value
    such that P(-z ≤ Z ≤ z) = confidence_level for Z ~ Normal(0, 1).

    Parameters
    ----------
    confidence_level : float
        The desired confidence level (0 < confidence_level < 1).

    Returns
    -------
    float
        The positive z-score threshold.

    Examples
    --------
    >>> round(z_score_threshold(0.95), 4)
    1.96
    >>> round(z_score_threshold(0.99), 4)
    2.5758
    >>> round(z_score_threshold(0.90), 4)
    1.6449
    """
    pass


# === Exercise 4: Simulate the Central Limit Theorem ===

def simulate_clt(data, num_samples, sample_size, seed=42):
    """Simulate the Central Limit Theorem by repeated sampling.

    Draw *num_samples* random samples (with replacement) of size
    *sample_size* from *data* and return the array of sample means.

    Parameters
    ----------
    data : array-like
        The population data to sample from.
    num_samples : int
        Number of random samples to draw.
    sample_size : int
        Size of each individual sample.
    seed : int, optional
        Random seed for reproducibility (default 42).

    Returns
    -------
    numpy.ndarray
        1-D array of length *num_samples* containing the sample means.

    Examples
    --------
    >>> means = simulate_clt([1, 2, 3, 4, 5], num_samples=1000, sample_size=3)
    >>> means.shape
    (1000,)
    >>> bool(2.5 < means.mean() < 3.5)
    True
    """
    pass


# === Exercise 5: Bayesian Posterior ===

def bayesian_posterior(prior, likelihood, evidence):
    """Compute the Bayesian posterior probability.

    Applies Bayes' Theorem:
        P(H | E) = P(E | H) · P(H) / P(E)

    Parameters
    ----------
    prior : float
        Prior probability P(H), where 0 ≤ prior ≤ 1.
    likelihood : float
        Likelihood P(E | H), where 0 ≤ likelihood ≤ 1.
    evidence : float
        Evidence (marginal likelihood) P(E), where 0 < evidence ≤ 1.

    Returns
    -------
    float
        Posterior probability P(H | E).

    Examples
    --------
    >>> round(bayesian_posterior(0.01, 0.99, 0.0594), 4)
    0.1667
    >>> round(bayesian_posterior(0.5, 0.8, 0.5), 4)
    0.8
    """
    pass
