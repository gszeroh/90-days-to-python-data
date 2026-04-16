"""
Day 35: Statistics — Descriptive Statistics — Examples
"""

import numpy as np
import pandas as pd
from scipy import stats

# === 1. Measures of Central Tendency ===

data = [4, 8, 6, 5, 3, 8, 9, 8, 2, 6]

mean = np.mean(data)
median = np.median(data)
mode_result = stats.mode(data, keepdims=False)

print("--- Central Tendency ---")
print(f"Data: {data}")
print(f"Mean:   {mean}")        # 5.9
print(f"Median: {median}")      # 6.0
print(f"Mode:   {mode_result.mode} (count={mode_result.count})")  # 8

# Weighted mean
values = [80, 90, 70]
weights = [0.3, 0.5, 0.2]
weighted_mean = np.average(values, weights=weights)
print(f"\nWeighted mean of {values} with weights {weights}: {weighted_mean}")

# === 2. Measures of Dispersion ===

print("\n--- Dispersion ---")

range_val = np.ptp(data)
variance_pop = np.var(data, ddof=0)
variance_sample = np.var(data, ddof=1)
std_pop = np.std(data, ddof=0)
std_sample = np.std(data, ddof=1)
iqr = stats.iqr(data)

print(f"Range:               {range_val}")
print(f"Population variance: {variance_pop:.4f}")
print(f"Sample variance:     {variance_sample:.4f}")
print(f"Population std dev:  {std_pop:.4f}")
print(f"Sample std dev:      {std_sample:.4f}")
print(f"IQR:                 {iqr}")

# Outlier detection using 1.5 × IQR rule
q1, q3 = np.percentile(data, [25, 75])
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr
outliers = [x for x in data if x < lower_fence or x > upper_fence]

print(f"\nQ1={q1}, Q3={q3}")
print(f"Lower fence: {lower_fence}, Upper fence: {upper_fence}")
print(f"Outliers: {outliers}")

# === 3. Measures of Shape ===

print("\n--- Shape ---")

skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)  # excess kurtosis (Fisher)

print(f"Skewness: {skewness:.4f}")
print(f"Kurtosis (excess): {kurtosis:.4f}")

# Demonstrate with a clearly skewed dataset
right_skewed = [1, 1, 2, 2, 2, 3, 3, 4, 5, 10, 15, 20]
print(f"\nRight-skewed data: {right_skewed}")
print(f"  Skewness: {stats.skew(right_skewed):.4f}")
print(f"  Kurtosis: {stats.kurtosis(right_skewed):.4f}")

# === 4. Quantiles & Percentiles ===

print("\n--- Quantiles & Percentiles ---")

quartiles = np.percentile(data, [25, 50, 75])
print(f"Quartiles (Q1, Q2, Q3): {quartiles}")

p10 = np.percentile(data, 10)
p90 = np.percentile(data, 90)
print(f"10th percentile: {p10}")
print(f"90th percentile: {p90}")

# Deciles using np.quantile
deciles = np.quantile(data, np.arange(0, 1.1, 0.1))
print(f"Deciles: {np.round(deciles, 2)}")

# Percentile rank of a specific value
rank = stats.percentileofscore(data, 6)
print(f"\nPercentile rank of 6 in the data: {rank}%")

# === 5. Frequency Distributions & Histograms ===

print("\n--- Frequency Distributions ---")

# NumPy histogram (without plotting)
counts, bin_edges = np.histogram(data, bins=4)
print(f"Bin edges: {bin_edges}")
print(f"Counts:    {counts}")

# Pandas value counts for discrete data
s = pd.Series(data)
freq = s.value_counts().sort_index()
rel_freq = freq / freq.sum()
cum_freq = freq.cumsum()

freq_table = pd.DataFrame({
    "frequency": freq,
    "relative_freq": rel_freq.round(4),
    "cumulative_freq": cum_freq,
})
print(f"\nFrequency table:\n{freq_table}")

# === 6. Summary Statistics with Pandas ===

print("\n--- Summary Statistics with Pandas ---")

df = pd.DataFrame({
    "score": [85, 92, 78, 90, 88, 76, 95, 89, 92, 80],
    "grade": ["B", "A", "C", "A", "B", "C", "A", "B", "A", "B"],
})

print("Numeric summary:")
print(df["score"].describe())

print(f"\nGrade frequencies:\n{df['grade'].value_counts()}")
print(f"\nNumber of unique grades: {df['grade'].nunique()}")

print("\nFull describe (include='all'):")
print(df.describe(include="all"))
