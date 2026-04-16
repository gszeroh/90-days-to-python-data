# Day 35: Statistics — Descriptive Statistics

## Overview
Descriptive statistics summarise and describe the main features of a dataset.
Today we cover measures of central tendency, dispersion, shape, quantiles, and
frequency distributions using **NumPy**, **SciPy**, and **Pandas** — the
essential toolkit for every data scientist.

---

## 1. Measures of Central Tendency

Central tendency tells us where the "centre" of the data lies.

| Measure | Description | Best For |
|---------|-------------|----------|
| **Mean** | Arithmetic average | Symmetric data without outliers |
| **Median** | Middle value when sorted | Skewed data / ordinal data |
| **Mode** | Most frequent value | Categorical / discrete data |
| **Weighted Mean** | Average weighted by importance | Survey / sampling weights |

```python
import numpy as np
from scipy import stats

data = [4, 8, 6, 5, 3, 8, 9, 8, 2, 6]

mean   = np.mean(data)            # 5.9
median = np.median(data)          # 6.0
mode   = stats.mode(data, keepdims=False).mode  # 8

# Weighted mean
values  = [80, 90, 70]
weights = [0.3, 0.5, 0.2]
weighted_mean = np.average(values, weights=weights)  # 83.0
```

> **Tip:** The mean is sensitive to outliers; the median is robust.

---

## 2. Measures of Dispersion

Dispersion quantifies how spread out the values are.

| Measure | Formula Idea | NumPy / SciPy |
|---------|-------------|----------------|
| **Range** | max − min | `np.ptp(data)` |
| **Variance** | mean of squared deviations | `np.var(data, ddof=1)` |
| **Std Dev** | √variance | `np.std(data, ddof=1)` |
| **IQR** | Q3 − Q1 | `stats.iqr(data)` |

```python
import numpy as np
from scipy import stats

data = [4, 8, 6, 5, 3, 8, 9, 8, 2, 6]

range_val = np.ptp(data)                   # 7
variance  = np.var(data, ddof=1)           # 5.21 (sample variance)
std_dev   = np.std(data, ddof=1)           # 2.28
iqr       = stats.iqr(data)               # 3.0

# Outlier detection with 1.5 × IQR rule
q1, q3 = np.percentile(data, [25, 75])
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = [x for x in data if x < lower or x > upper]
```

> **Note:** Use `ddof=1` for the *sample* variance/std; `ddof=0` gives the
> *population* version.

---

## 3. Measures of Shape

Shape statistics describe the symmetry and peakedness of a distribution.

| Measure | Interpretation |
|---------|---------------|
| **Skewness** | 0 = symmetric, > 0 = right-skewed, < 0 = left-skewed |
| **Kurtosis** | 0 = normal (excess), > 0 = heavy tails, < 0 = light tails |

```python
from scipy import stats

data = [4, 8, 6, 5, 3, 8, 9, 8, 2, 6]

skew = stats.skew(data)         # negative ⇒ slight left skew
kurt = stats.kurtosis(data)     # excess kurtosis (Fisher definition)
```

- **`stats.skew`** computes the sample skewness (bias=True by default).
- **`stats.kurtosis`** returns *excess* kurtosis (normal = 0) by default.

---

## 4. Quantiles & Percentiles

Quantiles divide ranked data into equal-probability intervals.

| Term | Meaning |
|------|---------|
| **Quartiles** | 4 equal parts → Q1 (25 %), Q2 (50 %), Q3 (75 %) |
| **Percentile** | Value below which a given % of data falls |
| **Quantile** | General term — 0.5 quantile = median |

```python
import numpy as np

data = [4, 8, 6, 5, 3, 8, 9, 8, 2, 6]

q1, q2, q3 = np.percentile(data, [25, 50, 75])
# q1 = 4.25, q2 = 6.0, q3 = 8.0

# Arbitrary percentile
p90 = np.percentile(data, 90)   # 8.1

# NumPy quantile (0-1 scale)
deciles = np.quantile(data, np.arange(0, 1.1, 0.1))
```

> **Percentile rank** of a value tells you what percentage of data falls at or
> below that value: `stats.percentileofscore(data, value)`.

---

## 5. Frequency Distributions & Histograms

A frequency distribution groups data into bins and counts occurrences.

```python
import numpy as np
import pandas as pd

data = [4, 8, 6, 5, 3, 8, 9, 8, 2, 6]

# NumPy histogram (counts + bin edges)
counts, bin_edges = np.histogram(data, bins=5)

# Pandas value counts (for discrete data)
s = pd.Series(data)
freq = s.value_counts().sort_index()

# Relative (normalised) frequency
rel_freq = freq / freq.sum()

# Cumulative frequency
cum_freq = freq.cumsum()
```

Frequency tables are the foundation of histograms and help reveal the shape of
the underlying distribution.

---

## 6. Summary Statistics with Pandas

Pandas provides convenient one-liner summaries for Series and DataFrames.

```python
import pandas as pd

df = pd.DataFrame({
    "score": [85, 92, 78, 90, 88, 76, 95, 89, 92, 80],
    "grade": ["B", "A", "C", "A", "B", "C", "A", "B", "A", "B"],
})

# Full statistical summary
df["score"].describe()
# count, mean, std, min, 25%, 50%, 75%, max

# Unique value helpers
df["grade"].value_counts()   # frequency of each grade
df["grade"].nunique()        # 3

# Correlation & covariance (for multiple numeric columns)
df.describe(include="all")   # includes categorical columns
```

> **`describe()`** automatically adjusts its output for numeric vs categorical
> columns when `include='all'` is used.

---

## Key Takeaways
- **Central tendency** (mean, median, mode) locates the centre of the data.
- **Dispersion** (range, variance, std, IQR) measures spread.
- **Skewness** and **kurtosis** describe distribution shape.
- **Quantiles** divide data into equal-probability segments; percentiles are
  the most common variant.
- **Frequency distributions** reveal the shape and concentration of data.
- **Pandas `describe()`** gives a quick statistical snapshot of any DataFrame.
- Always use `ddof=1` for *sample* statistics (the default in Pandas, but not
  in NumPy).

---

## Further Reading
- [NumPy — Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [SciPy — Descriptive Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Pandas — `describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- [Khan Academy — Descriptive Statistics](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)
- [NIST Engineering Statistics Handbook — Exploratory Data Analysis](https://www.itl.nist.gov/div898/handbook/eda/eda.htm)
