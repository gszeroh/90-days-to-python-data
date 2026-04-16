"""Day 31: Matplotlib — Fundamentals — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# === Exercise 1: Line Plot ===

def line_plot(x, y, title, xlabel, ylabel):
    """Create a line plot and return the Figure and Axes.

    Plot *y* versus *x* as a solid blue line with circle markers.  Set the
    title, x-label, and y-label to the provided strings.

    Args:
        x (array-like): X-axis values.
        y (array-like): Y-axis values.
        title (str): Plot title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        fig, ax = line_plot([1, 2, 3], [2, 4, 6], "My Line", "X", "Y")
        ax.get_title()   # "My Line"
        len(ax.lines)    # 1
    """
    pass


# === Exercise 2: Grouped Bar Chart ===

def grouped_bar_chart(labels, group_data, group_names, title):
    """Create a grouped (side-by-side) bar chart.

    Each key in *group_data* maps a group name to a list of values (one per
    label).  Bars for different groups sit next to each other with a total
    bar width that does not exceed 0.8 per label.

    Args:
        labels (list[str]): Category labels for the x-axis.
        group_data (dict[str, list[float]]): Mapping of group name → values.
            Length of each value list must equal ``len(labels)``.
        group_names (list[str]): Ordered list of group names (keys of
            *group_data*) that determines the plotting order.
        title (str): Plot title.

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        fig, ax = grouped_bar_chart(
            ["Q1", "Q2"],
            {"A": [10, 20], "B": [15, 25]},
            ["A", "B"],
            "Revenue",
        )
        ax.get_title()  # "Revenue"
    """
    pass


# === Exercise 3: Scatter Plot with Colour Mapping ===

def scatter_with_cmap(x, y, colors, title, cmap="viridis"):
    """Create a scatter plot with a colour map and colour bar.

    Plot *y* versus *x* using *colors* for the colour-mapped values.  Add a
    colour bar to the figure.  Set marker transparency to 0.7.

    Args:
        x (array-like): X-axis values.
        y (array-like): Y-axis values.
        colors (array-like): Values mapped to the colourmap.
        title (str): Plot title.
        cmap (str): Matplotlib colourmap name (default ``"viridis"``).

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        fig, ax = scatter_with_cmap(
            [1, 2, 3], [3, 2, 1], [0.1, 0.5, 0.9], "Scatter"
        )
        ax.get_title()  # "Scatter"
    """
    pass


# === Exercise 4: Histogram ===

def histogram(data, bins, title, xlabel):
    """Create a histogram and return the Figure and Axes.

    Plot *data* with the specified number of *bins*, black edge colour, and
    alpha of 0.7.  Set the title, x-label, and y-label (``"Frequency"``).

    Args:
        data (array-like): 1-D numerical data.
        bins (int): Number of histogram bins.
        title (str): Plot title.
        xlabel (str): X-axis label.

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        import numpy as np
        fig, ax = histogram(np.random.randn(500), 25, "Dist", "Value")
        ax.get_title()  # "Dist"
        ax.get_ylabel() # "Frequency"
    """
    pass


# === Exercise 5: Multi-Plot Figure ===

def multi_plot(x, y_line, y_scatter, hist_data):
    """Create a 2×2 figure with four different plot types.

    Subplot layout (row, col):
        (0, 0) — Line plot of *y_line* vs *x*.
        (0, 1) — Scatter plot of *y_scatter* vs *x*.
        (1, 0) — Histogram of *hist_data* with 20 bins.
        (1, 1) — Bar chart with labels ``["A", "B", "C", "D"]`` and
                  values ``[4, 7, 1, 8]``.

    Each subplot must have a descriptive title.  Call ``fig.tight_layout()``
    before returning.

    Args:
        x (array-like): Shared x values for the line and scatter plots.
        y_line (array-like): Y values for the line plot.
        y_scatter (array-like): Y values for the scatter plot.
        hist_data (array-like): 1-D data for the histogram.

    Returns:
        plt.Figure: The Figure containing all four subplots.

    Examples:
        import numpy as np
        x = np.arange(50)
        fig = multi_plot(x, x ** 2, np.sin(x), np.random.randn(500))
        len(fig.axes)  # 4
    """
    pass
