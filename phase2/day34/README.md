# Day 34: Plotly — Interactive Visualizations

## Overview

Plotly is a powerful Python library for creating interactive, publication-quality
visualizations that run in any web browser. Unlike static Matplotlib charts, Plotly
figures support hover tooltips, zoom, pan, and click interactions out of the box.
Plotly Express provides a concise, high-level API while Graph Objects offer
fine-grained control for complex visualizations.

| Capability | API | Use Case |
|---|---|---|
| Quick charts | `plotly.express` | Rapid exploration and prototyping |
| Fine control | `plotly.graph_objects` | Custom multi-trace figures |
| Subplots | `make_subplots` | Dashboard-style layouts |
| Export | `write_html`, `write_image` | Sharing and embedding |
| Animation | `animation_frame` | Time-series storytelling |

---

## 1. Plotly Express Basics

Plotly Express (`px`) is the recommended starting point — one function call produces
a fully interactive chart.

### Scatter Plot

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="day", size="size",
                 title="Tips by Total Bill")
fig.show()
```

### Line Chart

```python
df = px.data.gapminder().query("continent == 'Europe'")
fig = px.line(df, x="year", y="lifeExp", color="country",
              title="European Life Expectancy Over Time")
fig.show()
```

### Bar Chart

```python
df = px.data.medals_long()
fig = px.bar(df, x="nation", y="count", color="medal",
             title="Olympic Medals by Nation")
fig.show()
```

### Histogram

```python
df = px.data.tips()
fig = px.histogram(df, x="total_bill", nbins=30, color="sex",
                   title="Distribution of Total Bills")
fig.show()
```

> 💡 Every `px` function returns a `go.Figure` object, so you can further
> customize it using `update_layout()` and `update_traces()`.

---

## 2. Customizing Plotly Charts

### Layout Customization

```python
fig.update_layout(
    title=dict(text="Custom Title", font=dict(size=24)),
    xaxis_title="X Axis Label",
    yaxis_title="Y Axis Label",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02),
    width=800,
    height=500,
)
```

### Trace Customization

```python
fig.update_traces(
    marker=dict(size=12, line=dict(width=1, color="DarkSlateGrey")),
    selector=dict(mode="markers"),
)
```

### Built-in Templates

| Template | Style |
|---|---|
| `plotly` | Default with grid |
| `plotly_white` | Clean white background |
| `plotly_dark` | Dark theme |
| `seaborn` | Seaborn-inspired |
| `simple_white` | Minimal white |

```python
fig = px.scatter(df, x="total_bill", y="tip", template="plotly_dark")
```

---

## 3. Advanced Chart Types

### Sunburst Chart

```python
df = px.data.tips()
fig = px.sunburst(df, path=["day", "time", "sex"], values="total_bill",
                  title="Tips Breakdown: Day → Time → Sex")
fig.show()
```

### Treemap

```python
df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=["continent", "country"], values="pop",
                 color="lifeExp", color_continuous_scale="Viridis",
                 title="World Population Treemap (2007)")
fig.show()
```

### Choropleth Map

```python
df = px.data.gapminder().query("year == 2007")
fig = px.choropleth(df, locations="iso_alpha", color="gdpPercap",
                    hover_name="country",
                    color_continuous_scale="Plasma",
                    title="GDP per Capita (2007)")
fig.show()
```

### Funnel Chart

```python
data = dict(
    stage=["Visitors", "Leads", "Prospects", "Negotiations", "Closed"],
    count=[1000, 600, 400, 200, 80],
)
fig = px.funnel(data, x="count", y="stage", title="Sales Funnel")
fig.show()
```

---

## 4. Subplots with `make_subplots`

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Scatter", "Line", "Bar", "Histogram"),
)

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 3], mode="markers"), row=1, col=1)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 4, 3], mode="lines"), row=1, col=2)
fig.add_trace(go.Bar(x=["A", "B", "C"], y=[5, 3, 7]), row=2, col=1)
fig.add_trace(go.Histogram(x=[1, 2, 2, 3, 3, 3, 4]), row=2, col=2)

fig.update_layout(height=600, width=800, title_text="Dashboard with Subplots")
fig.show()
```

> 💡 Use `specs` parameter to mix chart types (e.g., include a pie chart):
> `specs=[[{"type": "xy"}, {"type": "domain"}]]`

---

## 5. Graph Objects for Fine Control

Graph Objects (`go`) give you explicit control over every trace and layout property.

### Building a Figure from Scratch

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 4, 3, 5, 4],
    mode="lines+markers",
    name="Series A",
    line=dict(color="royalblue", width=3),
    marker=dict(size=10, symbol="diamond"),
))

fig.add_trace(go.Bar(
    x=[1, 2, 3, 4, 5],
    y=[1, 3, 2, 4, 3],
    name="Series B",
    marker_color="lightcoral",
))

fig.update_layout(
    title="Mixed Chart with Graph Objects",
    xaxis_title="X",
    yaxis_title="Value",
    barmode="overlay",
    template="plotly_white",
)
fig.show()
```

### When to Use Graph Objects vs Plotly Express

| Aspect | Plotly Express | Graph Objects |
|---|---|---|
| Lines of code | Few | Many |
| Flexibility | Convention-based | Full control |
| Multi-trace | Automatic via `color` | Manual `add_trace` |
| Best for | Exploration | Production dashboards |

---

## 6. Exporting & Sharing

### Export to HTML (Interactive)

```python
fig.write_html("chart.html")           # standalone HTML file
fig.write_html("chart.html",
               include_plotlyjs="cdn")  # smaller file, needs internet
```

### Export to Static Image

```python
fig.write_image("chart.png")           # requires kaleido
fig.write_image("chart.svg")
fig.write_image("chart.pdf", width=800, height=600)
```

> ⚠️ Static image export requires the `kaleido` package:
> `pip install -U kaleido`

### Display in Notebooks

```python
fig.show()                             # renders in Jupyter / Colab
fig.show(renderer="browser")           # opens in default browser
```

---

## Key Takeaways

- Plotly Express (`px`) creates interactive charts in a single function call
- Every `px` function returns a `go.Figure` that can be further customized
- `update_layout()` and `update_traces()` modify appearance after creation
- `make_subplots` arranges multiple charts in a grid layout
- Graph Objects (`go`) provide low-level control for complex, multi-trace figures
- `write_html()` exports fully interactive charts; `write_image()` exports static files
- Built-in templates (`plotly_white`, `plotly_dark`, etc.) provide instant theming
- Animation support via `animation_frame` enables time-series storytelling

---

## Further Reading

- [Plotly Python Documentation](https://plotly.com/python/)
- [Plotly Express API Reference](https://plotly.com/python-api-reference/plotly.express.html)
- [Graph Objects Reference](https://plotly.com/python-api-reference/plotly.graph_objects.html)
- [Plotly Built-in Datasets](https://plotly.com/python-api-reference/generated/plotly.data.html)
- [Kaleido Static Export](https://github.com/plotly/Kaleido)
- [Dash — Plotly's Dashboard Framework](https://dash.plotly.com/)
