# Day 40: Mini-Project — Sales Data Dashboard

## Overview

Congratulations — you've reached the **capstone project** of Phase 2! Over the
past 19 days you progressed from NumPy fundamentals through Pandas mastery,
data cleaning, reshaping, time-series analysis, merging, group-by operations,
string handling, visualisation with Matplotlib and Seaborn, and exploratory data
analysis. Today you'll bring **all of those skills together** to build an
end-to-end **Sales Data Dashboard** that generates a synthetic dataset, performs
comprehensive EDA, and produces a suite of publication-quality visualisations.

This is not a toy exercise. The project mirrors a real-world analytics workflow:
data generation → inspection → cleaning → descriptive statistics → visual
exploration → insight extraction. By the end of the day you will have a
portfolio piece that demonstrates your Phase 2 mastery.

---

## Project Requirements

| Feature | Description |
|---------|-------------|
| **Synthetic dataset** | Generate 1 000+ rows with dates, products, categories, regions, quantities, prices, revenue, and customer demographics |
| **Data inspection** | Shape, dtypes, nulls, duplicates, head/tail preview |
| **Descriptive statistics** | Central tendency, spread, and distribution summaries |
| **Monthly revenue trend** | Line chart showing revenue over time |
| **Category breakdown** | Bar chart of revenue by product category |
| **Regional comparison** | Grouped bar chart comparing regions |
| **Customer demographics** | Histogram of customer age distribution |
| **Correlation heatmap** | Heatmap of numeric feature correlations |
| **Top products** | Horizontal bar chart of top-selling products |
| **Key insights** | Printed summary of business-relevant findings |

---

## Phase 2 Concepts Used

| Day | Concept | Where It Appears |
|-----|---------|------------------|
| 21–22 | NumPy Arrays & Operations | Random data generation, vectorised revenue calculation |
| 23 | NumPy Statistics | Descriptive statistics, z-scores for anomaly detection |
| 24 | Broadcasting & Vectorisation | Efficient column creation without loops |
| 25–26 | Pandas Series & DataFrames | Core data structure for the entire project |
| 27 | Indexing & Selection | Filtering rows, selecting columns |
| 28 | Data Cleaning | Handling missing values, type casting, deduplication |
| 29 | Data Transformation | Creating derived columns (revenue, age groups) |
| 30 | GroupBy & Aggregation | Monthly summaries, category totals, regional stats |
| 31 | Merging & Joining | Combining product metadata with sales records |
| 32 | Reshaping (Pivot / Melt) | Pivot tables for cross-tabulation |
| 33 | String Operations | Product name manipulation, category mapping |
| 34 | Time-Series Basics | Date parsing, monthly resampling, trend analysis |
| 35–36 | Matplotlib & Seaborn | All six visualisation panels |
| 37 | Advanced Visualisation | Heatmaps, multi-panel layouts, annotations |
| 38 | Statistical Visualisation | Distribution plots, box plots, pair plots |
| 39 | EDA Workflow | End-to-end analysis pattern, storytelling with data |

---

## Architecture

```
phase2/day40/
├── README.md        ← You are here
├── examples.py      ← Main dashboard: data generation, EDA, visualisations
├── exercises.py     ← Extension exercise stubs
└── solutions.py     ← Reference solutions for exercises
```

### Dashboard Pipeline

```
generate_sales_data()
  │
  ▼
inspect_data()  →  clean & validate
  │
  ▼
descriptive_statistics()  →  summary tables
  │
  ▼
create_visualisations()
  ├── plot_monthly_revenue_trend()   → monthly_revenue_trend.png
  ├── plot_revenue_by_category()     → revenue_by_category.png
  ├── plot_regional_comparison()     → regional_comparison.png
  ├── plot_customer_age_dist()       → customer_age_distribution.png
  ├── plot_correlation_heatmap()     → correlation_heatmap.png
  └── plot_top_products()            → top_products.png
  │
  ▼
print_key_insights()  →  business findings
```

---

## How to Run

### Generate the dashboard

```bash
python phase2/day40/examples.py
```

This will:
1. Generate a synthetic sales dataset (1 000 rows)
2. Print inspection summaries and descriptive statistics
3. Save six PNG visualisation files in the current directory
4. Print key business insights

### Run the exercises (after implementing)

```bash
python phase2/day40/exercises.py
```

### Verify solutions

```bash
python phase2/day40/solutions.py
```

---

## Extension Ideas

After completing the base project, try the exercises in `exercises.py`:

1. **Monthly Summary Report** — Build a DataFrame with monthly KPIs
   (total revenue, quantity, average order value, top product).
2. **Customer Segmentation** — Group customers by age bracket and compute
   per-segment statistics.
3. **Anomaly Detection** — Flag days with unusually high or low revenue
   using z-scores.
4. **Growth Rate Analysis** — Compute month-over-month revenue growth rates
   and identify acceleration / deceleration.
5. **Product Recommendations** — Discover co-purchase patterns (customers
   who bought X also bought Y).

See `exercises.py` for guided stubs and `solutions.py` for reference
implementations.

---

## Key Takeaways

- A **capstone project** forces you to decide *which* tool fits each step —
  the real skill behind data analysis.
- **Synthetic data generation** is invaluable for prototyping dashboards
  when real data is unavailable.
- **Descriptive statistics** should always precede visualisation — numbers
  guide your chart choices.
- **Multiple chart types** reveal different facets of the same data: trends,
  comparisons, distributions, and correlations.
- **Insight extraction** is the goal — visualisations are a means, not an end.
- **Reproducibility** (fixed random seed, scripted pipeline) makes your
  analysis trustworthy and shareable.

---

## Further Reading

- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Storytelling with Data (book)](https://www.storytellingwithdata.com/)
- [Exploratory Data Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
- [Real Python — Pandas EDA Tutorial](https://realpython.com/pandas-python-explore-dataset/)
