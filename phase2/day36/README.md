# Day 36: Statistics — Probability & Distributions

## Overview
Probability theory provides the mathematical foundation for statistical
inference and data science. Today we explore core probability concepts,
the most important discrete and continuous distributions, and how to work
with them in Python using **scipy.stats**. We also demonstrate the
**Central Limit Theorem**, one of the most powerful results in statistics.

---

## 1. Probability Basics

Probability assigns a number between 0 and 1 to every event in a **sample
space** (the set of all possible outcomes).

| Concept | Definition |
|---------|-----------|
| **Sample space (S)** | Set of all possible outcomes |
| **Event (A)** | A subset of the sample space |
| **Complement (Aᶜ)** | Everything in S not in A |
| **Union (A ∪ B)** | A or B (or both) occur |
| **Intersection (A ∩ B)** | Both A and B occur |

**Axioms of Probability (Kolmogorov):**
1. P(A) ≥ 0 for any event A
2. P(S) = 1
3. For mutually exclusive events: P(A ∪ B) = P(A) + P(B)

```python
# Complement rule
# P(Aᶜ) = 1 - P(A)
p_rain = 0.3
p_no_rain = 1 - p_rain  # 0.7

# Addition rule (general)
# P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
p_a, p_b, p_a_and_b = 0.4, 0.5, 0.2
p_a_or_b = p_a + p_b - p_a_and_b  # 0.7
```

> **Tip:** For mutually exclusive events (P(A ∩ B) = 0), the addition rule
> simplifies to P(A ∪ B) = P(A) + P(B).

---

## 2. Conditional Probability & Bayes' Theorem

**Conditional probability** is the probability of A given B has occurred:

P(A | B) = P(A ∩ B) / P(B)

**Bayes' Theorem** reverses the conditioning:

P(A | B) = P(B | A) · P(A) / P(B)

```python
# Medical test example
# Disease prevalence (prior): 1%
# Sensitivity P(positive | disease): 99%
# False-positive rate P(positive | no disease): 5%

prior = 0.01
sensitivity = 0.99
false_positive_rate = 0.05

# Total probability of a positive test
p_positive = sensitivity * prior + false_positive_rate * (1 - prior)

# Posterior: P(disease | positive test)
posterior = (sensitivity * prior) / p_positive
# ≈ 0.167 — only ~17% chance of actually having the disease!
```

> **Key insight:** Even with a highly accurate test, a low prior probability
> can lead to a surprisingly low posterior — the **base rate fallacy**.

---

## 3. Discrete Distributions

Discrete distributions model outcomes that take on countable values.

| Distribution | Parameters | Use Case |
|-------------|-----------|----------|
| **Bernoulli** | p | Single yes/no trial |
| **Binomial** | n, p | Number of successes in n trials |
| **Poisson** | λ (mu) | Count of events in a fixed interval |
| **Geometric** | p | Trials until first success |

```python
from scipy import stats

# Bernoulli: single coin flip (p=0.5)
bern = stats.bernoulli(p=0.5)
print(bern.pmf(1))   # P(X=1) = 0.5
print(bern.mean())    # 0.5

# Binomial: 10 trials, p=0.3 — P(X=3)
binom = stats.binom(n=10, p=0.3)
print(binom.pmf(3))   # ≈ 0.2668
print(binom.cdf(3))   # P(X ≤ 3) ≈ 0.6496

# Poisson: average 4 events per hour — P(X=6)
pois = stats.poisson(mu=4)
print(pois.pmf(6))    # ≈ 0.1042

# Geometric: P(first success on 5th trial), p=0.2
geom = stats.geom(p=0.2)
print(geom.pmf(5))    # ≈ 0.0819
```

---

## 4. Continuous Distributions

Continuous distributions model outcomes over a continuous range.

| Distribution | Parameters | Use Case |
|-------------|-----------|----------|
| **Uniform** | a, b | Equally likely over [a, b] |
| **Normal (Gaussian)** | μ, σ | Natural phenomena, errors |
| **Exponential** | λ (1/scale) | Time between Poisson events |

