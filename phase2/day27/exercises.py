"""
Day 27: Pandas — Data Transformation — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

import pandas as pd
import numpy as np


# === Exercise 1: Apply a Custom Function to a Column ===

def apply_discount(df, col, pct):
    """Apply a percentage discount to a numeric column using apply().

    Args:
        df (pd.DataFrame): Input DataFrame.
        col (str): Name of the numeric column to discount.
        pct (float): Discount percentage (e.g. 10 means 10 %).

    Returns:
        pd.DataFrame: New DataFrame with the column values reduced by *pct* %.

    Examples:
        df = pd.DataFrame({"price": [100, 200, 50]})
        apply_discount(df, "price", 10)
        ->    price
           0   90.0
           1  180.0
           2   45.0
    """
    pass


# === Exercise 2: Map Values with a Dictionary ===

def map_grades(series):
    """Map letter grades to descriptive labels using Series.map().

    Mapping:
        "A" -> "Excellent", "B" -> "Good", "C" -> "Average",
        "D" -> "Below Average", "F" -> "Failing"

    Args:
        series (pd.Series): Series of single-letter grades.

    Returns:
        pd.Series: Series with descriptive labels. Unrecognised grades
        become NaN.

    Examples:
        map_grades(pd.Series(["A", "C", "F"]))
        -> 0    Excellent
           1      Average
           2      Failing
    """
    pass


# === Exercise 3: Rename Columns with a Pattern ===

def clean_column_names(df):
    """Standardise column names: lowercase, spaces replaced with underscores.

    Args:
        df (pd.DataFrame): Input DataFrame with arbitrary column names.

    Returns:
        pd.DataFrame: New DataFrame whose column names are lowercased with
        spaces replaced by underscores.

    Examples:
        df = pd.DataFrame({"First Name": [1], "Last Name": [2], "AGE": [3]})
        clean_column_names(df).columns.tolist()
        -> ['first_name', 'last_name', 'age']
    """
    pass


# === Exercise 4: Use assign() for Computed Columns ===

def add_bmi_columns(df):
    """Add BMI and BMI category columns using assign().

    BMI = weight_kg / (height_m ** 2)

    Categories (use these exact strings):
        BMI < 18.5        -> "Underweight"
        18.5 <= BMI < 25  -> "Normal"
        25 <= BMI < 30    -> "Overweight"
        BMI >= 30         -> "Obese"

    Args:
        df (pd.DataFrame): Must contain 'weight_kg' and 'height_m' columns.

    Returns:
        pd.DataFrame: New DataFrame with added 'bmi' (float) and 'category'
        (str) columns.

    Examples:
        df = pd.DataFrame({"weight_kg": [70, 90], "height_m": [1.75, 1.60]})
        result = add_bmi_columns(df)
        result["bmi"].round(1).tolist()
        -> [22.9, 35.2]
        result["category"].tolist()
        -> ['Normal', 'Obese']
    """
    pass


# === Exercise 5: Transformation Pipeline with Method Chaining ===

def sales_pipeline(df):
    """Build a full transformation pipeline using method chaining.

    Steps (in order):
    1. replace() — In the 'region' column, replace "NA" with "North America".
    2. assign()  — Add a 'revenue' column equal to price * quantity.
    3. assign()  — Add a 'tax' column equal to revenue * 0.08.
    4. assign()  — Add a 'total' column equal to revenue + tax.
    5. rename()  — Uppercase all column names.

    Args:
        df (pd.DataFrame): Must contain columns 'region', 'price',
            and 'quantity'.

    Returns:
        pd.DataFrame: Transformed DataFrame with uppercased column names and
        the three new numeric columns.

    Examples:
        df = pd.DataFrame({
            "region": ["NA", "EU"],
            "price": [100, 200],
            "quantity": [2, 3]
        })
        result = sales_pipeline(df)
        result.columns.tolist()
        -> ['REGION', 'PRICE', 'QUANTITY', 'REVENUE', 'TAX', 'TOTAL']
        result["REGION"].tolist()
        -> ['North America', 'EU']
        result["TOTAL"].tolist()
        -> [216.0, 648.0]
    """
    pass
