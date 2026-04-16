# Day 31: Matplotlib — Fundamentals

## Overview

Matplotlib is the foundational plotting library in Python's data-science
stack.  Nearly every other visualization library (Seaborn, Pandas `.plot()`,
plotnine) is built on top of it.  Understanding Matplotlib's core concepts
gives you precise control over every pixel in your figures.

| Capability | Key API |
|---|---|
| Figure & Axes creation | `plt.subplots()`, `fig.add_subplot()` |
| Line plots | `ax.plot()` |
| Bar charts | `ax.bar()`, `ax.barh()` |
| Scatter plots | `ax.scatter()` |
| Histograms | `ax.hist()` |
| Box plots | `ax.boxplot()` |
| Customization | `ax.set_title()`, `ax.legend()`, `plt.style.use()` |

---

## 1. The Matplotlib Architecture

Matplotlib follows a layered, object-oriented design with three key levels:

| Layer | Object | Role |
|---|---|---|
| **Container** | `Figure` | Top-level window / canvas that holds everything |
| **Plotting area** | `Axes` | A single plot (coordinates, ticks, labels) |
| **Primitives** | `Artist` | Lines, text, patches — everything drawn on screen |

The recommended entry point is `plt.subplots()`, which returns both a
`Figure` and one or more `Axes` at once:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()          # one Axes
fig, axes = plt.subplots(2, 2)    # 2×2 grid → axes is a 2-D array
```

> 💡 **Tip:** Prefer the **OO interface** (`fig, ax = plt.subplots()`) over
> the pyplot state-machine (`plt.plot()`) for anything beyond quick one-liners.
> It is explicit, composable, and avoids "current Axes" surprises.

---

## 2. Line Plots

`ax.plot()` draws connected data points — ideal for time series and
continuous relationships:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)", color="steelblue", linewidth=2)
ax.plot(x, np.cos(x), label="cos(x)", color="coral", linestyle="--")
ax.set_title("Trigonometric Functions")
ax.set_xlabel("x (radians)")
ax.set_ylabel("Amplitude")
ax.legend()
plt.show()
```

Common `plot()` parameters:

| Parameter | Example | Purpose |
|---|---|---|
| `color` | `"steelblue"`, `"#FF5733"` | Line colour |
| `linewidth` / `lw` | `2` | Line thickness |
| `linestyle` / `ls` | `"--"`, `"-."`, `":"` | Dash pattern |
| `marker` | `"o"`, `"s"`, `"^"` | Data-point marker |
| `label` | `"sin(x)"` | Legend entry |

---

## 3. Bar Charts

Use `ax.bar()` for vertical bars and `ax.barh()` for horizontal bars:

```python
categories = ["Python", "R", "Julia", "MATLAB"]
values = [85, 55, 30, 40]

fig, ax = plt.subplots()
ax.bar(categories, values, color=["#306998", "#276DC3", "#9558B2", "#EF6C00"])
ax.set_ylabel("Popularity Score")
ax.set_title("Language Popularity")
plt.show()
```

### Grouped bars

Place bars side-by-side by offsetting x positions:

```python
import numpy as np

labels = ["Q1", "Q2", "Q3", "Q4"]
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width / 2, product_a, width, label="Product A")
ax.bar(x + width / 2, product_b, width, label="Product B")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()
```

---

## 4. Scatter Plots

`ax.scatter()` maps individual observations as points and optionally encodes
extra dimensions via size and colour:

```python
rng = np.random.default_rng(42)
x = rng.normal(size=200)
y = 2 * x + rng.normal(scale=0.5, size=200)
colors = rng.uniform(size=200)
sizes = rng.uniform(20, 200, size=200)

fig, ax = plt.subplots()
sc = ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap="viridis")
fig.colorbar(sc, ax=ax, label="Colour value")
ax.set_title("Scatter with Colour & Size Mapping")
plt.show()
```

| Parameter | Purpose |
|---|---|
| `c` | Colour value per point (scalar array → colourmap) |
| `s` | Size per point (in points²) |
| `cmap` | Colourmap name, e.g. `"viridis"`, `"plasma"` |
| `alpha` | Transparency (0–1) |

---

## 5. Histograms & Box Plots

### Histograms

`ax.hist()` bins continuous data and shows its distribution:

```python
data = rng.normal(loc=50, scale=10, size=1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor="black", alpha=0.7)
ax.set_title("Normal Distribution")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
plt.show()
```

| Parameter | Purpose |
|---|---|
| `bins` | Number of bins or bin-edge array |
| `density` | If `True`, area sums to 1 (probability density) |
| `edgecolor` | Colour of bin borders |
| `histtype` | `"bar"`, `"step"`, `"stepfilled"` |

### Box Plots

`ax.boxplot()` summarises distributions via quartiles and outliers:

```python
groups = [rng.normal(50, 10, 100), rng.normal(60, 15, 100), rng.normal(55, 5, 100)]

fig, ax = plt.subplots()
ax.boxplot(groups, tick_labels=["A", "B", "C"])
ax.set_title("Box Plot Comparison")
ax.set_ylabel("Value")
plt.show()
```

---

## 6. Customization

### Titles, Labels & Legends

```python
ax.set_title("Title", fontsize=14, fontweight="bold")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.legend(loc="upper right", frameon=False)
```

### Grids & Ticks

```python
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr"], rotation=45)
ax.tick_params(axis="both", labelsize=10)
```

### Built-in Styles

Matplotlib ships with many pre-defined styles:

```python
import matplotlib.pyplot as plt

print(plt.style.available)          # list all styles
plt.style.use("seaborn-v0_8-whitegrid")  # apply a style
```

Popular choices: `"ggplot"`, `"seaborn-v0_8-whitegrid"`, `"fivethirtyeight"`,
`"bmh"`, `"dark_background"`.

### Tight Layout

Prevent labels from overlapping or being clipped:

```python
fig.tight_layout()
```

---

## Key Takeaways

- **`Figure`** is the top-level container; **`Axes`** is an individual plot inside it.
- Use the **OO interface** (`fig, ax = plt.subplots()`) for clarity and composability.
- **`ax.plot()`**, **`ax.bar()`**, **`ax.scatter()`**, **`ax.hist()`**, and **`ax.boxplot()`** cover the most common plot types.
- Encode extra dimensions with **colour**, **size**, and **marker** parameters.
- **`ax.set_title()`**, **`ax.legend()`**, **`ax.grid()`**, and **`plt.style.use()`** handle visual polish.
- Always call **`fig.tight_layout()`** before saving to avoid clipped labels.

## Further Reading

- [Matplotlib — Quick Start Guide](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Matplotlib — Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Matplotlib — Artist Tutorial](https://matplotlib.org/stable/tutorials/intermediate/artists.html)
- [Matplotlib — Plot Types Gallery](https://matplotlib.org/stable/plot_types/index.html)
- [Real Python — Python Plotting With Matplotlib](https://realpython.com/python-matplotlib-guide/)
