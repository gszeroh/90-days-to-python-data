"""Day 26: Pandas — Data Cleaning — Examples"""

import pandas as pd
import numpy as np

# === 1. Detecting Missing Values ===
print("--- 1. Detecting Missing Values ---")

df = pd.DataFrame({
    "name": ["Alice", None, "Charlie", "Diana"],
    "score": [90, np.nan, 85, np.nan],
    "grade": ["A", "B", None, "A"],
})
print("Original DataFrame:")
print(df)
print()

print("isnull():")
print(df.isnull())
print()

print("Missing count per column:")
print(df.isnull().sum())
print()

print("Missing fraction per column:")
print(df.isnull().mean())
print()

# === 2. Handling Missing Values ===
print("--- 2. Handling Missing Values ---")

print("dropna() — remove rows with any NaN:")
print(df.dropna())
print()

print("dropna(subset=['score']) — only check 'score':")
print(df.dropna(subset=["score"]))
print()

print("fillna(0) on 'score':")
print(df["score"].fillna(0))
print()

print("fillna(mean) on 'score':")
print(df["score"].fillna(df["score"].mean()))
print()

series = pd.Series([1.0, np.nan, np.nan, 4.0, np.nan, 6.0])
print("interpolate():")
print(series.interpolate())
print()

# === 3. Removing Duplicates ===
print("--- 3. Removing Duplicates ---")

df_dup = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Bob", "Charlie"],
    "city": ["NYC", "LA", "NYC", "SF", "NYC"],
    "score": [90, 80, 90, 85, 70],
})
print("DataFrame with duplicates:")
print(df_dup)
print()

print("duplicated():")
print(df_dup.duplicated())
print()

print("duplicated(subset=['name']):")
print(df_dup.duplicated(subset=["name"]))
print()

print("drop_duplicates():")
print(df_dup.drop_duplicates())
print()

print("drop_duplicates(subset=['name'], keep='last'):")
print(df_dup.drop_duplicates(subset=["name"], keep="last"))
print()

# === 4. Type Conversion ===
print("--- 4. Type Conversion ---")

df_types = pd.DataFrame({
    "price": ["10.5", "20", "thirty", "40.1"],
    "date": ["2024-01-01", "2024-02-15", "2024-03-30", "2024-04-10"],
    "quantity": ["5", "10", "15", "20"],
})
print("Original dtypes:")
print(df_types.dtypes)
print()

df_types["quantity"] = df_types["quantity"].astype(int)
print("After astype(int) on 'quantity':")
print(df_types.dtypes)
print()

df_types["price"] = pd.to_numeric(df_types["price"], errors="coerce")
print("After to_numeric on 'price' (errors='coerce'):")
print(df_types["price"])
print()

df_types["date"] = pd.to_datetime(df_types["date"])
print("After to_datetime on 'date':")
print(df_types.dtypes)
print()

# === 5. String Operations ===
print("--- 5. String Operations ---")

names = pd.Series(["  Alice ", "BOB", "  charlie", "  Diana Lee  "])
print("Original strings:", names.tolist())

print("str.strip():", names.str.strip().tolist())
print("str.lower():", names.str.lower().tolist())
print("str.upper():", names.str.upper().tolist())
print("strip + lower:", names.str.strip().str.lower().tolist())
print()

print("str.contains('li', case=False):")
print(names.str.contains("li", case=False))
print()

print("str.replace('a', '@', case=False):")
print(names.str.replace("a", "@", case=False))
print()

emails = pd.Series(["alice@example.com", "bob@test.org", "charlie@school.edu"])
print("Extract domain from emails with str.extract:")
print(emails.str.extract(r"@(.+)\."))
print()

# === 6. Renaming & Replacing Values ===
print("--- 6. Renaming & Replacing Values ---")

df_rename = pd.DataFrame({
    "First Name": ["Alice", "Bob"],
    "Last Name": ["Smith", "Jones"],
    "Status": ["Y", "N"],
})
print("Original columns:", df_rename.columns.tolist())

df_rename.columns = df_rename.columns.str.lower().str.replace(" ", "_")
print("Cleaned columns:", df_rename.columns.tolist())
print()

print("Replace 'Y'/'N' with True/False:")
df_rename["status"] = df_rename["status"].replace({"Y": True, "N": False})
print(df_rename)
print()

df_sentinel = pd.DataFrame({"value": [10, -999, 30, -999, 50]})
print("Replace sentinel -999 with NaN:")
print(df_sentinel.replace({-999: np.nan}))
