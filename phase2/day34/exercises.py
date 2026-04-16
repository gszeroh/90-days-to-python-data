"""Day 34: Plotly — Interactive Visualizations — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np


# === Exercise 1: Interactive Scatter Plot ===

def create_scatter_plot(df, x_col, y_col, color_col, size_col, title):
    """Create an interactive scatter plot with color and size mapping.

    Use plotly express to build a scatter plot from the given DataFrame.
    Apply the 'plotly_white' template and add axis labels derived from
    the column names (replace underscores with spaces and title-case).

    Args:
        df (pd.DataFrame): Input data.
        x_col (str): Column name for the x-axis.
        y_col (str): Column name for the y-axis.
        color_col (str): Column name for color encoding.
        size_col (str): Column name for marker size encoding.
        title (str): Chart title.

    Returns:
        go.Figure: A plotly Figure with the scatter plot.

    Examples:
        tips = px.data.tips()
        fig = create_scatter_plot(tips, "total_bill", "tip", "day", "size", "Tips")
        len(fig.data) > 0 -> True
    """
    pass


# === Exercise 2: Grouped Bar Chart ===

def create_grouped_bar(df, x_col, y_col, color_col, title, colors=None):
    """Create a grouped bar chart with custom colors and layout.

    Use plotly express to build a grouped bar chart (barmode='group').
    If a list of colors is provided, apply it via color_discrete_sequence.
    Set the legend to horizontal orientation positioned above the chart.

    Args:
        df (pd.DataFrame): Input data.
        x_col (str): Column for the x-axis (categories).
        y_col (str): Column for the y-axis (values).
        color_col (str): Column for grouping/coloring bars.
        title (str): Chart title.
        colors (list or None): Optional list of hex color strings.

    Returns:
        go.Figure: A plotly Figure with the grouped bar chart.

    Examples:
        medals = px.data.medals_long()
        fig = create_grouped_bar(medals, "nation", "count", "medal", "Medals")
        fig.layout.barmode -> 'group'
    """
    pass


# === Exercise 3: Multi-Trace Line with Dropdown ===

def create_line_with_dropdown(df, x_col, y_col, trace_col, title):
    """Create a line chart with multiple traces and a dropdown selector.

    Build a line chart using plotly graph_objects. Each unique value in
    trace_col becomes a separate trace. Add a dropdown menu (updatemenus)
    that lets the user show/hide individual traces. The dropdown should
    include an 'All' option that shows every trace.

    Args:
        df (pd.DataFrame): Input data.
        x_col (str): Column for x-axis.
        y_col (str): Column for y-axis.
        trace_col (str): Column whose unique values define separate traces.
        title (str): Chart title.

    Returns:
        go.Figure: A plotly Figure with dropdown menu for trace selection.

    Examples:
        gap = px.data.gapminder().query("continent == 'Europe'")
        fig = create_line_with_dropdown(gap, "year", "lifeExp", "country", "EU")
        len(fig.layout.updatemenus) > 0 -> True
    """
    pass


# === Exercise 4: Four-Panel Subplot Dashboard ===

def create_subplot_dashboard(df):
    """Create a 2×2 subplot dashboard with four different chart types.

    Using the provided DataFrame (assumed to have numeric and categorical
    columns), create a figure with:
      - Top-left (row=1, col=1): Scatter plot of the first two numeric columns.
      - Top-right (row=1, col=2): Histogram of the first numeric column.
      - Bottom-left (row=2, col=1): Box plot of the first numeric column
        grouped by the first categorical column.
      - Bottom-right (row=2, col=2): Bar chart showing mean of the first
        numeric column per category of the first categorical column.

    Use make_subplots with appropriate subplot_titles. Set overall height
    to 700 and width to 900.

    Args:
        df (pd.DataFrame): Input data with at least two numeric columns
            and one categorical column.

    Returns:
        go.Figure: A 2×2 subplot figure.

    Examples:
        tips = px.data.tips()
        fig = create_subplot_dashboard(tips)
        len(fig.data) == 4 -> True
    """
    pass


# === Exercise 5: Animated Scatter Plot ===

def create_animated_scatter(df, x_col, y_col, size_col, color_col,
                            animation_col, hover_col, title, log_x=False):
    """Create an animated scatter plot (gapminder-style).

    Use plotly express to create an animated scatter plot where each frame
    corresponds to a unique value in animation_col. Set size_max to 60.
    Apply the hover_col as hover_name for tooltip labels. Optionally use
    a logarithmic x-axis.

    Args:
        df (pd.DataFrame): Input data.
        x_col (str): Column for x-axis.
        y_col (str): Column for y-axis.
        size_col (str): Column for bubble size.
        color_col (str): Column for color encoding.
        animation_col (str): Column for animation frames.
        hover_col (str): Column for hover labels.
        title (str): Chart title.
        log_x (bool): Whether to use logarithmic x-axis. Defaults to False.

    Returns:
        go.Figure: An animated plotly Figure with play/pause controls.

    Examples:
        gap = px.data.gapminder()
        fig = create_animated_scatter(
            gap, "gdpPercap", "lifeExp", "pop", "continent",
            "year", "country", "Gapminder", log_x=True,
        )
        len(fig.frames) > 0 -> True
    """
    pass
