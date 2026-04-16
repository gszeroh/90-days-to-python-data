# Day 39: Exploratory Data Analysis (EDA)

## Overview

Exploratory Data Analysis (EDA) is the critical first phase of any data project.
Before building models or drawing conclusions you need to *understand* your data —
its shape, quirks, distributions, and relationships. EDA combines summary
statistics, visualisation, and domain intuition to surface patterns, spot
anomalies, and guide subsequent analysis.

This lesson walks through a complete EDA workflow using **pandas**, **NumPy**,
**Matplotlib**, and **Seaborn**, covering everything from initial inspection to
communicating your findings as a coherent story.

---

## 1. The EDA Workflow

A practical EDA follows five stages:

| Stage | Goal | Typical Actions |
|-------|------|-----------------|
| **Understand** | Know what the data represents | Read documentation, check provenance |
| **Clean** | Fix quality issues early | Handle missing values, duplicates, types |
| **Explore** | Quantify distributions & relationships | Descriptive stats, groupby, correlation |
| **Visualise** | Reveal patterns the eye catches fast | Histograms, scatter plots, heatmaps |
| **Communicate** | Share insights with stakeholders | Summarise key findings, tell a story |

> **Tip:** EDA is iterative — you will often loop back from *Explore* to *Clean*
> as new issues surface.

---

## 2. Initial Inspection

Always start by getting a high-level feel for the dataset:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df.shape              # (rows, columns)
df.dtypes             # column data types
df.info()             # non-null counts + memory usage
df.describe()         # summary stats for numeric columns
df.head()             # first 5 rows
df.tail()             # last 5 rows
df.sample(5)          # 5 random rows
df.isnull().sum()     # missing values per column
df.duplicated().sum() # duplicate row count
```

These one-liners give you a quick snapshot before diving deeper.

---

## 3. Univariate Analysis

Examine each column in isolation to understand its distribution.

### Numeric Columns

```python
df["revenue"].describe()          # count, mean, std, min, quartiles, max
df["revenue"].skew()              # asymmetry of distribution
df["revenue"].kurtosis()          # tail heaviness
df["revenue"].hist(bins=30)       # histogram
```

### Categorical Columns

```python
df["region"].value_counts()               # frequency of each category
df["region"].value_counts(normalize=True)  # relative frequencies
df["region"].nunique()                     # number of unique values
```

Key questions: *Is the distribution symmetric or skewed? Are there unexpected
values? How many missing entries?*

---

## 4. Bivariate Analysis

Explore how pairs of variables relate to each other.

```python
import seaborn as sns

# Numeric vs Numeric — scatter plot + correlation
sns.scatterplot(data=df, x="ad_spend", y="revenue")
df[["ad_spend", "revenue"]].corr()

# Numeric vs Categorical — grouped comparison
df.groupby("region")["revenue"].mean()
sns.boxplot(data=df, x="region", y="revenue")

# Categorical vs Categorical — cross-tabulation
pd.crosstab(df["region"], df["product"])
```

Correlation coefficients (Pearson, Spearman) quantify linear or monotonic
relationships but never imply causation.

---

## 5. Multivariate Analysis

When two dimensions are not enough, visualise higher-order interactions.

```python
# Pair plot — all pairwise scatter plots + diagonal distributions
sns.pairplot(df, hue="region")

# Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

# Faceting — separate plots per category
g = sns.FacetGrid(df, col="region", col_wrap=2)
g.map_dataframe(sns.histplot, x="revenue", bins=20)
```

Pair plots and heatmaps are especially useful for spotting clusters of correlated
features early in the analysis.

---

## 6. Handling Outliers & Missing Data in EDA

### Detecting Outliers with the IQR Method

```python
Q1 = df["revenue"].quantile(0.25)
Q3 = df["revenue"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["revenue"] < lower) | (df["revenue"] > upper)]
```

### Missing Data Strategies

| Strategy | When to Use |
|----------|-------------|
| **Drop rows** | Very few missing values, data is large |
| **Fill with mean/median** | Numeric column, roughly symmetric |
| **Fill with mode** | Categorical column |
| **Forward/back fill** | Time-series data |
| **Flag as missing** | Missingness itself is informative |

Always document your choices and check how they affect distributions.

---

## 7. Data Profiling Tools

Manual EDA is essential for building intuition, but automated profiling can save
time on large datasets.

* **ydata-profiling** (formerly *pandas-profiling*) generates a comprehensive
  HTML report with distributions, correlations, missing-value patterns, and
  alerts — all from a single function call:

```python
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Sales EDA Report")
profile.to_file("eda_report.html")
```

Use profiling as a complement to, not a replacement for, manual exploration.

---

## 8. Telling a Story with Data

Raw statistics and charts are only valuable if they lead to clear, actionable
insights. Structure your EDA report around these elements:

1. **Context** — What question are you answering? What does the data represent?
2. **Key findings** — The 3–5 most important patterns or anomalies.
3. **Supporting evidence** — Charts and statistics that back each finding.
4. **Caveats** — Known limitations, missing data, and assumptions.
5. **Next steps** — Recommendations for deeper analysis or modelling.

> *"The goal is not to produce the most charts, but to produce the most
> clarity."*

---

## Key Takeaways

- EDA follows a repeatable cycle: **understand → clean → explore → visualise →
  communicate**.
- Start every analysis with `shape`, `dtypes`, `info()`, `describe()`, and
  missing-value checks.
- Univariate analysis examines one variable at a time; bivariate and multivariate
  analysis reveal relationships between variables.
- The IQR method is a robust, non-parametric way to flag outliers.
- Automated profiling tools like **ydata-profiling** accelerate initial
  inspection but do not replace manual EDA.
- The most important EDA skill is **storytelling** — translating numbers and
  plots into clear, actionable insights.

---

## Further Reading

- [pandas User Guide — Essential Basic Functionality](https://pandas.pydata.org/docs/user_guide/basics.html)
- [Seaborn Tutorial — Visualizing Statistical Relationships](https://seaborn.pydata.org/tutorial/relational.html)
- [ydata-profiling Documentation](https://docs.profiling.ydata.ai/)
- [Tukey, J. W. — *Exploratory Data Analysis* (1977)](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
- [Kaggle — Data Cleaning & EDA Micro-Course](https://www.kaggle.com/learn/data-cleaning)
