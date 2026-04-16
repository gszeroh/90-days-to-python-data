# Day 32: Matplotlib — Advanced Visualizations

## Overview

Building on Matplotlib fundamentals, this lesson explores advanced
visualization techniques that help you create publication-quality figures.
You will learn how to arrange multiple plots with flexible layouts, annotate
key data points, apply consistent styles, and even venture into 3-D plotting.

| Capability | Key API |
|---|---|
| Subplots & layouts | `plt.subplots()`, `GridSpec`, `constrained_layout` |
| Annotations & text | `ax.annotate()`, `ax.text()` |
| Styles & themes | `plt.style.use()`, `mpl.rcParams` |
| Pie / donut charts | `ax.pie()` |
| Heatmaps | `ax.imshow()`, `fig.colorbar()` |
| 3-D plots | `Axes3D`, `plot_surface()`, `plot_wireframe()` |

---

## 1. Subplots & Layouts

### Basic grid with `plt.subplots()`

```python
fig, axes = plt.subplots(2, 3, figsize=(12, 6))
```

### Flexible grids with `GridSpec`

`GridSpec` lets you create non-uniform grids where individual plots span
multiple rows or columns:

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 2, figure=fig)

ax_top = fig.add_subplot(gs[0, :])    # top row, full width
ax_bl  = fig.add_subplot(gs[1, 0])    # bottom-left
ax_br  = fig.add_subplot(gs[1, 1])    # bottom-right
```

| Parameter | Purpose |
|---|---|
| `nrows`, `ncols` | Grid dimensions |
| `width_ratios` | Relative column widths |
| `height_ratios` | Relative row heights |
| `hspace`, `wspace` | Vertical / horizontal spacing |

### Constrained layout

Use `constrained_layout=True` (or `layout="constrained"`) for automatic
spacing that prevents overlapping labels — a modern alternative to
`tight_layout()`:

```python
fig, axes = plt.subplots(2, 2, layout="constrained")
```

---

## 2. Annotations & Text

### `ax.annotate()`

Draw an arrow from a text label to a data point:

```python
ax.annotate(
    "Peak",
    xy=(x_peak, y_peak),            # point to annotate
    xytext=(x_peak + 1, y_peak + 5),  # text position
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=12,
    color="red",
)
```

| `arrowprops` key | Example values | Purpose |
|---|---|---|
| `arrowstyle` | `"->"`, `"fancy"`, `"wedge"` | Arrow head shape |
| `color` | `"red"`, `"#333333"` | Arrow colour |
| `lw` | `1.5` | Arrow line width |
| `connectionstyle` | `"arc3,rad=0.3"` | Curved arrow |

### `ax.text()`

Place text at arbitrary data coordinates:

```python
ax.text(0.5, 0.95, "R² = 0.98", transform=ax.transAxes,
        ha="center", va="top", fontsize=12,
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))
```

---

## 3. Styles & Themes

### Built-in styles

```python
plt.style.use("ggplot")          # apply globally
```

Popular styles: `"ggplot"`, `"seaborn-v0_8-whitegrid"`, `"fivethirtyeight"`,
`"bmh"`, `"dark_background"`, `"tableau-colorblind10"`.

### Temporary style context

```python
with plt.style.context("dark_background"):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
```

### `rcParams` customization

Fine-tune individual settings without switching styles:

```python
import matplotlib as mpl

mpl.rcParams["font.size"] = 14
mpl.rcParams["axes.grid"] = True
mpl.rcParams["figure.dpi"] = 120
```

---

## 4. Pie Charts & Donut Charts

### Pie chart

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.set_title("Market Share")
```

| Parameter | Purpose |
|---|---|
| `autopct` | Format string for percentage labels |
| `startangle` | Rotation of the first slice (degrees) |
| `explode` | Tuple of offsets to "explode" slices outward |
| `colors` | Custom colour list for slices |

### Donut chart

A donut chart is simply a pie chart with a white circle in the centre:

```python
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
       wedgeprops=dict(width=0.4))
```

---

## 5. Heatmaps with `imshow`

`ax.imshow()` displays a 2-D array as a colour-mapped image — perfect for
correlation matrices, confusion matrices, and grid data:

```python
fig, ax = plt.subplots()
im = ax.imshow(data, cmap="YlOrRd", aspect="auto")
fig.colorbar(im, ax=ax)
ax.set_xticks(range(len(col_labels)))
ax.set_xticklabels(col_labels)
ax.set_yticks(range(len(row_labels)))
ax.set_yticklabels(row_labels)
```

To overlay values on each cell:

```python
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        ax.text(j, i, f"{data[i, j]:.2f}", ha="center", va="center")
```

---

## 6. 3-D Plots

Matplotlib supports basic 3-D visualisation via the `mpl_toolkits.mplot3d`
module.  Request a 3-D Axes with the `projection="3d"` keyword:

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
```

### Surface plot

```python
X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
ax.set_title("Surface Plot")
```

### Wireframe plot

```python
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color="steelblue")
```

| Method | Purpose |
|---|---|
| `plot_surface()` | Filled 3-D surface with optional colourmap |
| `plot_wireframe()` | Wireframe mesh |
| `scatter()` (3-D) | 3-D scatter points |
| `view_init(elev, azim)` | Set camera angle |

---

## Key Takeaways

- **`GridSpec`** provides flexible subplot layouts where plots can span multiple rows or columns.
- **`ax.annotate()`** draws labelled arrows pointing at key data features — invaluable for storytelling.
- **`plt.style.use()`** and **`rcParams`** give you consistent, publication-ready themes in one line.
- **Pie / donut charts** are created with `ax.pie()`; use `wedgeprops=dict(width=…)` for donuts.
- **`ax.imshow()`** turns any 2-D array into a heatmap; add a `colorbar()` and cell text for clarity.
- **3-D plots** require `projection="3d"` and live in `mpl_toolkits.mplot3d`.

## Further Reading

- [Matplotlib — Arranging Multiple Axes](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)
- [Matplotlib — Annotations](https://matplotlib.org/stable/tutorials/text/annotations.html)
- [Matplotlib — Customizing Styles](https://matplotlib.org/stable/users/explain/customizing.html)
- [Matplotlib — Pie and Polar Charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/index.html)
- [Matplotlib — 3D Plotting](https://matplotlib.org/stable/gallery/mplot3d/index.html)
