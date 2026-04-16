"""Day 34: Plotly — Interactive Visualizations — Solutions

Complete each function below according to its docstring.
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
    labels = {
        x_col: x_col.replace("_", " ").title(),
        y_col: y_col.replace("_", " ").title(),
    }
    fig = px.scatter(
        df, x=x_col, y=y_col, color=color_col, size=size_col,
        title=title, labels=labels, template="plotly_white",
    )
    return fig


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
    kwargs = dict(
        data_frame=df, x=x_col, y=y_col, color=color_col,
        title=title, barmode="group",
    )
    if colors is not None:
        kwargs["color_discrete_sequence"] = colors

    fig = px.bar(**kwargs)
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


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
    fig = go.Figure()
    unique_vals = df[trace_col].unique()

    for val in unique_vals:
        subset = df[df[trace_col] == val]
        fig.add_trace(go.Scatter(
            x=subset[x_col], y=subset[y_col],
            mode="lines", name=str(val),
        ))

    # Build dropdown buttons
    buttons = [dict(label="All", method="update",
                    args=[{"visible": [True] * len(unique_vals)}])]
    for i, val in enumerate(unique_vals):
        visibility = [False] * len(unique_vals)
        visibility[i] = True
        buttons.append(dict(
            label=str(val), method="update",
            args=[{"visible": visibility}],
        ))

    fig.update_layout(
        title=title,
        xaxis_title=x_col.replace("_", " ").title(),
        yaxis_title=y_col.replace("_", " ").title(),
        updatemenus=[dict(
            active=0, buttons=buttons,
            x=0.0, xanchor="left", y=1.15, yanchor="top",
        )],
        template="plotly_white",
    )
    return fig


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
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()
    num1, num2 = numeric_cols[0], numeric_cols[1]
    cat1 = cat_cols[0]

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Scatter", "Histogram", "Box Plot", "Bar Chart"),
    )

    # Scatter
    fig.add_trace(
        go.Scatter(x=df[num1], y=df[num2], mode="markers",
                   marker=dict(color="royalblue", opacity=0.6), name="Scatter"),
        row=1, col=1,
    )

    # Histogram
    fig.add_trace(
        go.Histogram(x=df[num1], marker_color="firebrick", name="Histogram"),
        row=1, col=2,
    )

    # Box plot grouped by first categorical column
    fig.add_trace(
        go.Box(x=df[cat1], y=df[num1], marker_color="seagreen", name="Box"),
        row=2, col=1,
    )

    # Bar chart of means
    means = df.groupby(cat1, observed=True)[num1].mean()
    fig.add_trace(
        go.Bar(x=means.index.astype(str), y=means.values,
               marker_color="mediumpurple", name="Mean"),
        row=2, col=2,
    )

    fig.update_layout(height=700, width=900, showlegend=False,
                      title_text="Four-Panel Dashboard")
    return fig


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
    fig = px.scatter(
        df, x=x_col, y=y_col, size=size_col, color=color_col,
        animation_frame=animation_col, hover_name=hover_col,
        title=title, log_x=log_x, size_max=60,
    )
    return fig
