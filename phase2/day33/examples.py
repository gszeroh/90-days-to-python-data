"""Day 33: Seaborn — Statistical Visualization — Examples"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# === 1. Seaborn vs Matplotlib ===

print("--- Seaborn defaults & theme ---")
sns.set_theme(style="whitegrid", palette="muted")
tips = sns.load_dataset("tips")
print(f"Loaded 'tips' dataset: {tips.shape[0]} rows, {tips.shape[1]} columns")
print(tips.head(3).to_string())

# === 2. Distribution Plots ===

print("\n--- histplot with KDE ---")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data=tips, x="total_bill", kde=True, bins=30, ax=ax)
ax.set_title("Distribution of Total Bill")
fig.tight_layout()
fig.savefig("dist_histplot.png", dpi=100)
print("Saved dist_histplot.png — histogram with KDE overlay")
plt.close(fig)

print("\n--- kdeplot by group ---")
fig, ax = plt.subplots(figsize=(8, 4))
sns.kdeplot(data=tips, x="total_bill", hue="sex", fill=True, alpha=0.4, ax=ax)
ax.set_title("Total Bill KDE by Sex")
fig.tight_layout()
fig.savefig("dist_kdeplot.png", dpi=100)
print("Saved dist_kdeplot.png — overlapping KDE curves by sex")
plt.close(fig)

print("\n--- ecdfplot ---")
fig, ax = plt.subplots(figsize=(8, 4))
sns.ecdfplot(data=tips, x="total_bill", hue="time", ax=ax)
ax.set_title("ECDF of Total Bill by Meal Time")
fig.tight_layout()
fig.savefig("dist_ecdfplot.png", dpi=100)
print("Saved dist_ecdfplot.png — empirical CDF by time")
plt.close(fig)

print("\n--- rugplot combined with kdeplot ---")
fig, ax = plt.subplots(figsize=(8, 4))
sns.kdeplot(data=tips, x="tip", fill=True, alpha=0.3, ax=ax)
sns.rugplot(data=tips, x="tip", height=0.05, ax=ax)
ax.set_title("Tip Distribution — KDE + Rug")
fig.tight_layout()
fig.savefig("dist_rugplot.png", dpi=100)
print("Saved dist_rugplot.png — KDE with rug marks")
plt.close(fig)

# === 3. Categorical Plots ===

print("\n--- boxplot ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex", ax=ax)
ax.set_title("Total Bill by Day (Box Plot)")
fig.tight_layout()
fig.savefig("cat_boxplot.png", dpi=100)
print("Saved cat_boxplot.png — grouped box plots by day and sex")
plt.close(fig)

print("\n--- violinplot ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", inner="quart", ax=ax)
ax.set_title("Total Bill by Day (Violin Plot)")
fig.tight_layout()
fig.savefig("cat_violinplot.png", dpi=100)
print("Saved cat_violinplot.png — violin plots with quartile lines")
plt.close(fig)

print("\n--- boxplot + stripplot overlay ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill", whis=1.5, ax=ax)
sns.stripplot(data=tips, x="day", y="total_bill", color="black",
              alpha=0.3, size=3, ax=ax)
ax.set_title("Box + Strip Overlay")
fig.tight_layout()
fig.savefig("cat_box_strip.png", dpi=100)
print("Saved cat_box_strip.png — box plot with individual observations")
plt.close(fig)

print("\n--- barplot with error bars ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill", estimator="mean",
            errorbar="sd", ax=ax)
ax.set_title("Mean Total Bill by Day (± SD)")
fig.tight_layout()
fig.savefig("cat_barplot.png", dpi=100)
print("Saved cat_barplot.png — bar plot with standard deviation")
plt.close(fig)

print("\n--- countplot ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=tips, x="day", hue="sex", ax=ax)
ax.set_title("Observation Count by Day")
fig.tight_layout()
fig.savefig("cat_countplot.png", dpi=100)
print("Saved cat_countplot.png — count plot by day and sex")
plt.close(fig)

# === 4. Relational Plots ===

print("\n--- scatterplot with hue, size, style ---")
penguins = sns.load_dataset("penguins").dropna()
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="species", size="body_mass_g", style="sex",
    alpha=0.7, ax=ax,
)
ax.set_title("Penguin Bill Dimensions")
fig.tight_layout()
fig.savefig("rel_scatterplot.png", dpi=100)
print("Saved rel_scatterplot.png — multi-dimensional scatter plot")
plt.close(fig)

print("\n--- lineplot ---")
fmri = sns.load_dataset("fmri")
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(data=fmri, x="timepoint", y="signal",
             hue="region", style="event", ax=ax)
ax.set_title("fMRI Signal over Time")
fig.tight_layout()
fig.savefig("rel_lineplot.png", dpi=100)
print("Saved rel_lineplot.png — grouped line plot with confidence band")
plt.close(fig)

print("\n--- relplot (figure-level with facets) ---")
g = sns.relplot(
    data=tips, x="total_bill", y="tip",
    hue="smoker", col="time", kind="scatter", height=4,
)
g.fig.suptitle("Tip vs Total Bill by Time", y=1.02)
g.savefig("rel_relplot.png", dpi=100)
print("Saved rel_relplot.png — faceted scatter plot (Lunch vs Dinner)")
plt.close(g.fig)

# === 5. Regression Plots ===

print("\n--- regplot ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.regplot(data=tips, x="total_bill", y="tip", ci=95,
            scatter_kws={"alpha": 0.5}, ax=ax)
ax.set_title("Tip vs Total Bill — Linear Regression (95% CI)")
fig.tight_layout()
fig.savefig("reg_regplot.png", dpi=100)
print("Saved reg_regplot.png — regression line with confidence interval")
plt.close(fig)

print("\n--- lmplot with hue and col ---")
g = sns.lmplot(data=tips, x="total_bill", y="tip",
               hue="smoker", col="time", height=4)
g.fig.suptitle("Linear Model by Smoker & Time", y=1.02)
g.savefig("reg_lmplot.png", dpi=100)
print("Saved reg_lmplot.png — faceted regression plot")
plt.close(g.fig)

print("\n--- residplot ---")
fig, ax = plt.subplots(figsize=(8, 5))
sns.residplot(data=tips, x="total_bill", y="tip", ax=ax)
ax.set_title("Residual Plot — Total Bill vs Tip")
fig.tight_layout()
fig.savefig("reg_residplot.png", dpi=100)
print("Saved reg_residplot.png — residuals of linear fit")
plt.close(fig)

# === 6. Heatmaps & Cluster Maps ===

print("\n--- correlation heatmap ---")
corr = tips[["total_bill", "tip", "size"]].corr()
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, ax=ax)
ax.set_title("Correlation Heatmap")
fig.tight_layout()
fig.savefig("heatmap_corr.png", dpi=100)
print("Saved heatmap_corr.png — annotated correlation matrix")
plt.close(fig)

print("\n--- masked upper triangle ---")
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="vlag", mask=mask,
            linewidths=0.5, ax=ax)
ax.set_title("Lower-Triangle Correlation Heatmap")
fig.tight_layout()
fig.savefig("heatmap_masked.png", dpi=100)
print("Saved heatmap_masked.png — lower-triangle heatmap")
plt.close(fig)

print("\n--- clustermap ---")
iris = sns.load_dataset("iris")
numeric = iris.drop(columns="species")
g = sns.clustermap(numeric, cmap="viridis", standard_scale=1, figsize=(8, 8))
g.fig.suptitle("Iris Cluster Map", y=1.02)
g.savefig("clustermap_iris.png", dpi=100)
print("Saved clustermap_iris.png — clustered heatmap with dendrograms")
plt.close(g.fig)

# === 7. FacetGrid & PairGrid ===

print("\n--- FacetGrid ---")
g = sns.FacetGrid(tips, col="time", row="smoker", hue="sex", height=3.5)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.add_legend()
g.fig.suptitle("FacetGrid: Tip vs Total Bill", y=1.02)
g.savefig("facetgrid.png", dpi=100)
print("Saved facetgrid.png — 2×2 faceted scatter grid")
plt.close(g.fig)

print("\n--- pairplot ---")
g = sns.pairplot(
    penguins, hue="species",
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"],
    diag_kind="kde",
)
g.fig.suptitle("Penguin Pair Plot", y=1.02)
g.savefig("pairplot_penguins.png", dpi=100)
print("Saved pairplot_penguins.png — pairwise relationship grid")
plt.close(g.fig)

print("\n--- PairGrid with custom panels ---")
g = sns.PairGrid(penguins, hue="species",
                 vars=["bill_length_mm", "bill_depth_mm"])
g.map_upper(sns.scatterplot, alpha=0.6)
g.map_lower(sns.kdeplot, fill=True, alpha=0.3)
g.map_diag(sns.histplot, kde=True)
g.add_legend()
g.fig.suptitle("Custom PairGrid", y=1.02)
g.savefig("pairgrid_custom.png", dpi=100)
print("Saved pairgrid_custom.png — PairGrid with scatter/KDE/hist")
plt.close(g.fig)

print("\nAll examples completed.")
