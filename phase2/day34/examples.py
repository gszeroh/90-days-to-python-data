"""Day 34: Plotly — Interactive Visualizations — Examples"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# === 1. Plotly Express Basics ===

print("=== 1. Plotly Express Basics ===\n")

# Scatter plot with color and size mapping
tips = px.data.tips()
print(f"Tips dataset: {tips.shape[0]} rows, {tips.shape[1]} columns")
print(f"Columns: {list(tips.columns)}\n")

fig_scatter = px.scatter(
    tips, x="total_bill", y="tip", color="day", size="size",
    title="Tips by Total Bill",
    labels={"total_bill": "Total Bill ($)", "tip": "Tip ($)"},
)
fig_scatter.write_html("scatter_basic.html")
print("Scatter plot saved to scatter_basic.html")

# Line chart with gapminder data
gapminder = px.data.gapminder()
europe = gapminder.query("continent == 'Europe'")
print(f"\nGapminder Europe: {europe['country'].nunique()} countries")

fig_line = px.line(
    europe, x="year", y="lifeExp", color="country",
    title="European Life Expectancy Over Time",
)
fig_line.write_html("line_basic.html")
print("Line chart saved to line_basic.html")

# Bar chart with medals data
medals = px.data.medals_long()
fig_bar = px.bar(
    medals, x="nation", y="count", color="medal",
    title="Olympic Medals by Nation",
)
fig_bar.write_html("bar_basic.html")
print("Bar chart saved to bar_basic.html")

# Histogram
fig_hist = px.histogram(
    tips, x="total_bill", nbins=30, color="sex",
    title="Distribution of Total Bills",
    labels={"total_bill": "Total Bill ($)"},
)
fig_hist.write_html("histogram_basic.html")
print("Histogram saved to histogram_basic.html")

# === 2. Customizing Plotly Charts ===

print("\n=== 2. Customizing Plotly Charts ===\n")

# Start with a basic scatter and customize it
fig_custom = px.scatter(
    tips, x="total_bill", y="tip", color="smoker",
    title="Customized Scatter Plot",
)

fig_custom.update_layout(
    title=dict(text="Tips: Smoker vs Non-Smoker", font=dict(size=22)),
    xaxis_title="Total Bill ($)",
    yaxis_title="Tip ($)",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    width=800,
    height=500,
)

fig_custom.update_traces(
    marker=dict(size=10, line=dict(width=1, color="DarkSlateGrey")),
    selector=dict(mode="markers"),
)
fig_custom.write_html("scatter_custom.html")
print("Customized scatter saved to scatter_custom.html")

# Demonstrate templates
templates = ["plotly", "plotly_white", "plotly_dark", "seaborn", "simple_white"]
print(f"\nAvailable templates: {templates}")

fig_template = px.scatter(
    tips, x="total_bill", y="tip",
    template="seaborn",
    title="Seaborn Template Example",
)
fig_template.write_html("scatter_seaborn.html")
print("Seaborn-styled scatter saved to scatter_seaborn.html")

# === 3. Advanced Chart Types ===

print("\n=== 3. Advanced Chart Types ===\n")

# Sunburst chart
fig_sunburst = px.sunburst(
    tips, path=["day", "time", "sex"], values="total_bill",
    title="Tips Breakdown: Day → Time → Sex",
)
fig_sunburst.write_html("sunburst.html")
print("Sunburst chart saved to sunburst.html")

# Treemap
gapminder_2007 = gapminder.query("year == 2007")
fig_treemap = px.treemap(
    gapminder_2007, path=["continent", "country"], values="pop",
    color="lifeExp", color_continuous_scale="Viridis",
    title="World Population Treemap (2007)",
)
fig_treemap.write_html("treemap.html")
print("Treemap saved to treemap.html")

# Choropleth map
fig_choropleth = px.choropleth(
    gapminder_2007, locations="iso_alpha", color="gdpPercap",
    hover_name="country",
    color_continuous_scale="Plasma",
    title="GDP per Capita (2007)",
)
fig_choropleth.write_html("choropleth.html")
print("Choropleth map saved to choropleth.html")

# Funnel chart
funnel_data = dict(
    stage=["Visitors", "Leads", "Prospects", "Negotiations", "Closed"],
    count=[1000, 600, 400, 200, 80],
)
fig_funnel = px.funnel(
    funnel_data, x="count", y="stage",
    title="Sales Funnel",
)
fig_funnel.write_html("funnel.html")
print("Funnel chart saved to funnel.html")

# === 4. Subplots with make_subplots ===

print("\n=== 4. Subplots with make_subplots ===\n")

fig_sub = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Scatter", "Line", "Bar", "Histogram"),
)

# Top-left: scatter
fig_sub.add_trace(
    go.Scatter(x=tips["total_bill"], y=tips["tip"],
               mode="markers", name="Tips", marker=dict(color="royalblue")),
    row=1, col=1,
)

# Top-right: line
yearly = gapminder.query("country == 'United States'")
fig_sub.add_trace(
    go.Scatter(x=yearly["year"], y=yearly["lifeExp"],
               mode="lines+markers", name="US Life Exp",
               line=dict(color="firebrick")),
    row=1, col=2,
)

# Bottom-left: bar
day_totals = tips.groupby("day", observed=True)["total_bill"].sum().reset_index()
fig_sub.add_trace(
    go.Bar(x=day_totals["day"], y=day_totals["total_bill"],
           name="Daily Total", marker_color="seagreen"),
    row=2, col=1,
)

# Bottom-right: histogram
fig_sub.add_trace(
    go.Histogram(x=tips["tip"], nbinsx=20, name="Tip Distribution",
                 marker_color="mediumpurple"),
    row=2, col=2,
)

fig_sub.update_layout(
    height=600, width=900,
    title_text="Dashboard with Four Subplots",
    showlegend=False,
)
fig_sub.write_html("subplots.html")
print("Subplot dashboard saved to subplots.html")

# Subplots with mixed types using specs
fig_mixed = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Bar Chart", "Pie Chart"),
)

fig_mixed.add_trace(
    go.Bar(x=["A", "B", "C"], y=[10, 20, 15], marker_color="steelblue"),
    row=1, col=1,
)
fig_mixed.add_trace(
    go.Pie(labels=["A", "B", "C"], values=[10, 20, 15]),
    row=1, col=2,
)
fig_mixed.update_layout(title_text="Mixed Subplot Types")
fig_mixed.write_html("subplots_mixed.html")
print("Mixed subplot types saved to subplots_mixed.html")

# === 5. Graph Objects for Fine Control ===

print("\n=== 5. Graph Objects for Fine Control ===\n")

# Build a multi-trace figure from scratch
np.random.seed(42)
x = np.linspace(0, 10, 50)
y1 = np.sin(x) + np.random.normal(0, 0.1, 50)
y2 = np.cos(x) + np.random.normal(0, 0.1, 50)

fig_go = go.Figure()

fig_go.add_trace(go.Scatter(
    x=x, y=y1,
    mode="lines+markers",
    name="sin(x) + noise",
    line=dict(color="royalblue", width=2),
    marker=dict(size=6, symbol="circle"),
))

fig_go.add_trace(go.Scatter(
    x=x, y=y2,
    mode="lines+markers",
    name="cos(x) + noise",
    line=dict(color="firebrick", width=2, dash="dash"),
    marker=dict(size=6, symbol="diamond"),
))

fig_go.update_layout(
    title="Trigonometric Functions with Noise",
    xaxis_title="x",
    yaxis_title="f(x)",
    template="plotly_white",
    hovermode="x unified",
)
fig_go.write_html("graph_objects.html")
print("Graph Objects figure saved to graph_objects.html")

# Bar chart with error bars
categories = ["Product A", "Product B", "Product C", "Product D"]
values = [45, 62, 38, 55]
errors = [5, 8, 4, 7]

fig_error = go.Figure(data=[
    go.Bar(
        x=categories, y=values,
        error_y=dict(type="data", array=errors, visible=True),
        marker_color=["#636EFA", "#EF553B", "#00CC96", "#AB63FA"],
        text=values,
        textposition="outside",
    )
])
fig_error.update_layout(
    title="Product Sales with Error Bars",
    yaxis_title="Sales",
    template="simple_white",
)
fig_error.write_html("bar_error_bars.html")
print("Bar chart with error bars saved to bar_error_bars.html")

# === 6. Exporting & Sharing ===

print("\n=== 6. Exporting & Sharing ===\n")

# Create a polished figure for export
fig_export = px.scatter(
    gapminder.query("year == 2007"),
    x="gdpPercap", y="lifeExp", size="pop", color="continent",
    hover_name="country", log_x=True, size_max=60,
    title="Gapminder 2007: GDP vs Life Expectancy",
    labels={"gdpPercap": "GDP per Capita (log)", "lifeExp": "Life Expectancy"},
)

# HTML export — fully interactive
fig_export.write_html("gapminder_2007.html")
print("Interactive HTML saved to gapminder_2007.html")

# HTML export with CDN (smaller file size)
fig_export.write_html("gapminder_2007_cdn.html", include_plotlyjs="cdn")
print("CDN-based HTML saved to gapminder_2007_cdn.html")

# Show figure as JSON summary
fig_json = fig_export.to_json()
print(f"\nFigure JSON length: {len(fig_json):,} characters")
print(f"Number of traces: {len(fig_export.data)}")
print(f"Layout template: {fig_export.layout.template.layout.to_plotly_json().get('paper_bgcolor', 'default')}")

print("\nAll examples complete!")