```python
from scipy import stats

# Uniform distribution on [0, 10]
unif = stats.uniform(loc=0, scale=10)
print(unif.mean())      # 5.0
print(unif.pdf(3))      # 0.1 (constant)
print(unif.cdf(7))      # 0.7

# Normal distribution: μ=100, σ=15
norm = stats.norm(loc=100, scale=15)
print(norm.pdf(100))     # peak density ≈ 0.0266
print(norm.cdf(115))     # P(X ≤ 115) ≈ 0.8413
print(norm.ppf(0.975))   # 97.5th percentile ≈ 129.4

# Exponential distribution: λ=0.5 → scale=2
expon = stats.expon(scale=2)
print(expon.mean())      # 2.0
print(expon.cdf(3))      # P(X ≤ 3) ≈ 0.7769
```

> **Remember:** In scipy.stats the normal distribution uses `loc` (mean) and
> `scale` (standard deviation), not variance.

---

## 5. Working with scipy.stats

Every distribution in `scipy.stats` exposes a consistent API:

| Method | Description |
|--------|-----------|
| `pmf(k)` / `pdf(x)` | Probability mass / density at a point |
| `cdf(x)` | Cumulative distribution function P(X ≤ x) |
| `ppf(q)` | Percent-point (inverse CDF) — quantile for probability q |
| `rvs(size)` | Generate random variates (samples) |
| `fit(data)` | Fit distribution parameters to data (continuous) |
| `mean()` | Distribution mean |
| `var()` | Distribution variance |
| `interval(alpha)` | Confidence interval around the median |

```python
import numpy as np
from scipy import stats

# Generate 1000 samples from N(50, 10)
dist = stats.norm(loc=50, scale=10)
samples = dist.rvs(size=1000, random_state=42)

# Fit a normal distribution to the samples
mu_hat, sigma_hat = stats.norm.fit(samples)
print(f"Fitted μ={mu_hat:.2f}, σ={sigma_hat:.2f}")

# 95% confidence interval
lo, hi = dist.interval(0.95)
print(f"95% CI: [{lo:.2f}, {hi:.2f}]")

# Two-tailed z-values
z_95 = stats.norm.ppf(0.975)   # ≈ 1.96
z_99 = stats.norm.ppf(0.995)   # ≈ 2.576
```

---

## 6. Central Limit Theorem

The **Central Limit Theorem (CLT)** states that the distribution of sample
means approaches a normal distribution as the sample size grows, regardless
of the shape of the original population.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Population: highly skewed exponential (λ=1)
population = rng.exponential(scale=1.0, size=100_000)

# Draw many samples of size n and compute the mean of each
n = 30
num_samples = 5000
sample_means = np.array([
    rng.choice(population, size=n, replace=True).mean()
    for _ in range(num_samples)
])

# The sample means are approximately normal
print(f"Mean of sample means: {sample_means.mean():.4f}")
print(f"Std of sample means:  {sample_means.std():.4f}")
print(f"Theoretical SE:       {population.std() / np.sqrt(n):.4f}")

# Normality test on sample means
_, p_value = stats.normaltest(sample_means)
print(f"Normality test p-value: {p_value:.4f}")
```

> **Rule of thumb:** n ≥ 30 is often sufficient for the CLT to provide a good
> normal approximation, though highly skewed populations may need larger n.

---

## Key Takeaways
- **Probability axioms** ensure consistency: P(S) = 1, P(A) ≥ 0, and
  additivity for mutually exclusive events.
- **Bayes' Theorem** updates beliefs with new evidence — beware the base rate
  fallacy.
- **Binomial** and **Poisson** are the workhorses for discrete count data.
- The **Normal distribution** is central to statistics thanks to the CLT.
- **scipy.stats** provides a unified API (`pmf`/`pdf`, `cdf`, `ppf`, `rvs`,
  `fit`) for 100+ distributions.
- The **Central Limit Theorem** guarantees that sample means are approximately
  normal for large enough samples.

---

## Further Reading
- [SciPy — Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [SciPy — Discrete Distributions](https://docs.scipy.org/doc/scipy/tutorial/stats/discrete.html)
- [SciPy — Continuous Distributions](https://docs.scipy.org/doc/scipy/tutorial/stats/continuous.html)
- [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability/probability-library)
- [Wikipedia — Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
