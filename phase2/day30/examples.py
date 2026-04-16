"""Day 30: Pandas — Time Series — Examples"""

import pandas as pd
import numpy as np

# === 1. Datetime Basics ===

print("--- pd.to_datetime() ---")
print(pd.to_datetime("2024-03-15"))
print(pd.to_datetime(["2024-01-01", "2024-06-15"]))
print(pd.to_datetime(1_700_000_000, unit="s"))

print("\n--- pd.Timestamp ---")
ts = pd.Timestamp("2024-07-04 09:30:00")
print(f"Year: {ts.year}, Month: {ts.month}, Day name: {ts.day_name()}")

print("\n--- pd.date_range() ---")
print(pd.date_range("2024-01-01", periods=6, freq="ME"))
print(pd.date_range("2024-01-01", "2024-12-31", freq="QE"))

# === 2. DatetimeIndex & dt Accessor ===

print("\n--- .dt accessor ---")
dates = pd.date_range("2024-01-01", periods=10, freq="D")
s = pd.Series(dates)
print("Year:\n", s.dt.year)
print("Day name:\n", s.dt.day_name())

print("\n--- Date-string slicing ---")
df = pd.DataFrame({"value": range(90)},
                   index=pd.date_range("2024-01-01", periods=90, freq="D"))
print("February rows:\n", df.loc["2024-02"].head())

# === 3. Resampling ===

print("\n--- Down-sampling: monthly sum ---")
daily = pd.Series(
    np.random.default_rng(42).integers(10, 100, size=90),
    index=pd.date_range("2024-01-01", periods=90, freq="D"),
)
print(daily.resample("ME").sum())

print("\n--- Down-sampling: weekly mean ---")
print(daily.resample("W").mean().head())

print("\n--- Up-sampling with forward fill ---")
monthly = daily.resample("ME").sum()
print(monthly.resample("D").ffill().head(10))

# === 4. Rolling & Expanding Windows ===

print("\n--- Rolling mean (window=7) ---")
print(daily.rolling(window=7).mean().head(10))

print("\n--- Rolling std (window=7) ---")
print(daily.rolling(window=7).std().head(10))

print("\n--- Expanding mean ---")
print(daily.expanding().mean().head(10))

# === 5. Shifting & Differencing ===

print("\n--- shift(1) — previous value ---")
small = pd.Series([100, 110, 105, 120, 130],
                   index=pd.date_range("2024-01-01", periods=5, freq="D"))
print(small.shift(1))

print("\n--- diff() — period difference ---")
print(small.diff())

print("\n--- pct_change() — growth rate ---")
print(small.pct_change())

# === 6. Time Zones ===

print("\n--- Localize & convert ---")
ts_naive = pd.Timestamp("2024-07-04 12:00")
ts_utc = ts_naive.tz_localize("UTC")
ts_eastern = ts_utc.tz_convert("US/Eastern")
print(f"UTC:     {ts_utc}")
print(f"Eastern: {ts_eastern}")

print("\n--- DatetimeIndex with timezone ---")
idx = pd.date_range("2024-01-01", periods=3, freq="D", tz="Europe/London")
print("London:", idx)
print("Tokyo: ", idx.tz_convert("Asia/Tokyo"))
