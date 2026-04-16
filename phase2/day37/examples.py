"""Day 37: Statistics — Hypothesis Testing — Examples"""

import numpy as np
import pandas as pd
from scipy import stats

# === 1. Hypothesis Testing Framework ===

print("--- 1. Hypothesis Testing Framework ---")
print("Steps: state H₀/H₁ → choose α → compute test statistic → p-value → decide")
print(f"Common significance level: α = 0.05")
print("Reject H₀ when p-value < α\n")

# Quick demonstration with a z-test (known σ)
np.random.seed(42)
sample = np.random.normal(loc=52, scale=10, size=50)
# H₀: μ = 50 vs H₁: μ ≠ 50
z_stat = (sample.mean() - 50) / (10 / np.sqrt(len(sample)))
p_value_z = 2 * (1 - stats.norm.cdf(abs(z_stat)))
print(f"Z-test example: z = {z_stat:.4f}, p = {p_value_z:.4f}")
print(f"  Reject H₀ (α=0.05)? {p_value_z < 0.05}")

# === 2. One-Sample t-Test ===

print("\n--- 2. One-Sample t-Test ---")

# H₀: The mean exam score is 75
exam_scores = np.array([78, 72, 81, 77, 74, 80, 76, 73, 79, 85,
                         71, 82, 77, 74, 83, 76, 80, 78, 75, 79])
t_stat, p_value = stats.ttest_1samp(exam_scores, popmean=75)
alpha = 0.05

print(f"Sample mean = {exam_scores.mean():.2f}")
print(f"H₀: μ = 75")
print(f"t-statistic = {t_stat:.4f}")
print(f"p-value     = {p_value:.4f}")
print(f"Reject H₀ at α={alpha}? {p_value < alpha}")

# === 3. Two-Sample t-Tests ===

print("\n--- 3. Two-Sample t-Tests ---")

# Independent two-sample t-test
print("Independent t-test:")
np.random.seed(10)
drug = np.random.normal(loc=8, scale=2, size=30)      # treatment group
placebo = np.random.normal(loc=6.5, scale=2.5, size=30)  # control group

t_stat, p_value = stats.ttest_ind(drug, placebo)
print(f"  Drug mean = {drug.mean():.2f}, Placebo mean = {placebo.mean():.2f}")
print(f"  t = {t_stat:.4f}, p = {p_value:.4f}")
print(f"  Reject H₀ (equal means) at α=0.05? {p_value < 0.05}")

# Welch's t-test (unequal variances)
t_welch, p_welch = stats.ttest_ind(drug, placebo, equal_var=False)
print(f"\n  Welch's t-test: t = {t_welch:.4f}, p = {p_welch:.4f}")

# Paired t-test
print("\nPaired t-test:")
before = np.array([200, 210, 190, 220, 205, 215, 195, 225, 210, 200])
after  = np.array([185, 195, 180, 205, 190, 200, 185, 210, 195, 188])

t_stat, p_value = stats.ttest_rel(before, after)
diff = before - after
print(f"  Mean difference = {diff.mean():.2f}")
print(f"  t = {t_stat:.4f}, p = {p_value:.4f}")
print(f"  Reject H₀ (no change) at α=0.05? {p_value < 0.05}")

# === 4. Chi-Square Tests ===

print("\n--- 4. Chi-Square Tests ---")

# Goodness of fit
print("Goodness of fit — are die rolls fair?")
observed = np.array([18, 22, 16, 20, 24, 20])  # 120 rolls
expected = np.array([20, 20, 20, 20, 20, 20])   # fair die
chi2, p_value = stats.chisquare(observed, f_exp=expected)
print(f"  χ² = {chi2:.4f}, p = {p_value:.4f}")
print(f"  Reject H₀ (fair die) at α=0.05? {p_value < 0.05}")

# Test of independence
print("\nTest of independence — treatment vs outcome:")
contingency = np.array([
    [30, 10],   # Treatment A: [success, failure]
    [15, 25],   # Treatment B: [success, failure]
])
chi2, p_value, dof, expected_freq = stats.chi2_contingency(contingency)
print(f"  Contingency table:\n{contingency}")
print(f"  χ² = {chi2:.4f}, p = {p_value:.4f}, dof = {dof}")
print(f"  Expected frequencies:\n{expected_freq}")
print(f"  Reject H₀ (independence) at α=0.05? {p_value < 0.05}")

# === 5. P-Values & Confidence Intervals ===

print("\n--- 5. P-Values & Confidence Intervals ---")

data = np.array([12.1, 11.8, 12.5, 12.0, 11.9, 12.3, 12.2, 11.7, 12.4, 12.1])
n = len(data)
mean = data.mean()
se = stats.sem(data)

print(f"Sample: n={n}, mean={mean:.4f}, SE={se:.4f}")

