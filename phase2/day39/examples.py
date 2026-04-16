"""Day 39: Exploratory Data Analysis (EDA) — Examples"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# === 1. Build a Synthetic Sales Dataset ===

np.random.seed(39)
n = 200

regions = np.random.choice(["North", "South", "East", "West"], size=n)
products = np.random.choice(["Widget", "Gadget", "Doohickey"], size=n)

ad_spend = np.round(np.random.uniform(500, 5000, n), 2)
revenue = ad_spend * np.random.uniform(1.5, 4.0, n) + np.random.normal(0, 500, n)
revenue = np.round(revenue, 2)

units_sold = np.random.poisson(lam=50, size=n)
satisfaction = np.clip(np.random.normal(4.0, 0.8, n), 1, 5).round(1)

df = pd.DataFrame({
    "region": regions,
    "product": products,
    "ad_spend": ad_spend,
    "revenue": revenue,
    "units_sold": units_sold,
    "satisfaction": satisfaction,
})

# Inject some missing values and duplicates for realism
df.loc[np.random.choice(n, 10, replace=False), "satisfaction"] = np.nan
df.loc[np.random.choice(n, 5, replace=False), "revenue"] = np.nan
df = pd.concat([df, df.iloc[:3]], ignore_index=True)  # add 3 duplicate rows

print("=== Synthetic Sales Dataset ===")
print(f"Shape: {df.shape}\n")

# === 2. Initial Inspection ===

print("--- Data Types ---")
print(df.dtypes)

print("\n--- Info ---")
df.info()

print("\n--- Describe (numeric) ---")
print(df.describe().round(2))

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Missing values per column ---")
print(df.isnull().sum())

print(f"\nDuplicate rows: {df.duplicated().sum()}")

# === 3. Univariate Analysis ===

print("\n=== Univariate Analysis ===")

# Numeric column: revenue
print("\n--- Revenue distribution ---")
rev = df["revenue"].dropna()
print(f"  Mean:     {rev.mean():.2f}")
print(f"  Median:   {rev.median():.2f}")
print(f"  Std:      {rev.std():.2f}")
print(f"  Skew:     {rev.skew():.3f}")
print(f"  Kurtosis: {rev.kurtosis():.3f}")

# Categorical column: region
print("\n--- Region value counts ---")
print(df["region"].value_counts())
print(f"\nUnique regions: {df['region'].nunique()}")

# Histogram of revenue
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(rev, bins=25, color="steelblue", edgecolor="white")
axes[0].set_title("Revenue Distribution")
axes[0].set_xlabel("Revenue")
axes[0].set_ylabel("Frequency")

# Count plot for region
region_counts = df["region"].value_counts()
axes[1].bar(region_counts.index, region_counts.values, color="coral", edgecolor="white")
axes[1].set_title("Sales by Region")
axes[1].set_xlabel("Region")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("univariate_analysis.png", dpi=100)
plt.close()
print("\nSaved univariate_analysis.png")

# === 4. Bivariate Analysis ===

print("\n=== Bivariate Analysis ===")

# Scatter: ad_spend vs revenue
clean = df.dropna(subset=["revenue", "ad_spend"])
corr_val = clean["ad_spend"].corr(clean["revenue"])
print(f"Pearson r (ad_spend vs revenue): {corr_val:.3f}")

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].scatter(clean["ad_spend"], clean["revenue"],
                alpha=0.5, color="steelblue", edgecolors="white", linewidths=0.5)
axes[0].set_title(f"Ad Spend vs Revenue  (r = {corr_val:.2f})")
axes[0].set_xlabel("Ad Spend")
axes[0].set_ylabel("Revenue")

# Grouped comparison: revenue by region
grouped = df.groupby("region")["revenue"].mean().sort_values(ascending=False)
print(f"\nMean revenue by region:\n{grouped.round(2)}")

axes[1].barh(grouped.index, grouped.values, color="teal")
axes[1].set_title("Mean Revenue by Region")
axes[1].set_xlabel("Mean Revenue")

plt.tight_layout()
plt.savefig("bivariate_analysis.png", dpi=100)
plt.close()
print("\nSaved bivariate_analysis.png")

# Cross-tabulation
print("\n--- Cross-tabulation: region × product ---")
print(pd.crosstab(df["region"], df["product"]))

# === 5. Multivariate Analysis ===

print("\n=== Multivariate Analysis ===")

numeric_cols = ["ad_spend", "revenue", "units_sold", "satisfaction"]
corr_matrix = df[numeric_cols].corr()
print("Correlation matrix:")
print(corr_matrix.round(3))

# Heatmap
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr_matrix.values, cmap="coolwarm", vmin=-1, vmax=1)

ax.set_xticks(range(len(numeric_cols)))
ax.set_yticks(range(len(numeric_cols)))
ax.set_xticklabels(numeric_cols, rotation=45, ha="right")
ax.set_yticklabels(numeric_cols)

for i in range(len(numeric_cols)):
    for j in range(len(numeric_cols)):
        val = corr_matrix.iloc[i, j]
        color = "white" if abs(val) > 0.5 else "black"
        ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                fontsize=10, color=color)

fig.colorbar(im, ax=ax, shrink=0.8)
ax.set_title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=100)
plt.close()
print("\nSaved correlation_heatmap.png")

# Pair plot (seaborn)
pair_df = df[["ad_spend", "revenue", "units_sold", "region"]].dropna()
g = sns.pairplot(pair_df, hue="region", diag_kind="hist",
                 plot_kws={"alpha": 0.5, "s": 20})
g.figure.suptitle("Pair Plot — Sales Data", y=1.02)
g.savefig("pair_plot.png", dpi=100)
plt.close()
print("Saved pair_plot.png")

# === 6. Handling Outliers & Missing Data ===

print("\n=== Outliers & Missing Data ===")

# IQR outlier detection on revenue
Q1 = rev.quantile(0.25)
Q3 = rev.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier_mask = (rev < lower_bound) | (rev > upper_bound)
print(f"Revenue IQR: {IQR:.2f}")
print(f"Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Outlier count: {outlier_mask.sum()}")

# Missing data summary
missing_pct = (df.isnull().sum() / len(df) * 100).round(2)
print(f"\nMissing data (%):\n{missing_pct[missing_pct > 0]}")

# Demonstrate filling strategies
df_clean = df.copy()
df_clean["satisfaction"] = df_clean["satisfaction"].fillna(
    df_clean["satisfaction"].median()
)
df_clean["revenue"] = df_clean["revenue"].fillna(
    df_clean.groupby("region")["revenue"].transform("median")
)
df_clean.drop_duplicates(inplace=True)
print(f"\nAfter cleaning — shape: {df_clean.shape}")
print(f"Remaining missing: {df_clean.isnull().sum().sum()}")

# === 7. Data Profiling (Concept Demo) ===

print("\n=== Data Profiling (Manual Mini-Report) ===")

report = {}
for col in df_clean.columns:
    info = {"dtype": str(df_clean[col].dtype), "missing": int(df_clean[col].isnull().sum())}
    if pd.api.types.is_numeric_dtype(df_clean[col]):
        info["mean"] = round(float(df_clean[col].mean()), 2)
        info["std"] = round(float(df_clean[col].std()), 2)
    else:
        info["unique"] = int(df_clean[col].nunique())
        info["top"] = str(df_clean[col].mode().iloc[0])
    report[col] = info

for col, info in report.items():
    print(f"  {col}: {info}")

# === 8. Telling a Story ===

print("\n=== Key Findings (Story) ===")
print("1. Revenue is positively correlated with ad spend — higher budgets")
print("   tend to produce higher returns.")
print(f"2. The '{grouped.index[0]}' region leads in mean revenue, suggesting")
print("   stronger market performance or customer base.")
print(f"3. {outlier_mask.sum()} revenue outlier(s) were detected via the IQR")
print("   method and should be investigated for data-entry errors.")
print("4. Satisfaction scores are roughly normally distributed (mean ≈ 4.0),")
print("   with no strong link to revenue.")
print("5. Missing data was modest (<10 %) and handled with median imputation")
print("   per region for revenue, and global median for satisfaction.")
