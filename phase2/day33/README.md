# Day 33: Seaborn — Statistical Visualization

## Overview

Seaborn is a high-level statistical visualization library built on top of
Matplotlib.  It is tightly integrated with pandas DataFrames, provides
attractive default styles, and makes it easy to explore relationships in data
through distribution, categorical, relational, and regression plots.

| Capability | Key API |
|---|---|
| Distribution plots | `histplot()`, `kdeplot()`, `ecdfplot()`, `rugplot()` |
| Categorical plots | `boxplot()`, `violinplot()`, `stripplot()`, `swarmplot()`, `barplot()`, `countplot()` |
| Relational plots | `scatterplot()`, `lineplot()`, `relplot()` |
| Regression plots | `regplot()`, `lmplot()`, `residplot()` |
| Matrix plots | `heatmap()`, `clustermap()` |
| Multi-panel grids | `FacetGrid`, `PairGrid`, `pairplot()` |

---

## 1. Seaborn vs Matplotlib

Seaborn is **not** a replacement for Matplotlib — it is a complementary
layer that simplifies common statistical graphics:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn works directly with DataFrames
tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="total_bill", hue="time", kde=True)
plt.show()
```

| Feature | Matplotlib | Seaborn |
|---|---|---|
| Level | Low-level, full control | High-level, concise API |
| DataFrame support | Manual column extraction | Native `data=` parameter |
| Default aesthetics | Basic | Publication-quality defaults |
| Statistical summaries | Manual calculation | Built-in (CI, KDE, regression) |
| Themes | `plt.style.use()` | `sns.set_theme()`, `sns.set_style()` |

> 💡 Since Seaborn returns Matplotlib `Axes` objects, you can always
> fine-tune the result with Matplotlib calls afterwards.

---

## 2. Distribution Plots

Distribution plots help you understand the shape and spread of a single
variable or compare distributions across groups.

### `histplot` — histogram with optional KDE

```python
sns.histplot(data=tips, x="total_bill", kde=True, bins=30)
```

### `kdeplot` — kernel density estimate

```python
sns.kdeplot(data=tips, x="total_bill", hue="sex", fill=True, alpha=0.5)
```

### `ecdfplot` — empirical cumulative distribution

```python
sns.ecdfplot(data=tips, x="total_bill", hue="time")
```

### `rugplot` — tick marks along an axis

```python
sns.rugplot(data=tips, x="total_bill", height=0.05)
```

| Function | Purpose |
|---|---|
| `histplot()` | Histogram with optional KDE overlay |
| `kdeplot()` | Smooth density estimate curve |
| `ecdfplot()` | Cumulative distribution function |
| `rugplot()` | Marginal tick marks showing individual observations |

> 💡 Combine `histplot` with `kde=True` for a quick overview of both the
> binned counts and the smoothed density.

---

## 3. Categorical Plots

Categorical plots show the distribution or summary of a numeric variable
across different categories.

### Box and violin plots

```python
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
sns.violinplot(data=tips, x="day", y="total_bill", inner="quart", split=True)
```

### Strip and swarm plots

```python
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True, alpha=0.5)
sns.swarmplot(data=tips, x="day", y="total_bill", size=3)
```

### Bar and count plots

```python
sns.barplot(data=tips, x="day", y="total_bill", estimator="mean", errorbar="sd")
sns.countplot(data=tips, x="day", hue="sex")
```

| Function | Shows |
|---|---|
| `boxplot()` | Quartiles, median, outliers |
| `violinplot()` | KDE + box summary |
| `stripplot()` | Individual points with jitter |
| `swarmplot()` | Non-overlapping individual points |
| `barplot()` | Point estimate + error bar |
| `countplot()` | Observation counts per category |

> 💡 Overlay a `stripplot` on a `boxplot` by plotting both on the same
> `Axes` to show individual data points alongside the summary statistics.

---

## 4. Relational Plots

Relational plots visualise the relationship between two numeric variables,
optionally encoding additional dimensions with `hue`, `size`, and `style`.

### `scatterplot`

```python
penguins = sns.load_dataset("penguins")
sns.scatterplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="species", size="body_mass_g", style="sex",
)
```

### `lineplot`

```python
fmri = sns.load_dataset("fmri")
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="region", style="event")
```

### `relplot` — figure-level interface

`relplot` wraps `scatterplot` and `lineplot` and adds support for `col`
and `row` faceting:

```python
sns.relplot(
    data=tips, x="total_bill", y="tip",
    hue="smoker", col="time", kind="scatter",
)
```

> 💡 Figure-level functions (`relplot`, `catplot`, `displot`, `lmplot`)
> create their own `Figure` and return a `FacetGrid`.  Axes-level functions
> (`scatterplot`, `boxplot`, etc.) draw onto an existing `Axes`.

---

## 5. Regression Plots

Seaborn can fit and display regression models directly in a plot.

### `regplot` — axes-level regression

```python
sns.regplot(data=tips, x="total_bill", y="tip", ci=95, scatter_kws={"alpha": 0.5})
```

### `lmplot` — figure-level regression with faceting

```python
sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time")
```

### `residplot` — residuals of a linear fit

```python
sns.residplot(data=tips, x="total_bill", y="tip", lowess=True)
```

| Function | Level | Faceting | Returns |
|---|---|---|---|
| `regplot()` | Axes | No | `Axes` |
| `lmplot()` | Figure | `hue` / `col` / `row` | `FacetGrid` |
| `residplot()` | Axes | No | `Axes` |

> ⚠️ `regplot` draws on an existing `Axes` (pass `ax=`), while `lmplot`
> creates its own `Figure` — do not mix the two approaches.

---

## 6. Heatmaps & Cluster Maps

### `heatmap` — annotated colour matrix

```python
corr = tips[["total_bill", "tip", "size"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
```

| Parameter | Purpose |
|---|---|
| `annot` | Show cell values |
| `fmt` | Number format for annotations |
| `cmap` | Colour palette |
| `linewidths` | Width of cell divider lines |
| `vmin` / `vmax` | Fix colour-bar range |
| `mask` | Boolean array to hide cells (e.g. upper triangle) |

### `clustermap` — heatmap with hierarchical clustering

```python
iris = sns.load_dataset("iris")
numeric = iris.drop(columns="species")
sns.clustermap(numeric, cmap="viridis", standard_scale=1, figsize=(8, 8))
```

`clustermap` reorders rows and columns by similarity and draws dendrograms
along the margins.

---

## 7. FacetGrid & PairGrid

### `FacetGrid` — multi-panel layout by variable

```python
g = sns.FacetGrid(tips, col="time", row="smoker", hue="sex", height=4)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.add_legend()
```

### `PairGrid` & `pairplot` — all pairwise relationships

```python
g = sns.pairplot(
    penguins, hue="species",
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"],
    diag_kind="kde",
)
```

`PairGrid` gives you lower-level control:

```python
g = sns.PairGrid(penguins, hue="species",
                 vars=["bill_length_mm", "bill_depth_mm"])
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot, fill=True, alpha=0.4)
g.map_diag(sns.histplot)
g.add_legend()
```

> 💡 `pairplot()` is the quick convenience wrapper; use `PairGrid` when
> you need different plot types in the upper, lower, and diagonal panels.

---

## Key Takeaways

- **Seaborn** is a high-level statistical visualization library that works directly with pandas DataFrames and builds on Matplotlib.
- **Distribution plots** (`histplot`, `kdeplot`, `ecdfplot`) reveal the shape, centre, and spread of a variable.
- **Categorical plots** (`boxplot`, `violinplot`, `stripplot`, `barplot`) compare distributions across groups.
- **Relational plots** (`scatterplot`, `lineplot`) show pairwise relationships and support `hue` / `size` / `style` encoding.
- **Regression plots** (`regplot`, `lmplot`, `residplot`) overlay fitted models with confidence intervals.
- **`heatmap()`** and **`clustermap()`** visualise matrices such as correlation tables and pivot tables.
- **`FacetGrid`** and **`pairplot()`** automate multi-panel layouts for exploring multivariate data.

## Further Reading

- [Seaborn Official Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Seaborn API Reference](https://seaborn.pydata.org/api.html)
- [Seaborn — Choosing Colour Palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)
- [Seaborn — Controlling Figure Aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
- [Seaborn — Multi-Plot Grids](https://seaborn.pydata.org/tutorial/axis_grids.html)