for confidence in [0.90, 0.95, 0.99]:
    ci = stats.t.interval(confidence, df=n - 1, loc=mean, scale=se)
    print(f"  {confidence:.0%} CI: [{ci[0]:.4f}, {ci[1]:.4f}]")

# One-sample t-test and its relationship to CI
t_stat, p_value = stats.ttest_1samp(data, popmean=12.0)
print(f"\nH₀: μ = 12.0 → t = {t_stat:.4f}, p = {p_value:.4f}")
print("Note: if 12.0 falls inside the 95% CI, we fail to reject at α=0.05")

# === 6. Non-Parametric Tests ===

print("\n--- 6. Non-Parametric Tests ---")

# Mann-Whitney U test (independent samples, non-normal)
np.random.seed(7)
x = np.array([4, 5, 6, 7, 3, 5, 6, 4, 5, 7])
y = np.array([8, 9, 7, 10, 8, 9, 11, 8, 10, 9])

u_stat, p_value = stats.mannwhitneyu(x, y, alternative='two-sided')
print(f"Mann-Whitney U: U = {u_stat:.2f}, p = {p_value:.4f}")
print(f"  Reject H₀ (equal distributions) at α=0.05? {p_value < 0.05}")

# Wilcoxon signed-rank (paired, non-normal)
before_w = np.array([25, 30, 28, 35, 32, 27, 29, 33, 31, 26])
after_w  = np.array([22, 27, 25, 30, 28, 24, 26, 29, 28, 23])

w_stat, p_value = stats.wilcoxon(before_w - after_w)
print(f"\nWilcoxon signed-rank: W = {w_stat:.2f}, p = {p_value:.4f}")
print(f"  Reject H₀ (no change) at α=0.05? {p_value < 0.05}")

# Kruskal-Wallis (3+ independent groups)
g1 = [4, 5, 6, 7, 3]
g2 = [8, 9, 7, 10, 8]
g3 = [2, 3, 1, 4, 2]
h_stat, p_value = stats.kruskal(g1, g2, g3)
print(f"\nKruskal-Wallis: H = {h_stat:.2f}, p = {p_value:.4f}")
print(f"  Reject H₀ (equal medians) at α=0.05? {p_value < 0.05}")

# === 7. Multiple Testing Correction ===

print("\n--- 7. Multiple Testing Correction ---")

raw_pvalues = [0.01, 0.04, 0.03, 0.20, 0.005, 0.08]
print(f"Raw p-values: {raw_pvalues}")

# Bonferroni (manual)
m = len(raw_pvalues)
bonf_pvalues = [min(p * m, 1.0) for p in raw_pvalues]
bonf_reject = [p < 0.05 for p in bonf_pvalues]
print(f"\nBonferroni adjusted: {[round(p, 4) for p in bonf_pvalues]}")
print(f"Bonferroni reject:   {bonf_reject}")

# Using statsmodels for Bonferroni and BH
try:
    from statsmodels.stats.multitest import multipletests

    reject_bonf, pvals_bonf, _, _ = multipletests(raw_pvalues, method='bonferroni')
    print(f"\nstatsmodels Bonferroni: {np.round(pvals_bonf, 4).tolist()}")
    print(f"  Reject: {reject_bonf.tolist()}")

    reject_bh, pvals_bh, _, _ = multipletests(raw_pvalues, method='fdr_bh')
    print(f"\nBenjamini-Hochberg (FDR): {np.round(pvals_bh, 4).tolist()}")
    print(f"  Reject: {reject_bh.tolist()}")

    reject_holm, pvals_holm, _, _ = multipletests(raw_pvalues, method='holm')
    print(f"\nHolm-Bonferroni: {np.round(pvals_holm, 4).tolist()}")
    print(f"  Reject: {reject_holm.tolist()}")
except ImportError:
    print("\n(statsmodels not installed — showing manual Bonferroni only)")

# Summary table
print("\n--- Summary: Which Test to Use ---")
summary = pd.DataFrame({
    "Scenario": [
        "Sample mean vs known value",
        "Two independent group means",
        "Paired/before-after means",
        "Categorical frequencies (1 var)",
        "Categorical independence (2 vars)",
        "Non-normal independent samples",
        "Non-normal paired samples",
        "3+ non-normal groups",
    ],
    "Test": [
        "One-sample t-test",
        "Independent t-test / Welch's",
        "Paired t-test",
        "Chi-square goodness of fit",
        "Chi-square independence",
        "Mann-Whitney U",
        "Wilcoxon signed-rank",
        "Kruskal-Wallis",
    ],
    "scipy Function": [
        "ttest_1samp",
        "ttest_ind",
        "ttest_rel",
        "chisquare",
        "chi2_contingency",
        "mannwhitneyu",
        "wilcoxon",
        "kruskal",
    ],
})
print(summary.to_string(index=False))

print("\n✅ All examples completed.")
