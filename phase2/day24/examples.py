"""Day 24: Pandas — Series & DataFrames — Examples"""

import pandas as pd
import numpy as np


# === Series Creation ===

print("--- Series from a list ---")
s1 = pd.Series([10, 20, 30, 40])
print(s1)
print("dtype:", s1.dtype)

print("\n--- Series with custom index ---")
s2 = pd.Series([100, 200, 300], index=["x", "y", "z"])
print(s2)

print("\n--- Series from a dictionary ---")
s3 = pd.Series({"apples": 3, "bananas": 5, "cherries": 12})
print(s3)

print("\n--- Series from a scalar ---")
s4 = pd.Series(7, index=["a", "b", "c"])
print(s4)


# === Series Indexing ===

print("\n--- Series indexing ---")
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("s['b']       :", s["b"])
print("s['a':'c']   :\n", s["a":"c"])
print("s[s > 15]    :\n", s[s > 15])


# === Series Methods ===

print("\n--- Series methods ---")
print("values      :", s.values)
print("index       :", s.index.tolist())
print("mean        :", s.mean())
print("sum         :", s.sum())
print("describe:\n", s.describe())

print("\n--- unique & value_counts ---")
s5 = pd.Series(["a", "b", "a", "c", "b", "a"])
print("unique      :", s5.unique())
print("value_counts:\n", s5.value_counts())


# === DataFrame Creation from Dict of Lists ===

print("\n--- DataFrame from dict of lists ---")
df = pd.DataFrame({
    "name":  ["Alice", "Bob", "Charlie", "Diana"],
    "age":   [25, 30, 35, 28],
    "score": [88.5, 92.0, 78.3, 95.1],
})
print(df)
print("\nshape  :", df.shape)
print("columns:", df.columns.tolist())
print("dtypes:\n", df.dtypes)


# === DataFrame from List of Dicts ===

print("\n--- DataFrame from list of dicts ---")
records = [
    {"city": "Seattle", "temp": 58},
    {"city": "Portland", "temp": 62},
    {"city": "San Francisco", "temp": 65},
]
df_cities = pd.DataFrame(records)
print(df_cities)


# === DataFrame from NumPy Array ===

print("\n--- DataFrame from NumPy array ---")
arr = np.arange(12).reshape(4, 3)
df_np = pd.DataFrame(arr, columns=["x", "y", "z"])
print(df_np)


# === Selecting Data: [] ===

print("\n--- Column selection with [] ---")
print("df['name']:\n", df["name"])
print("\ndf[['name', 'score']]:\n", df[["name", "score"]])


# === Selecting Data: .loc[] (label-based) ===

print("\n--- .loc[] (label-based) ---")
print("df.loc[0]:\n", df.loc[0])
print("\ndf.loc[0:2, 'name']:\n", df.loc[0:2, "name"])
print("\ndf.loc[:, ['name', 'score']]:\n", df.loc[:, ["name", "score"]])


# === Selecting Data: .iloc[] (integer position) ===

print("\n--- .iloc[] (integer position) ---")
print("df.iloc[0]:\n", df.iloc[0])
print("\ndf.iloc[0:2]:\n", df.iloc[0:2])
print("\ndf.iloc[0:2, 0:2]:\n", df.iloc[0:2, 0:2])
print("\ndf.iloc[:, -1]:\n", df.iloc[:, -1])


# === Boolean Selection ===

print("\n--- Boolean selection ---")
print("age > 28:\n", df[df["age"] > 28])
print("\nscore >= 90, name:\n", df.loc[df["score"] >= 90, "name"])


# === Adding & Removing Columns ===

print("\n--- Adding columns ---")
df["passed"] = df["score"] >= 80
df["score_pct"] = df["score"] / 100
print(df)

print("\n--- Removing a column ---")
df = df.drop(columns=["score_pct"])
print(df)

print("\n--- Renaming columns ---")
df_renamed = df.rename(columns={"name": "student_name"})
print(df_renamed.columns.tolist())


# === Data Types & Conversion ===

print("\n--- dtypes ---")
print(df.dtypes)

print("\n--- astype conversions ---")
df["age_float"] = df["age"].astype(float)
df["score_int"] = df["score"].astype(int)
df["age_str"] = df["age"].astype(str)
print(df.dtypes)

print("\n--- Nullable integer ---")
s_nullable = pd.array([1, 2, None, 4], dtype="Int64")
print("Nullable Int64:", s_nullable)
print("dtype:", s_nullable.dtype)
