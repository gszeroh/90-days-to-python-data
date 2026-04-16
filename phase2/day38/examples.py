"""Day 38: Statistics — Correlation & Regression Basics — Examples"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# === 1. Covariance ===

print("--- 1. Covariance ---")
np.random.seed(38)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2.1, 4.0, 5.2, 4.8, 7.1, 7.8, 8.5, 9.0, 10.3, 11.5])

# Sample covariance matrix (ddof=1 by default)
cov_matrix = np.cov(x, y)
print(f"Covariance matrix:\n{cov_matrix}")
print(f"Cov(x, y) = {cov_matrix[0, 1]:.4f}")

# Population covariance — set ddof=0
cov_pop = np.cov(x, y, ddof=0)
print(f"Population Cov(x, y) = {cov_pop[0, 1]:.4f}")

# Limitation: scale-dependent
y_cm = y * 100  # convert units
print(f"Cov(x, y_cm) = {np.cov(x, y_cm)[0, 1]:.4f}  (100× larger)")

# === 2. Pearson Correlation Coefficient ===

print("\n--- 2. Pearson Correlation Coefficient ---")

r, p_value = stats.pearsonr(x, y)
print(f"Pearson r = {r:.4f}")
print(f"p-value   = {p_value:.6f}")
print(f"Interpretation: {'Strong' if abs(r) >= 0.6 else 'Moderate'} "
      f"{'positive' if r > 0 else 'negative'} linear relationship")

# Pearson with outlier — sensitivity demonstration
y_outlier = y.copy()
y_outlier[4] = 50  # inject an outlier
r_outlier, _ = stats.pearsonr(x, y_outlier)
print(f"\nWith outlier at index 4 (value=50):")
print(f"Pearson r = {r_outlier:.4f}  (original r = {r:.4f})")

# === 3. Spearman Rank Correlation ===

print("\n--- 3. Spearman Rank Correlation ---")

rho, p_value_sp = stats.spearmanr(x, y)
print(f"Spearman ρ = {rho:.4f}")
print(f"p-value    = {p_value_sp:.6f}")

# Spearman is more robust to the outlier
rho_outlier, _ = stats.spearmanr(x, y_outlier)
print(f"\nWith outlier: Spearman ρ = {rho_outlier:.4f}  (original ρ = {rho:.4f})")
print("Spearman is less affected by the outlier than Pearson.")

# Monotonic but non-linear example
x_exp = np.arange(1, 11)
y_exp = np.exp(x_exp * 0.3)  # exponential relationship
r_exp, _ = stats.pearsonr(x_exp, y_exp)
rho_exp, _ = stats.spearmanr(x_exp, y_exp)
print(f"\nExponential relationship: Pearson r = {r_exp:.4f}, Spearman ρ = {rho_exp:.4f}")
print("Spearman captures the perfect monotonic relationship (ρ = 1).")

# === 4. Correlation Matrices & Heatmaps ===

print("\n--- 4. Correlation Matrices & Heatmaps ---")

np.random.seed(38)
n = 50
df = pd.DataFrame({
    "height": np.random.normal(170, 10, n),
    "weight": np.random.normal(70, 15, n),
    "age": np.random.randint(20, 60, n).astype(float),
})
# Add a correlated column
df["shoe_size"] = df["height"] * 0.15 + np.random.normal(0, 1, n)

# Pearson correlation matrix
corr_pearson = df.corr()
print("Pearson correlation matrix:")
print(corr_pearson.round(3))

# Spearman correlation matrix
corr_spearman = df.corr(method="spearman")
print("\nSpearman correlation matrix:")
print(corr_spearman.round(3))

# Heatmap
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax, corr, title in zip(
    axes,
    [corr_pearson, corr_spearman],
    ["Pearson Correlation", "Spearman Correlation"],
):
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)
    # Annotate cells
    for i in range(len(corr)):
        for j in range(len(corr)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                    ha="center", va="center", fontsize=9,
                    color="white" if abs(corr.iloc[i, j]) > 0.5 else "black")
    ax.set_title(title)
fig.colorbar(im, ax=axes, shrink=0.8)
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=100)
print("\nSaved correlation_heatmap.png")

# === 5. Simple Linear Regression ===

print("\n--- 5. Simple Linear Regression ---")

result = stats.linregress(x, y)
print(f"slope     = {result.slope:.4f}")
print(f"intercept = {result.intercept:.4f}")
print(f"r-value   = {result.rvalue:.4f}")
print(f"R²        = {result.rvalue ** 2:.4f}")
print(f"p-value   = {result.pvalue:.6f}")
print(f"std err   = {result.stderr:.4f}")

# Predictions
y_pred = result.slope * x + result.intercept
print(f"\nPredicted values: {np.round(y_pred, 2)}")

# Predict new points
x_new = np.array([11, 12, 13])
y_new = result.slope * x_new + result.intercept
print(f"Predictions for x={x_new}: {np.round(y_new, 2)}")

# Regression plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x, y, color="steelblue", label="Observed data", zorder=3)
x_line = np.linspace(x.min() - 1, x_new.max() + 1, 100)
y_line = result.slope * x_line + result.intercept
ax.plot(x_line, y_line, color="red", linewidth=2,
        label=f"y = {result.slope:.2f}x + {result.intercept:.2f}")
ax.scatter(x_new, y_new, color="orange", marker="^", s=80,
           label="Predictions", zorder=3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Simple Linear Regression")
ax.legend()
plt.tight_layout()
plt.savefig("regression_line.png", dpi=100)
print("Saved regression_line.png")

# === 6. Evaluating Regression ===

print("\n--- 6. Evaluating Regression ---")

residuals = y - y_pred
ss_res = np.sum(residuals ** 2)
ss_tot = np.sum((y - y.mean()) ** 2)
r_squared = 1 - ss_res / ss_tot
mse = np.mean(residuals ** 2)

print(f"Residuals:      {np.round(residuals, 3)}")
print(f"SS_res          = {ss_res:.4f}")
print(f"SS_tot          = {ss_tot:.4f}")
print(f"R² (manual)     = {r_squared:.4f}")
print(f"R² (from r)     = {result.rvalue ** 2:.4f}")
print(f"MSE             = {mse:.4f}")
print(f"RMSE            = {np.sqrt(mse):.4f}")

# Residual plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Residuals vs fitted
axes[0].scatter(y_pred, residuals, color="steelblue", edgecolors="black")
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set_xlabel("Fitted values (ŷ)")
axes[0].set_ylabel("Residuals (y − ŷ)")
axes[0].set_title("Residuals vs Fitted")

# Histogram of residuals
axes[1].hist(residuals, bins=6, color="steelblue", edgecolor="black", alpha=0.7)
axes[1].set_xlabel("Residual")
axes[1].set_ylabel("Frequency")
axes[1].set_title("Residual Distribution")

plt.tight_layout()
plt.savefig("residual_analysis.png", dpi=100)
print("Saved residual_analysis.png")
