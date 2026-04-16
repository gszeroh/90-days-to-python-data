# Day 37: Statistics — Hypothesis Testing

## Overview
Hypothesis testing is the backbone of statistical inference — it provides a
structured framework for making decisions about populations using sample data.
Today we cover the most widely used tests (t-tests, chi-square), interpret
p-values and confidence intervals, and explore non-parametric alternatives and
corrections for multiple comparisons, all using **scipy.stats**.

---

## 1. Hypothesis Testing Framework

Every hypothesis test follows the same general workflow:

1. **State the hypotheses:**
   - **Null hypothesis (H₀):** The default assumption (e.g., "no effect").
   - **Alternative hypothesis (H₁ / Hₐ):** What we want to show (e.g., "there
     is an effect").
2. **Choose a significance level (α):** The probability of rejecting H₀ when
   it is actually true (commonly α = 0.05).
3. **Compute the test statistic** from the sample data.
4. **Determine the p-value** — the probability of observing a result at least
   as extreme as the test statistic, assuming H₀ is true.
5. **Make a decision:** Reject H₀ if p-value < α; otherwise fail to reject.

| Term | Definition |
|------|-----------|
| **Type I error (α)** | Rejecting H₀ when it is true (false positive) |
| **Type II error (β)** | Failing to reject H₀ when it is false (false negative) |
| **Power (1 − β)** | Probability of correctly rejecting a false H₀ |
| **Effect size** | Magnitude of the difference being tested |

> **Tip:** "Fail to reject H₀" is not the same as "accept H₀." The test only
> measures evidence *against* the null hypothesis.

---

## 2. One-Sample t-Test

Tests whether the mean of a single sample differs from a known or hypothesized
population mean μ₀.

**Assumptions:** Data approximately normal (robust with n ≥ 30 by CLT),
observations independent.

```python
from scipy import stats

# Does this sample have a mean different from 100?
data = [102, 98, 104, 101, 97, 105, 99, 103, 100, 106]
t_stat, p_value = stats.ttest_1samp(data, popmean=100)
print(f"t = {t_stat:.4f}, p = {p_value:.4f}")
# If p < 0.05 → reject H₀: μ = 100
```

---

## 3. Two-Sample t-Tests

### Independent Two-Sample t-Test
Compares the means of two **independent** groups.

```python
group_a = [23, 25, 28, 22, 27]
group_b = [30, 33, 29, 35, 31]
t_stat, p_value = stats.ttest_ind(group_a, group_b)
# equal_var=False for Welch's t-test (unequal variances)
```

### Paired t-Test
Compares means from the **same group** measured at two time points (e.g.,
before/after treatment).

```python
before = [200, 210, 190, 220, 205]
after  = [180, 195, 185, 210, 195]
t_stat, p_value = stats.ttest_rel(before, after)
```

> **When to use which:** Use paired when measurements are naturally linked
> (same subject, same item). Use independent otherwise.

---

## 4. Chi-Square Tests

### Goodness of Fit
Tests whether observed frequencies match an expected distribution.

```python
observed = [50, 30, 20]
expected = [40, 35, 25]
chi2, p_value = stats.chisquare(observed, f_exp=expected)
```

### Test of Independence
Tests whether two categorical variables are independent using a contingency
table.

```python
import numpy as np
from scipy import stats

table = np.array([[30, 10],
                  [5,  25]])
chi2, p_value, dof, expected = stats.chi2_contingency(table)
print(f"χ² = {chi2:.4f}, p = {p_value:.4f}, dof = {dof}")
```

---

## 5. P-Values & Confidence Intervals

**P-value:** The probability of obtaining a test statistic at least as extreme
as the observed value, assuming H₀ is true. A small p-value (< α) provides
evidence against H₀.

**Confidence interval (CI):** A range of values that is expected to contain the
true population parameter with a given probability (e.g., 95%).

```python
import numpy as np
from scipy import stats

data = np.array([12.1, 11.8, 12.5, 12.0, 11.9, 12.3])
n = len(data)
mean = data.mean()
se = stats.sem(data)               # standard error of the mean
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)
print(f"95% CI: [{ci[0]:.4f}, {ci[1]:.4f}]")
```

| α | Confidence Level | Interpretation |
|---|-----------------|----------------|
| 0.10 | 90% | Weak evidence against H₀ |
| 0.05 | 95% | Moderate evidence (most common) |
| 0.01 | 99% | Strong evidence against H₀ |

> **Common misconception:** A 95% CI does *not* mean there is a 95% probability
> that the true parameter is inside the interval. It means that 95% of such
> intervals (across repeated experiments) would contain the true value.

---

## 6. Non-Parametric Tests

When data violate normality assumptions or are ordinal, use non-parametric
alternatives:

| Parametric Test | Non-Parametric Alternative | scipy Function |
|----------------|---------------------------|---------------|
| One-sample t-test | Wilcoxon signed-rank | `stats.wilcoxon` |
| Independent t-test | Mann-Whitney U | `stats.mannwhitneyu` |
| Paired t-test | Wilcoxon signed-rank | `stats.wilcoxon` |
| One-way ANOVA | Kruskal-Wallis | `stats.kruskal` |

```python
from scipy import stats

x = [4, 5, 6, 7, 3, 5]
y = [8, 9, 7, 10, 8, 9]

# Mann-Whitney U test (independent samples)
u_stat, p_value = stats.mannwhitneyu(x, y, alternative='two-sided')
print(f"U = {u_stat:.2f}, p = {p_value:.4f}")

# Kruskal-Wallis (3+ independent groups)
z = [2, 3, 1, 4, 2, 3]
h_stat, p_value = stats.kruskal(x, y, z)
print(f"H = {h_stat:.2f}, p = {p_value:.4f}")
```

---

## 7. Multiple Testing Correction

When performing many simultaneous tests, the chance of at least one Type I
error increases. Corrections control for this.

| Method | Controls | Approach |
|--------|----------|----------|
| **Bonferroni** | Family-wise error rate (FWER) | Multiply p-values by number of tests |
| **Holm** | FWER | Step-down Bonferroni (less conservative) |
| **Benjamini-Hochberg** | False discovery rate (FDR) | Controls expected proportion of false positives |

```python
from statsmodels.stats.multitest import multipletests

p_values = [0.01, 0.04, 0.03, 0.20, 0.005]

# Bonferroni correction
reject_bonf, pvals_bonf, _, _ = multipletests(p_values, method='bonferroni')
print("Bonferroni adjusted:", pvals_bonf)

# Benjamini-Hochberg (FDR)
reject_bh, pvals_bh, _, _ = multipletests(p_values, method='fdr_bh')
print("BH adjusted:", pvals_bh)
```

> **Rule of thumb:** Use Bonferroni when false positives are very costly.
> Use FDR when testing many hypotheses (e.g., genomics) and some false
> positives are tolerable.

---

## Key Takeaways
- Always state H₀ and H₁ **before** looking at data to avoid bias.
- **One-sample t-test** compares a sample mean to a known value; **two-sample**
  compares two group means.
- **Chi-square tests** evaluate categorical frequency data — goodness of fit or
  independence.
- A **p-value** quantifies evidence against H₀; it is *not* the probability
  that H₀ is true.
- **Confidence intervals** give a range of plausible values for a parameter —
  more informative than a binary reject/fail decision.
- Use **non-parametric tests** when normality assumptions are violated.
- Apply **multiple testing corrections** (Bonferroni, FDR) whenever you run
  many tests simultaneously.

---

## Further Reading
- [SciPy — Statistical Tests](https://docs.scipy.org/doc/scipy/reference/stats.html#statistical-tests)
- [statsmodels — Multiple Testing](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html)
- [Khan Academy — Hypothesis Testing](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)
- [Wikipedia — Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)
- [Wikipedia — Chi-squared test](https://en.wikipedia.org/wiki/Chi-squared_test)
