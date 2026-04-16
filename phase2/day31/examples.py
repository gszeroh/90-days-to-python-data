"""Day 31: Matplotlib — Fundamentals — Examples"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# === 1. The Matplotlib Architecture ===

print("--- Figure & Axes creation ---")
fig, ax = plt.subplots()
print(f"Figure: {type(fig)}")
print(f"Axes:   {type(ax)}")
plt.close(fig)

fig, axes = plt.subplots(2, 2)
print(f"2×2 grid shape: {axes.shape}")
plt.close(fig)

# === 2. Line Plots ===

print("\n--- Line plot: trig functions ---")
x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)", color="steelblue", linewidth=2)
ax.plot(x, np.cos(x), label="cos(x)", color="coral", linestyle="--")
ax.set_title("Trigonometric Functions")
ax.set_xlabel("x (radians)")
ax.set_ylabel("Amplitude")
ax.legend()
fig.tight_layout()
fig.savefig("line_plot.png", dpi=100)
print("Saved line_plot.png — sin and cos curves with legend")
plt.close(fig)

print("\n--- Line plot with markers ---")
x_small = np.arange(0, 10)
fig, ax = plt.subplots()
ax.plot(x_small, x_small ** 2, marker="o", color="#E74C3C", label="x²")
ax.plot(x_small, x_small ** 1.5, marker="s", color="#2ECC71", label="x^1.5")
ax.set_title("Markers Demo")
ax.legend()
fig.tight_layout()
fig.savefig("line_markers.png", dpi=100)
print("Saved line_markers.png — lines with circle and square markers")
plt.close(fig)

# === 3. Bar Charts ===

print("\n--- Vertical bar chart ---")
categories = ["Python", "R", "Julia", "MATLAB"]
values = [85, 55, 30, 40]

fig, ax = plt.subplots()
ax.bar(categories, values, color=["#306998", "#276DC3", "#9558B2", "#EF6C00"])
ax.set_ylabel("Popularity Score")
ax.set_title("Language Popularity")
fig.tight_layout()
fig.savefig("bar_chart.png", dpi=100)
print("Saved bar_chart.png — four languages, different colours")
plt.close(fig)

print("\n--- Grouped bar chart ---")
labels = ["Q1", "Q2", "Q3", "Q4"]
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width / 2, product_a, width, label="Product A", color="steelblue")
ax.bar(x + width / 2, product_b, width, label="Product B", color="coral")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_title("Quarterly Revenue by Product")
ax.legend()
fig.tight_layout()
fig.savefig("grouped_bar.png", dpi=100)
print("Saved grouped_bar.png — side-by-side bars for two products")
plt.close(fig)

print("\n--- Horizontal bar chart ---")
fig, ax = plt.subplots()
ax.barh(categories, values, color="teal")
ax.set_xlabel("Popularity Score")
ax.set_title("Language Popularity (Horizontal)")
fig.tight_layout()
fig.savefig("barh_chart.png", dpi=100)
print("Saved barh_chart.png — horizontal bars")
plt.close(fig)

# === 4. Scatter Plots ===

print("\n--- Scatter plot with colour & size ---")
rng = np.random.default_rng(42)
x_scatter = rng.normal(size=200)
y_scatter = 2 * x_scatter + rng.normal(scale=0.5, size=200)
colors = rng.uniform(size=200)
sizes = rng.uniform(20, 200, size=200)

fig, ax = plt.subplots()
sc = ax.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6,
                cmap="viridis")
fig.colorbar(sc, ax=ax, label="Colour value")
ax.set_title("Scatter with Colour & Size Mapping")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()
fig.savefig("scatter_plot.png", dpi=100)
print("Saved scatter_plot.png — 200 points, viridis colourmap, variable size")
plt.close(fig)

# === 5. Histograms & Box Plots ===

print("\n--- Histogram ---")
data = rng.normal(loc=50, scale=10, size=1000)

fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor="black", alpha=0.7, color="mediumpurple")
ax.set_title("Normal Distribution (μ=50, σ=10)")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
fig.tight_layout()
fig.savefig("histogram.png", dpi=100)
print("Saved histogram.png — 1000 samples, 30 bins")
plt.close(fig)

print("\n--- Box plot ---")
groups = [rng.normal(50, 10, 100),
          rng.normal(60, 15, 100),
          rng.normal(55, 5, 100)]

fig, ax = plt.subplots()
ax.boxplot(groups, tick_labels=["A", "B", "C"])
ax.set_title("Box Plot Comparison")
ax.set_ylabel("Value")
fig.tight_layout()
fig.savefig("boxplot.png", dpi=100)
print("Saved boxplot.png — three groups with different spread")
plt.close(fig)

# === 6. Customization ===

print("\n--- Customization showcase ---")
x = np.linspace(0, 10, 50)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, np.sin(x), "o-", label="sin(x)", markersize=4)
ax.plot(x, np.cos(x), "s--", label="cos(x)", markersize=4)

ax.set_title("Customization Demo", fontsize=14, fontweight="bold")
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("f(x)", fontsize=12)
ax.legend(loc="upper right", frameon=False)
ax.grid(True, linestyle="--", alpha=0.5)
ax.tick_params(axis="both", labelsize=10)

fig.tight_layout()
fig.savefig("customization.png", dpi=100)
print("Saved customization.png — styled with grid, legend, bold title")
plt.close(fig)

print("\n--- Available styles (first 10) ---")
print(plt.style.available[:10])
