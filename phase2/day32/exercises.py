"""Day 32: Matplotlib — Advanced Visualizations — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec


# === Exercise 1: Custom GridSpec Layout ===

def gridspec_layout(x, y_top, y_bottom_left, y_bottom_right):
    """Create a figure with a custom GridSpec layout.

    Build a figure with three subplots arranged via ``GridSpec(2, 2)``:
        - **Top** (row 0, both columns): Line plot of *y_top* vs *x*.
        - **Bottom-left** (row 1, col 0): Bar chart with labels
          ``["A", "B", "C", "D"]`` and values from *y_bottom_left*.
        - **Bottom-right** (row 1, col 1): Scatter plot of
          *y_bottom_right* vs *x* with ``alpha=0.6``.

    Each subplot must have a descriptive title.  Use ``figsize=(10, 6)``.

    Args:
        x (array-like): X-axis values for the line and scatter plots.
        y_top (array-like): Y values for the top line plot.
        y_bottom_left (list[float]): Four values for the bar chart.
        y_bottom_right (array-like): Y values for the bottom-right scatter.

    Returns:
        plt.Figure: The Figure containing all three subplots.

    Examples:
        import numpy as np
        x = np.linspace(0, 10, 50)
        fig = gridspec_layout(x, np.sin(x), [3, 7, 5, 2], np.cos(x))
        len(fig.axes)  # 3
    """
    pass


# === Exercise 2: Annotated Line Plot ===

def annotated_minmax(x, y, title):
    """Create a line plot with annotations at the minimum and maximum points.

    Plot *y* vs *x* as a solid line.  Identify the indices of the minimum
    and maximum values in *y*.  Use ``ax.annotate()`` to label each point:
        - **Max** annotation in green with an arrow (``arrowstyle="->"``)
          pointing to the maximum, text offset ``(+1.0, +0.15)`` from point.
        - **Min** annotation in red with an arrow (``arrowstyle="->"``)
          pointing to the minimum, text offset ``(+1.0, -0.15)`` from point.

    Set the plot title to *title*.

    Args:
        x (array-like): X-axis values.
        y (array-like): Y-axis values.
        title (str): Plot title.

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        import numpy as np
        x = np.linspace(0, 2 * np.pi, 100)
        fig, ax = annotated_minmax(x, np.sin(x), "Sine Wave")
        ax.get_title()  # "Sine Wave"
        len(ax.texts)   # >= 2  (annotation texts)
    """
    pass


# === Exercise 3: Styled Pie Chart ===

def styled_pie(sizes, labels, title, explode=None):
    """Create a styled pie chart.

    Draw a pie chart with percentage labels (``autopct="%1.1f%%"``),
    starting at 90°.  If *explode* is provided, apply it.  Use the
    ``Set2`` colourmap for slice colours.

    Args:
        sizes (list[float]): Wedge sizes (do not need to sum to 100).
        labels (list[str]): Label for each wedge.
        title (str): Plot title.
        explode (tuple[float] | None): Fraction to offset each wedge.
            Defaults to ``None``.

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        fig, ax = styled_pie(
            [40, 30, 20, 10], ["A", "B", "C", "D"], "Share"
        )
        ax.get_title()  # "Share"
    """
    pass


# === Exercise 4: Heatmap with Colour Bar ===

def heatmap(data, row_labels, col_labels, title, cmap="YlOrRd"):
    """Create a heatmap from a 2-D array with a colour bar.

    Display *data* using ``ax.imshow()`` with ``aspect="auto"`` and the
    specified *cmap*.  Add a colour bar labelled ``"Value"``.  Set tick
    labels to *row_labels* (y-axis) and *col_labels* (x-axis, rotated 45°).
    Overlay each cell with its value formatted to one decimal place.

    Args:
        data (np.ndarray): 2-D numeric array of shape ``(rows, cols)``.
        row_labels (list[str]): Labels for each row.
        col_labels (list[str]): Labels for each column.
        title (str): Plot title.
        cmap (str): Matplotlib colourmap name (default ``"YlOrRd"``).

    Returns:
        tuple[plt.Figure, plt.Axes]: The (fig, ax) pair.

    Examples:
        import numpy as np
        data = np.array([[1.0, 2.0], [3.0, 4.0]])
        fig, ax = heatmap(data, ["r0", "r1"], ["c0", "c1"], "Test")
        ax.get_title()  # "Test"
    """
    pass


# === Exercise 5: 3-D Surface Plot ===

def surface_plot(func, x_range=(-5, 5), y_range=(-5, 5), n=50, title="3-D Surface"):
    """Create a 3-D surface plot for a given mathematical function.

    Generate a mesh grid over *x_range* and *y_range* with *n* points per
    axis.  Evaluate ``Z = func(X, Y)`` and plot the surface using
    ``ax.plot_surface()`` with ``cmap="viridis"`` and ``edgecolor="none"``.
    Set axis labels to ``"X"``, ``"Y"``, ``"Z"`` and the title to *title*.

    Args:
        func (callable): A function ``f(X, Y) -> Z`` that accepts 2-D
            NumPy arrays and returns a 2-D array of the same shape.
        x_range (tuple[float, float]): ``(min, max)`` for the x-axis.
        y_range (tuple[float, float]): ``(min, max)`` for the y-axis.
        n (int): Number of grid points per axis (default 50).
        title (str): Plot title (default ``"3-D Surface"``).

    Returns:
        plt.Figure: The Figure containing the 3-D surface.

    Examples:
        import numpy as np
        fig = surface_plot(lambda X, Y: np.sin(np.sqrt(X**2 + Y**2)))
        len(fig.axes)  # 1
        fig.axes[0].get_title()  # "3-D Surface"
    """
    pass
