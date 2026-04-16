"""Day 40: Mini-Project — Sales Data Dashboard — Examples"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. Generate Synthetic Sales Dataset
# ============================================================

np.random.seed(40)

N_ROWS = 1000

products = {
    "Laptop":       ("Electronics", 800, 1500),
    "Smartphone":   ("Electronics", 400, 1000),
    "Headphones":   ("Electronics", 30, 200),
    "Desk Chair":   ("Furniture",   150, 500),
    "Standing Desk": ("Furniture",  300, 900),
    "Bookshelf":    ("Furniture",   80, 250),
    "Python Book":  ("Books",       20, 60),
    "Data Science Book": ("Books",  25, 70),
    "Notebook Set": ("Stationery",  5, 20),
    "Pen Pack":     ("Stationery",  3, 15),
}

product_names = list(products.keys())

dates = pd.date_range("2023-01-01", periods=365, freq="D")
regions = ["North", "South", "East", "West"]
genders = ["Male", "Female", "Non-binary"]

chosen_dates = np.random.choice(dates, size=N_ROWS)
chosen_products = np.random.choice(product_names, size=N_ROWS)

categories = [products[p][0] for p in chosen_products]
low_prices = np.array([products[p][1] for p in chosen_products], dtype=float)
high_prices = np.array([products[p][2] for p in chosen_products], dtype=float)

unit_prices = np.round(
    np.random.uniform(low_prices, high_prices), 2
)
quantities = np.random.randint(1, 11, size=N_ROWS)
revenues = np.round(unit_prices * quantities, 2)

customer_ages = np.random.normal(loc=35, scale=12, size=N_ROWS).astype(int)
customer_ages = np.clip(customer_ages, 18, 75)
customer_genders = np.random.choice(genders, size=N_ROWS, p=[0.48, 0.48, 0.04])

# Assign a customer_id so co-purchase analysis is possible
customer_ids = np.random.randint(1, 201, size=N_ROWS)

df = pd.DataFrame({
    "date":            chosen_dates,
    "product":         chosen_products,
    "category":        categories,
    "region":          np.random.choice(regions, size=N_ROWS),
    "quantity":        quantities,
    "unit_price":      unit_prices,
    "revenue":         revenues,
    "customer_id":     customer_ids,
    "customer_age":    customer_ages,
    "customer_gender": customer_genders,
})

df = df.sort_values("date").reset_index(drop=True)

print("=" * 60)
print("  📊  SALES DATA DASHBOARD — Day 40 Capstone")
print("=" * 60)

# ============================================================
# 2. Data Inspection
# ============================================================

print("\n--- Data Inspection ---")
print(f"Shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nNull counts:\n{df.isnull().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")
print(f"\nFirst 5 rows:\n{df.head()}")

# ============================================================
# 3. Descriptive Statistics
# ============================================================

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Revenue by Category ---")
cat_stats = df.groupby("category")["revenue"].agg(
    ["sum", "mean", "median", "std", "count"]
).sort_values("sum", ascending=False)
print(cat_stats)

print("\n--- Revenue by Region ---")
region_stats = df.groupby("region")["revenue"].agg(
    ["sum", "mean", "count"]
).sort_values("sum", ascending=False)
print(region_stats)

print("\n--- Top 10 Products by Total Revenue ---")
top_products = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)

# ============================================================
# 4. Visualisations
# ============================================================

sns.set_style("whitegrid")
palette = sns.color_palette("viridis", n_colors=6)

# --- 4a. Monthly Revenue Trend ---
monthly = df.set_index("date").resample("ME")["revenue"].sum()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly.index, monthly.values, marker="o", linewidth=2, color=palette[0])
ax.fill_between(monthly.index, monthly.values, alpha=0.15, color=palette[0])
ax.set_title("Monthly Revenue Trend (2023)", fontsize=14, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Total Revenue ($)")
plt.tight_layout()
fig.savefig("monthly_revenue_trend.png", dpi=150)
plt.close(fig)
print("\n✅ Saved monthly_revenue_trend.png")

# --- 4b. Revenue by Category ---
cat_rev = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
cat_rev.plot.bar(ax=ax, color=palette[:len(cat_rev)], edgecolor="black")
ax.set_title("Total Revenue by Category", fontsize=14, fontweight="bold")
ax.set_xlabel("Category")
ax.set_ylabel("Revenue ($)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
plt.tight_layout()
fig.savefig("revenue_by_category.png", dpi=150)
plt.close(fig)
print("✅ Saved revenue_by_category.png")

# --- 4c. Regional Comparison ---
region_cat = df.pivot_table(
    index="region", columns="category", values="revenue", aggfunc="sum"
)

fig, ax = plt.subplots(figsize=(10, 5))
region_cat.plot.bar(ax=ax, edgecolor="black")
ax.set_title("Revenue by Region & Category", fontsize=14, fontweight="bold")
ax.set_xlabel("Region")
ax.set_ylabel("Revenue ($)")
ax.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.tight_layout()
fig.savefig("regional_comparison.png", dpi=150)
plt.close(fig)
print("✅ Saved regional_comparison.png")

# --- 4d. Customer Age Distribution ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["customer_age"], bins=30, kde=True, ax=ax, color=palette[3])
ax.axvline(df["customer_age"].mean(), color="red", linestyle="--",
           label=f'Mean = {df["customer_age"].mean():.1f}')
ax.axvline(df["customer_age"].median(), color="orange", linestyle="--",
           label=f'Median = {df["customer_age"].median():.1f}')
ax.set_title("Customer Age Distribution", fontsize=14, fontweight="bold")
ax.set_xlabel("Age")
ax.set_ylabel("Count")
ax.legend()
plt.tight_layout()
fig.savefig("customer_age_distribution.png", dpi=150)
plt.close(fig)
print("✅ Saved customer_age_distribution.png")

# --- 4e. Correlation Heatmap ---
numeric_cols = df.select_dtypes(include=np.number)
corr = numeric_cols.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            square=True, linewidths=0.5, ax=ax)
ax.set_title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
fig.savefig("correlation_heatmap.png", dpi=150)
plt.close(fig)
print("✅ Saved correlation_heatmap.png")

# --- 4f. Top Products by Revenue ---
top10 = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=True)
    .tail(10)
)

fig, ax = plt.subplots(figsize=(9, 5))
top10.plot.barh(ax=ax, color=palette[4], edgecolor="black")
ax.set_title("Top 10 Products by Revenue", fontsize=14, fontweight="bold")
ax.set_xlabel("Total Revenue ($)")
ax.set_ylabel("")
plt.tight_layout()
fig.savefig("top_products.png", dpi=150)
plt.close(fig)
print("✅ Saved top_products.png")

# ============================================================
# 5. Key Insights
# ============================================================

print("\n" + "=" * 60)
print("  💡  KEY INSIGHTS")
print("=" * 60)

total_revenue = df["revenue"].sum()
best_month = monthly.idxmax().strftime("%B %Y")
best_category = cat_rev.idxmax()
best_region = df.groupby("region")["revenue"].sum().idxmax()
best_product = df.groupby("product")["revenue"].sum().idxmax()
avg_order = df["revenue"].mean()
median_age = df["customer_age"].median()

print(f"""
1. Total annual revenue: ${total_revenue:,.2f}
2. Best month: {best_month} (${monthly.max():,.2f})
3. Top category: {best_category} (${cat_rev.max():,.2f})
4. Top region: {best_region}
5. Best-selling product (by revenue): {best_product}
6. Average order value: ${avg_order:,.2f}
7. Median customer age: {median_age} years
8. Customer base: {df['customer_id'].nunique()} unique customers
9. Product catalogue: {df['product'].nunique()} products across {df['category'].nunique()} categories
""")

print("Dashboard complete! 🎉")
