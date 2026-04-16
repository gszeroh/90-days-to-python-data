"""Day 36: Statistics — Probability & Distributions — Examples"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# === 1. Probability Basics ===

print("--- 1. Probability Basics ---")

# Complement rule: P(Aᶜ) = 1 - P(A)
p_rain = 0.3
p_no_rain = 1 - p_rain
print(f"P(rain) = {p_rain}, P(no rain) = {p_no_rain}")

# Addition rule: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
p_a, p_b, p_a_and_b = 0.4, 0.5, 0.2
p_a_or_b = p_a + p_b - p_a_and_b
print(f"P(A ∪ B) = {p_a} + {p_b} - {p_a_and_b} = {p_a_or_b}")

# Multiplication rule (independent): P(A ∩ B) = P(A) · P(B)
p_heads = 0.5
p_two_heads = p_heads * p_heads
print(f"P(two heads) = {p_heads} × {p_heads} = {p_two_heads}")

# === 2. Conditional Probability & Bayes' Theorem ===

print("\n--- 2. Conditional Probability & Bayes' Theorem ---")

prior = 0.01           # P(disease)
sensitivity = 0.99     # P(positive | disease)
false_pos = 0.05       # P(positive | no disease)

p_positive = sensitivity * prior + false_pos * (1 - prior)
posterior = (sensitivity * prior) / p_positive

print(f"Prior P(disease)       = {prior}")
print(f"P(positive test)       = {p_positive:.4f}")
print(f"Posterior P(disease|+)  = {posterior:.4f}")
print("Even a 99% sensitive test gives only ~17% posterior with 1% prevalence!")

# === 3. Discrete Distributions ===

print("\n--- 3. Discrete Distributions ---")

# Bernoulli
bern = stats.bernoulli(p=0.7)
print(f"Bernoulli(p=0.7): P(X=1) = {bern.pmf(1):.4f}, mean = {bern.mean():.2f}")

# Binomial: 20 coin flips, P(heads)=0.5
binom_dist = stats.binom(n=20, p=0.5)
print(f"Binom(n=20, p=0.5): P(X=10) = {binom_dist.pmf(10):.4f}")
print(f"  P(X ≤ 10)  = {binom_dist.cdf(10):.4f}")
print(f"  Mean = {binom_dist.mean():.1f}, Var = {binom_dist.var():.1f}")

# Poisson: average 3 emails per minute
pois_dist = stats.poisson(mu=3)
print(f"Poisson(μ=3): P(X=5) = {pois_dist.pmf(5):.4f}")
print(f"  P(X ≤ 5)  = {pois_dist.cdf(5):.4f}")

# Geometric: trials until first success, p=0.3
geom_dist = stats.geom(p=0.3)
print(f"Geom(p=0.3): P(first success on trial 4) = {geom_dist.pmf(4):.4f}")
print(f"  Mean trials until success = {geom_dist.mean():.2f}")

# Plot discrete distributions
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

k_binom = np.arange(0, 21)
axes[0].bar(k_binom, binom_dist.pmf(k_binom), color="steelblue", alpha=0.8)
axes[0].set_title("Binomial(n=20, p=0.5)")
axes[0].set_xlabel("k")
axes[0].set_ylabel("P(X=k)")

k_pois = np.arange(0, 15)
axes[1].bar(k_pois, pois_dist.pmf(k_pois), color="coral", alpha=0.8)
axes[1].set_title("Poisson(μ=3)")
axes[1].set_xlabel("k")
axes[1].set_ylabel("P(X=k)")

k_geom = np.arange(1, 16)
axes[2].bar(k_geom, geom_dist.pmf(k_geom), color="mediumseagreen", alpha=0.8)
axes[2].set_title("Geometric(p=0.3)")
axes[2].set_xlabel("k")
axes[2].set_ylabel("P(X=k)")

plt.tight_layout()
plt.savefig("discrete_distributions.png", dpi=100, bbox_inches="tight")
plt.close()
print("\nSaved: discrete_distributions.png")

# === 4. Continuous Distributions ===

print("\n--- 4. Continuous Distributions ---")

# Uniform
unif = stats.uniform(loc=0, scale=10)
print(f"Uniform(0, 10): mean = {unif.mean():.1f}, P(X ≤ 7) = {unif.cdf(7):.2f}")

# Normal (Gaussian)
norm_dist = stats.norm(loc=100, scale=15)
print(f"Normal(μ=100, σ=15):")
print(f"  P(X ≤ 115) = {norm_dist.cdf(115):.4f}")
print(f"  P(85 ≤ X ≤ 115) = {norm_dist.cdf(115) - norm_dist.cdf(85):.4f}")
print(f"  95th percentile = {norm_dist.ppf(0.95):.2f}")

# Exponential
expon_dist = stats.expon(scale=2)
print(f"Exponential(λ=0.5, scale=2): mean = {expon_dist.mean():.1f}")
print(f"  P(X ≤ 3) = {expon_dist.cdf(3):.4f}")

# Plot continuous distributions
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

x_unif = np.linspace(-1, 11, 300)
axes[0].plot(x_unif, unif.pdf(x_unif), "steelblue", lw=2)
axes[0].fill_between(x_unif, unif.pdf(x_unif), alpha=0.3, color="steelblue")
axes[0].set_title("Uniform(0, 10)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")

x_norm = np.linspace(50, 150, 300)
axes[1].plot(x_norm, norm_dist.pdf(x_norm), "coral", lw=2)
axes[1].fill_between(x_norm, norm_dist.pdf(x_norm), alpha=0.3, color="coral")
axes[1].axvline(100, color="gray", ls="--", label="μ=100")
axes[1].set_title("Normal(μ=100, σ=15)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("f(x)")
axes[1].legend()

x_exp = np.linspace(0, 10, 300)
axes[2].plot(x_exp, expon_dist.pdf(x_exp), "mediumseagreen", lw=2)
axes[2].fill_between(x_exp, expon_dist.pdf(x_exp), alpha=0.3, color="mediumseagreen")
axes[2].set_title("Exponential(scale=2)")
axes[2].set_xlabel("x")
axes[2].set_ylabel("f(x)")

plt.tight_layout()
plt.savefig("continuous_distributions.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: continuous_distributions.png")

# === 5. Working with scipy.stats ===

print("\n--- 5. Working with scipy.stats ---")

# Generate samples and fit
dist = stats.norm(loc=50, scale=10)
samples = dist.rvs(size=1000, random_state=42)
mu_hat, sigma_hat = stats.norm.fit(samples)
print(f"True parameters:   μ=50, σ=10")
print(f"Fitted parameters: μ={mu_hat:.2f}, σ={sigma_hat:.2f}")

# Confidence interval
lo, hi = dist.interval(0.95)
print(f"95% CI: [{lo:.2f}, {hi:.2f}]")

# Common z-values via ppf
for confidence in [0.90, 0.95, 0.99]:
    z = stats.norm.ppf(1 - (1 - confidence) / 2)
    print(f"  z for {confidence:.0%} confidence: {z:.4f}")

# CDF and survival function
x_val = 65
print(f"\nFor N(50, 10) at x={x_val}:")
print(f"  CDF  P(X ≤ {x_val}) = {dist.cdf(x_val):.4f}")
print(f"  SF   P(X > {x_val}) = {dist.sf(x_val):.4f}")

# === 6. Central Limit Theorem ===

print("\n--- 6. Central Limit Theorem ---")

rng = np.random.default_rng(42)

# Skewed population: Exponential(scale=2)
population = rng.exponential(scale=2.0, size=100_000)
pop_mean = population.mean()
pop_std = population.std()
print(f"Population (Exponential): mean={pop_mean:.4f}, std={pop_std:.4f}")

# Draw samples of increasing size and collect means
sample_sizes = [5, 30, 100]
num_samples = 5000

fig, axes = plt.subplots(1, len(sample_sizes), figsize=(15, 4))

for ax, n in zip(axes, sample_sizes):
    means = np.array([
        rng.choice(population, size=n, replace=True).mean()
        for _ in range(num_samples)
    ])
    theoretical_se = pop_std / np.sqrt(n)

    ax.hist(means, bins=50, density=True, alpha=0.7, color="steelblue",
            edgecolor="white", label="Sample means")

    # Overlay theoretical normal
    x_range = np.linspace(means.min(), means.max(), 200)
    ax.plot(x_range, stats.norm.pdf(x_range, pop_mean, theoretical_se),
            "r-", lw=2, label="Normal approx.")

    ax.set_title(f"n = {n}")
    ax.set_xlabel("Sample mean")
    ax.legend(fontsize=8)

    print(f"  n={n:>3}: mean of means={means.mean():.4f}, "
          f"std={means.std():.4f}, theoretical SE={theoretical_se:.4f}")

fig.suptitle("Central Limit Theorem — Exponential Population", y=1.02,
             fontsize=13)
plt.tight_layout()
plt.savefig("central_limit_theorem.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: central_limit_theorem.png")

print("\n✅ All examples completed.")
