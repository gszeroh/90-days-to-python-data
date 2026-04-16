"""Day 32: Matplotlib — Advanced Visualizations — Examples"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# === 1. Subplots & Layouts ===

print("--- Basic 2×2 grid ---")
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
for i, ax in enumerate(axes.flat):
    ax.set_title(f"Subplot {i + 1}")
    ax.plot(np.random.default_rng(i).normal(size=30))
fig.tight_layout()
fig.savefig("subplots_grid.png", dpi=100)
print("Saved subplots_grid.png — 2×2 grid of random line plots")
plt.close(fig)

print("\n--- GridSpec: 1 wide + 2 narrow ---")
fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

ax_top = fig.add_subplot(gs[0, :])
ax_bl = fig.add_subplot(gs[1, 0])
ax_br = fig.add_subplot(gs[1, 1])

x = np.linspace(0, 4 * np.pi, 200)
ax_top.plot(x, np.sin(x), color="steelblue")
ax_top.set_title("Full-Width Sine Wave")

ax_bl.bar(["A", "B", "C"], [3, 7, 5], color="coral")
ax_bl.set_title("Bar Chart")

ax_br.scatter(*np.random.default_rng(0).normal(size=(2, 50)), alpha=0.6)
ax_br.set_title("Scatter")

fig.savefig("gridspec_layout.png", dpi=100)
print("Saved gridspec_layout.png — GridSpec with spanning top plot")
plt.close(fig)

print("\n--- Constrained layout ---")
fig, axes = plt.subplots(1, 3, figsize=(12, 4), layout="constrained")
for ax, style in zip(axes, ["o-", "s--", "^:"]):
    ax.plot(np.arange(10), np.random.default_rng(42).integers(1, 10, 10), style)
    ax.set_xlabel("X axis label")
    ax.set_ylabel("Y axis label")
    ax.set_title("Constrained")
fig.savefig("constrained_layout.png", dpi=100)
print("Saved constrained_layout.png — automatic spacing with constrained layout")
plt.close(fig)

# === 2. Annotations & Text ===

print("\n--- Annotating min and max ---")
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) * np.exp(-0.1 * x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color="steelblue", linewidth=2)

i_max = np.argmax(y)
i_min = np.argmin(y)

ax.annotate(
    f"Max ({x[i_max]:.2f}, {y[i_max]:.2f})",
    xy=(x[i_max], y[i_max]),
    xytext=(x[i_max] + 1, y[i_max] + 0.15),
    arrowprops=dict(arrowstyle="->", color="green", lw=1.5),
    fontsize=10, color="green",
)
ax.annotate(
    f"Min ({x[i_min]:.2f}, {y[i_min]:.2f})",
    xy=(x[i_min], y[i_min]),
    xytext=(x[i_min] + 1, y[i_min] - 0.15),
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
    fontsize=10, color="red",
)

ax.set_title("Damped Sine — Annotated Min/Max")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()
fig.savefig("annotations.png", dpi=100)
print("Saved annotations.png — line plot with min/max annotations")
plt.close(fig)

print("\n--- Text box ---")
fig, ax = plt.subplots()
rng = np.random.default_rng(7)
data = rng.normal(50, 10, 200)
ax.hist(data, bins=20, edgecolor="black", alpha=0.7)
ax.text(
    0.95, 0.95,
    f"μ = {data.mean():.1f}\nσ = {data.std():.1f}",
    transform=ax.transAxes, ha="right", va="top", fontsize=11,
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
)
ax.set_title("Histogram with Statistics Text Box")
fig.tight_layout()
fig.savefig("text_box.png", dpi=100)
print("Saved text_box.png — histogram with μ/σ text overlay")
plt.close(fig)

# === 3. Styles & Themes ===

print("\n--- Style gallery (4 styles) ---")
styles = ["ggplot", "bmh", "fivethirtyeight", "dark_background"]
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
x = np.linspace(0, 2 * np.pi, 100)

for ax, style_name in zip(axes.flat, styles):
    with plt.style.context(style_name):
        temp_fig, temp_ax = plt.subplots()
        temp_ax.plot(x, np.sin(x))
        plt.close(temp_fig)
    # Demonstrate by just labelling
    ax.plot(x, np.sin(x), linewidth=2)
    ax.set_title(f'Style: "{style_name}"')

fig.tight_layout()
fig.savefig("style_gallery.png", dpi=100)
print("Saved style_gallery.png — four built-in style previews")
plt.close(fig)

print("\n--- rcParams customization ---")
original_fontsize = matplotlib.rcParams["font.size"]
matplotlib.rcParams["font.size"] = 14
matplotlib.rcParams["axes.grid"] = True

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], "o-", color="teal")
ax.set_title("rcParams: larger font + grid")
fig.tight_layout()
fig.savefig("rcparams_demo.png", dpi=100)
print("Saved rcparams_demo.png — custom rcParams font size and grid")
plt.close(fig)

matplotlib.rcParams["font.size"] = original_fontsize
matplotlib.rcParams["axes.grid"] = False

# === 4. Pie Charts & Donut Charts ===

print("\n--- Pie chart ---")
labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 10, 10]
explode = (0.05, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
       explode=explode, colors=plt.cm.Set2.colors[:5])
ax.set_title("Language Market Share")
fig.tight_layout()
fig.savefig("pie_chart.png", dpi=100)
print("Saved pie_chart.png — exploded pie chart with percentages")
plt.close(fig)

print("\n--- Donut chart ---")
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
       wedgeprops=dict(width=0.4), colors=plt.cm.Pastel1.colors[:5])
ax.set_title("Language Share (Donut)")
fig.tight_layout()
fig.savefig("donut_chart.png", dpi=100)
print("Saved donut_chart.png — donut chart with wedgeprops width")
plt.close(fig)

# === 5. Heatmaps with imshow ===

print("\n--- Heatmap ---")
rng = np.random.default_rng(42)
data = rng.random((6, 8))
row_labels = [f"Row {i}" for i in range(6)]
col_labels = [f"Col {j}" for j in range(8)]

fig, ax = plt.subplots(figsize=(8, 5))
im = ax.imshow(data, cmap="YlOrRd", aspect="auto")
fig.colorbar(im, ax=ax, label="Value")
ax.set_xticks(range(len(col_labels)))
ax.set_xticklabels(col_labels, rotation=45, ha="right")
ax.set_yticks(range(len(row_labels)))
ax.set_yticklabels(row_labels)
ax.set_title("Heatmap with imshow")
fig.tight_layout()
fig.savefig("heatmap.png", dpi=100)
print("Saved heatmap.png — 6×8 random heatmap with colour bar")
plt.close(fig)

print("\n--- Heatmap with cell values ---")
small = rng.integers(0, 100, (4, 4))
fig, ax = plt.subplots()
im = ax.imshow(small, cmap="Blues")
fig.colorbar(im, ax=ax)
for i in range(small.shape[0]):
    for j in range(small.shape[1]):
        ax.text(j, i, str(small[i, j]), ha="center", va="center", fontsize=12)
ax.set_title("Heatmap with Cell Values")
fig.tight_layout()
fig.savefig("heatmap_values.png", dpi=100)
print("Saved heatmap_values.png — 4×4 heatmap with numeric labels")
plt.close(fig)

# === 6. 3-D Plots ===

print("\n--- 3-D surface plot ---")
X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none", alpha=0.9)
ax.set_title("3-D Surface: sin(√(x²+y²))")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
fig.tight_layout()
fig.savefig("surface_3d.png", dpi=100)
print("Saved surface_3d.png — 3-D surface plot with viridis colourmap")
plt.close(fig)

print("\n--- 3-D wireframe plot ---")
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color="steelblue")
ax.set_title("3-D Wireframe")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.view_init(elev=30, azim=45)
fig.tight_layout()
fig.savefig("wireframe_3d.png", dpi=100)
print("Saved wireframe_3d.png — wireframe with custom camera angle")
plt.close(fig)
