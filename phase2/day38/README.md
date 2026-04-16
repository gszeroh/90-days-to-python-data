# Day 38: Statistics — Correlation & Regression Basics

## Overview
Understanding the relationship between variables is fundamental to data
analysis. Today we explore **correlation** — measuring the strength and
direction of associations — and **simple linear regression** — fitting a
straight line to model how one variable predicts another. We use **NumPy**,
**pandas**, **scipy.stats**, and **matplotlib** throughout.

---

## 1. Covariance

Covariance measures how two variables change together.

**Population covariance:**

$$\text{Cov}(X, Y) = \frac{1}{N}\sum_{i=1}^{N}(x_i - \bar{x})(y_i - \bar{y})$$

**Sample covariance** (Bessel's correction):

$$s_{xy} = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Sample covariance matrix — element [0, 1] is Cov(x, y)
cov_matrix = np.cov(x, y)          # ddof=1 by default (sample)
cov_xy = cov_matrix[0, 1]          # 1.5
```

**Limitations:**

| Issue | Explanation |
|-------|-------------|
| Scale-dependent | Covariance magnitude depends on variable units |
| No bounded range | Hard to compare across different variable pairs |
| Linear only | Does not capture non-linear associations |

> Because of these limitations, we typically standardise covariance into a
> **correlation coefficient**.

---

## 2. Pearson Correlation Coefficient

The Pearson correlation coefficient (*r*) standardises covariance to the range
\[−1, +1\]:

$$r = \frac{\text{Cov}(X, Y)}{s_X \, s_Y}$$

```python
from scipy import stats

r, p_value = stats.pearsonr(x, y)
print(f"Pearson r = {r:.4f}, p-value = {p_value:.4f}")
```

**Interpretation guide:**

| |r| Range | Strength |
|------------|----------|
| 0.00–0.19 | Very weak |
| 0.20–0.39 | Weak |
| 0.40–0.59 | Moderate |
| 0.60–0.79 | Strong |
| 0.80–1.00 | Very strong |

**Key assumptions:**

1. Both variables are **continuous**.
2. The relationship is approximately **linear**.
3. Both variables are roughly **normally distributed** (for inference/p-value).
4. **No significant outliers** — Pearson *r* is sensitive to extreme values.

> ⚠️ Correlation does not imply causation. A strong *r* value means the
> variables move together; it does not tell us *why*.

---

## 3. Spearman Rank Correlation

Spearman's *ρ* (rho) is a **non-parametric** rank-based alternative to Pearson.
It measures the strength of a **monotonic** relationship — the variables
consistently increase or decrease together, but not necessarily at a constant
rate.

```python
rho, p_value = stats.spearmanr(x, y)
print(f"Spearman ρ = {rho:.4f}, p-value = {p_value:.4f}")
```

**When to prefer Spearman over Pearson:**

- Data contain **outliers** that could distort Pearson *r*.
- The relationship is **monotonic but non-linear** (e.g., exponential growth).
- Variables are measured on **ordinal** scales (ranks, ratings).

| Feature | Pearson | Spearman |
|---------|---------|----------|
| Measures | Linear association | Monotonic association |
| Data type | Continuous | Continuous or ordinal |
| Sensitivity to outliers | High | Low |
| Assumes normality | Yes (for inference) | No |

---

## 4. Correlation Matrices & Heatmaps

When working with multiple variables, computing pairwise correlations produces a
**correlation matrix**. Visualising it as a heatmap is a quick way to spot
patterns.

```python
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.DataFrame({"A": x, "B": y, "C": [5, 3, 4, 2, 1]})

# Pearson correlation matrix
corr = df.corr()
print(corr)

# Heatmap
fig, ax = plt.subplots()
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticks(range(len(corr.columns)))
ax.set_yticklabels(corr.columns)
fig.colorbar(im)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=100)
```

> **Tip:** For large DataFrames, `df.corr(method="spearman")` generates a
> Spearman matrix instead.

---

## 5. Simple Linear Regression

Simple linear regression fits a straight line through the data:

$$\hat{y} = b_0 + b_1 x$$

where *b₁* (slope) and *b₀* (intercept) are estimated by **Ordinary Least
Squares (OLS)** — minimising the sum of squared residuals.

$$b_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$

$$b_0 = \bar{y} - b_1 \bar{x}$$

`scipy.stats.linregress` computes everything in one call:

```python
result = stats.linregress(x, y)
print(f"slope     = {result.slope:.4f}")
print(f"intercept = {result.intercept:.4f}")
print(f"r-value   = {result.rvalue:.4f}")
print(f"p-value   = {result.pvalue:.6f}")
print(f"std err   = {result.stderr:.4f}")
```

Predicting new values:

```python
x_new = np.array([6, 7, 8])
y_pred = result.slope * x_new + result.intercept
```

---

## 6. Evaluating Regression

### R² (Coefficient of Determination)

R² measures how much variance in *y* is explained by the model:

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

where:
- **SS_res** = Σ(yᵢ − ŷᵢ)² — residual sum of squares
- **SS_tot** = Σ(yᵢ − ȳ)² — total sum of squares

For simple linear regression, R² = r².

### Residual Analysis

Residuals are the differences between observed and predicted values:

$$e_i = y_i - \hat{y}_i$$

A good model shows residuals that are:
1. **Randomly scattered** around zero (no pattern).
2. **Roughly constant variance** (homoscedasticity).
3. **Approximately normally distributed**.

### Mean Squared Error (MSE)

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

### Key Assumptions of OLS Regression

| Assumption | Description |
|------------|-------------|
| **Linearity** | Relationship between *x* and *y* is linear |
| **Independence** | Observations are independent of each other |
| **Homoscedasticity** | Constant variance of residuals |
| **Normality** | Residuals are normally distributed |

---

## Key Takeaways

1. **Covariance** measures joint variability but is scale-dependent — use
   correlation instead for comparisons.
2. **Pearson *r*** captures *linear* association; **Spearman *ρ*** captures
   *monotonic* association and is robust to outliers.
3. A **correlation matrix** paired with a **heatmap** is the fastest way to
   scan pairwise relationships in a dataset.
4. **Simple linear regression** (OLS) finds the best-fit line by minimising
   squared residuals; `scipy.stats.linregress` is the go-to tool.
5. **R²** quantifies explanatory power; **residual plots** verify model
   assumptions.

---

## Further Reading

- [scipy.stats.pearsonr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)
- [scipy.stats.spearmanr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)
- [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)
- [NumPy — np.cov](https://numpy.org/doc/stable/reference/generated/numpy.cov.html)
- [pandas — DataFrame.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [Khan Academy — Correlation and Regression](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data)
- [Penn State STAT 501 — Simple Linear Regression](https://online.stat.psu.edu/stat501/lesson/1)
