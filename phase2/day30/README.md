# Day 30: Pandas — Time Series

## Overview

Time-series data — observations indexed by timestamps — is one of the most
common data formats in finance, IoT, web analytics, and science.  Pandas was
*built* with time series in mind and offers first-class support for:

| Capability | Key API |
|---|---|
| Parsing dates | `pd.to_datetime()`, `pd.Timestamp()` |
| Date ranges | `pd.date_range()` |
| Component access | `.dt` accessor |
| Down/up-sampling | `.resample()` |
| Smoothing | `.rolling()`, `.expanding()` |
| Lagging | `.shift()`, `.diff()`, `.pct_change()` |
| Time-zone handling | `tz_localize()`, `tz_convert()` |

---

## 1. Datetime Basics

### `pd.to_datetime()`

Convert strings, epochs, or mixed formats into proper `Timestamp` objects:

```python
import pandas as pd

pd.to_datetime("2024-03-15")                  # single string
pd.to_datetime(["2024-01-01", "2024-06-15"])   # list → DatetimeIndex
pd.to_datetime(1_700_000_000, unit="s")        # Unix epoch
```

### `pd.Timestamp`

A single point in time (nanosecond precision):

```python
ts = pd.Timestamp("2024-07-04 09:30:00")
ts.year, ts.month, ts.day_name()  # (2024, 7, 'Thursday')
```

### `pd.date_range()`

Generate a fixed-frequency `DatetimeIndex`:

```python
pd.date_range("2024-01-01", periods=6, freq="ME")   # month-end
pd.date_range("2024-01-01", "2024-12-31", freq="QE") # quarter-end
```

> 💡 **Tip:** Since pandas 2.2 the offset aliases changed — use `"ME"` (month
> end) instead of the deprecated `"M"`, and `"QE"` instead of `"Q"`.

---

## 2. DatetimeIndex & the `.dt` Accessor

When a `Series` has `datetime64` dtype you can use the `.dt` accessor to pull
out individual components:

```python
dates = pd.date_range("2024-01-01", periods=90, freq="D")
s = pd.Series(dates)

s.dt.year          # year component
s.dt.month         # month (1-12)
s.dt.day_name()    # 'Monday', 'Tuesday', …
s.dt.is_month_end  # boolean mask
```

Setting a datetime column as the index unlocks time-based slicing:

```python
df = pd.DataFrame({"value": range(90)}, index=dates)
df.loc["2024-02"]              # all February rows
df.loc["2024-01-15":"2024-02-15"]  # slice by date string
```

---

## 3. Resampling

`.resample(rule)` is the time-series equivalent of `.groupby()`.  It buckets
data by a calendar period and applies an aggregation.

| Rule | Meaning |
|---|---|
| `"D"` | Calendar day |
| `"W"` | Week (Sunday end) |
| `"ME"` | Month end |
| `"QE"` | Quarter end |
| `"YE"` | Year end |

### Down-sampling (higher → lower frequency)

```python
daily = pd.Series(range(90), index=pd.date_range("2024-01-01", periods=90, freq="D"))
daily.resample("ME").sum()     # monthly totals
daily.resample("W").mean()     # weekly averages
```

### Up-sampling (lower → higher frequency)

```python
monthly = daily.resample("ME").sum()
monthly.resample("D").ffill()  # forward-fill to daily
```

> ⚠️ **Warning:** Up-sampling introduces rows with no observed data.  Always
> choose an appropriate fill method (`ffill`, `bfill`, or `interpolate`).

---

## 4. Rolling & Expanding Windows

### Rolling window

`.rolling(window)` computes statistics over a sliding window of fixed size:

```python
s = pd.Series([1, 3, 5, 7, 9, 11])
s.rolling(window=3).mean()   # NaN, NaN, 3.0, 5.0, 7.0, 9.0
```

Common parameters:

| Parameter | Description |
|---|---|
| `window` | Number of observations |
| `min_periods` | Minimum non-NaN values required |
| `center` | Centre the window label |

### Expanding window

`.expanding()` grows from the first observation — useful for cumulative stats:

```python
s.expanding().mean()  # cumulative mean
```

---

## 5. Shifting & Differencing

### `shift()`

Move data forward or backward by *n* periods without changing the index:

```python
s = pd.Series([100, 110, 105, 120])
s.shift(1)   # [NaN, 100, 110, 105]  — previous value
s.shift(-1)  # [110, 105, 120, NaN]  — next value
```

### `diff()`

Difference between current and *n*-th prior element:

```python
s.diff()     # [NaN, 10, -5, 15]
```

### `pct_change()`

Percentage change between current and *n*-th prior element:

```python
s.pct_change()  # [NaN, 0.10, -0.0454…, 0.1428…]
```

> 💡 **Tip:** `pct_change()` is equivalent to `s.diff() / s.shift()`.

---

## 6. Time Zones

Pandas can localize naive timestamps and convert between zones:

```python
ts = pd.Timestamp("2024-07-04 12:00")

ts_utc = ts.tz_localize("UTC")
ts_eastern = ts_utc.tz_convert("US/Eastern")   # 08:00 EDT

idx = pd.date_range("2024-01-01", periods=3, freq="D", tz="Europe/London")
idx.tz_convert("Asia/Tokyo")
```

> ⚠️ **Warning:** Always localize before converting.  Calling `tz_convert()`
> on a timezone-naive object raises `TypeError`.

---

## Key Takeaways

- **`pd.to_datetime()`** parses almost any date representation into `Timestamp`.
- **`DatetimeIndex`** enables powerful date-string slicing and frequency-based operations.
- **`.resample()`** groups by calendar period — use `"D"`, `"W"`, `"ME"`, `"QE"` rules.
- **`.rolling()` / `.expanding()`** compute windowed statistics for smoothing and cumulative analysis.
- **`.shift()`, `.diff()`, `.pct_change()`** are essential for lag, difference, and growth-rate calculations.
- **Time-zone handling** requires a localize-then-convert workflow.

## Further Reading

- [Pandas — Time Series / Date Functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Pandas — `resample` API](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)
- [Pandas — Window Functions](https://pandas.pydata.org/docs/user_guide/window.html)
- [Pandas — Time Deltas](https://pandas.pydata.org/docs/user_guide/timedeltas.html)
- [Real Python — Time Series with Pandas](https://realpython.com/pandas-time-series/)
