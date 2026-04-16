"""Day 33: Seaborn — Statistical Visualization — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# === Exercise 1: Distribution Plot ===

def distribution_plot(series, bins=30, title="Distribution"):
    """Create a histogram with a KDE overlay for a numeric Series.

    Use ``sns.histplot()`` with ``kde=True`` on a pre-created ``Axes``.
    Set the plot title to *title*.

    Args:
        series (pd.Series): Numeric data to plot.
        bins (int): Number of histogram bins (default 30).
        title (str): Plot title (default ``"Distribution"``).

    Returns:
        matplotlib.axes.Axes: The Axes containing the plot.

    Examples:
        import pandas as pd, numpy as np
        s = pd.Series(np.random.default_rng(0).normal(50, 10, 200))
        ax = distribution_plot(s, bins=20, title="Test Dist")
        ax.get_title()  # "Test Dist"
    """
    pass


# === Exercise 2: Categorical Comparison ===

def categorical_comparison(df, x, y, title="Categorical Comparison"):
    """Create a box plot with a strip-plot overlay for a DataFrame.

    Draw a ``sns.boxplot()`` and then overlay a ``sns.stripplot()``
    (``color="black"``, ``alpha=0.3``, ``size=3``) on the same ``Axes``.
    Set the plot title to *title*.

    Args:
        df (pd.DataFrame): Source data.
        x (str): Column name for the categorical axis.
        y (str): Column name for the numeric axis.
        title (str): Plot title (default ``"Categorical Comparison"``).

    Returns:
        matplotlib.axes.Axes: The Axes containing the overlaid plots.

    Examples:
        tips = sns.load_dataset("tips")
        ax = categorical_comparison(tips, "day", "total_bill", "Bill by Day")
        ax.get_title()  # "Bill by Day"
    """
    pass


# === Exercise 3: Regression Plot ===

def regression_plot(df, x, y, ci=95, title="Regression"):
    """Create a regression scatter plot with a confidence interval band.

    Use ``sns.regplot()`` on a pre-created ``Axes`` with
    ``scatter_kws={"alpha": 0.5}``.  Set the plot title to *title*.

    Args:
        df (pd.DataFrame): Source data.
        x (str): Column name for the x-axis variable.
        y (str): Column name for the y-axis variable.
        ci (int): Confidence interval percentage (default 95).
        title (str): Plot title (default ``"Regression"``).

    Returns:
        matplotlib.axes.Axes: The Axes containing the regression plot.

    Examples:
        tips = sns.load_dataset("tips")
        ax = regression_plot(tips, "total_bill", "tip", title="Tip Fit")
        ax.get_title()  # "Tip Fit"
    """
    pass


# === Exercise 4: Annotated Correlation Heatmap ===

def correlation_heatmap(df, title="Correlation Heatmap", cmap="coolwarm"):
    """Create an annotated correlation heatmap for a DataFrame.

    Compute the Pearson correlation matrix of all numeric columns in *df*.
    Display it with ``sns.heatmap()`` using ``annot=True``, ``fmt=".2f"``,
    and ``linewidths=0.5``.  Set the plot title to *title*.

    Args:
        df (pd.DataFrame): Source data (must contain numeric columns).
        title (str): Plot title (default ``"Correlation Heatmap"``).
        cmap (str): Colour map name (default ``"coolwarm"``).

    Returns:
        tuple[plt.Figure, matplotlib.axes.Axes]: The (fig, ax) pair.

    Examples:
        tips = sns.load_dataset("tips")
        fig, ax = correlation_heatmap(tips, title="Tips Corr")
        ax.get_title()  # "Tips Corr"
    """
    pass


# === Exercise 5: Pair Plot ===

def pair_plot(df, numeric_cols, hue_col, diag_kind="kde"):
    """Create a pair plot for selected numeric columns coloured by a hue variable.

    Use ``sns.pairplot()`` with ``vars=numeric_cols``, ``hue=hue_col``,
    and ``diag_kind=diag_kind``.

    Args:
        df (pd.DataFrame): Source data.
        numeric_cols (list[str]): Column names for the pairwise axes.
        hue_col (str): Column name used for colour grouping.
        diag_kind (str): Kind of diagonal plot — ``"kde"`` or ``"hist"``
            (default ``"kde"``).

    Returns:
        sns.PairGrid: The PairGrid object produced by ``pairplot()``.

    Examples:
        penguins = sns.load_dataset("penguins").dropna()
        g = pair_plot(
            penguins,
            ["bill_length_mm", "bill_depth_mm"],
            "species",
        )
        type(g).__name__  # "PairGrid"
    """
    pass
