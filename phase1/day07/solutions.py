"""
Day 07: Functions — Basics — Solutions
"""


# === Exercise 1: Factorial ===

def factorial(n):
    """Return the factorial of a non-negative integer n.

    The factorial of n (written n!) is the product of all positive integers
    from 1 to n. By definition, 0! = 1.

    Use a loop (not recursion).

    If n is negative, return -1.

    Examples:
        factorial(0)  -> 1
        factorial(1)  -> 1
        factorial(5)  -> 120
        factorial(10) -> 3628800
        factorial(-3) -> -1
    """
    if n < 0:
        return -1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# === Exercise 2: Fibonacci ===

def fibonacci(n):
    """Return a list of the first n Fibonacci numbers.

    The Fibonacci sequence starts with 0, 1, and each subsequent number
    is the sum of the two preceding numbers.

    If n <= 0, return an empty list.

    Examples:
        fibonacci(0)  -> []
        fibonacci(1)  -> [0]
        fibonacci(2)  -> [0, 1]
        fibonacci(7)  -> [0, 1, 1, 2, 3, 5, 8]
        fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# === Exercise 3: Temperature Converter ===

def convert_temperature(value, from_scale, to_scale):
    """Convert a temperature between Celsius, Fahrenheit, and Kelvin.

    Supported scales: "C" (Celsius), "F" (Fahrenheit), "K" (Kelvin).

    Conversion formulas:
        C to F: F = C * 9/5 + 32
        C to K: K = C + 273.15
        F to C: C = (F - 32) * 5/9
        F to K: K = (F - 32) * 5/9 + 273.15
        K to C: C = K - 273.15
        K to F: F = (K - 273.15) * 9/5 + 32

    If from_scale equals to_scale, return the value unchanged.
    Return the result rounded to 2 decimal places.

    Examples:
        convert_temperature(100, "C", "F") -> 212.0
        convert_temperature(32, "F", "C")  -> 0.0
        convert_temperature(0, "C", "K")   -> 273.15
        convert_temperature(72, "F", "F")  -> 72
    """
    if from_scale == to_scale:
        return value

    # Convert to Celsius first
    if from_scale == "C":
        celsius = value
    elif from_scale == "F":
        celsius = (value - 32) * 5 / 9
    elif from_scale == "K":
        celsius = value - 273.15

    # Convert from Celsius to target
    if to_scale == "C":
        result = celsius
    elif to_scale == "F":
        result = celsius * 9 / 5 + 32
    elif to_scale == "K":
        result = celsius + 273.15

    return round(result, 2)


# === Exercise 4: Palindrome Checker ===

def is_palindrome(text):
    """Return True if text is a palindrome, False otherwise.

    A palindrome reads the same forwards and backwards.
    The check should be case-insensitive and ignore spaces.

    Examples:
        is_palindrome("racecar")       -> True
        is_palindrome("hello")         -> False
        is_palindrome("A man a plan a canal Panama") -> True
        is_palindrome("Was it a car or a cat I saw")  -> True
        is_palindrome("")              -> True
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# === Exercise 5: BMI Calculator ===

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI and return a tuple of (bmi_value, category).

    BMI formula: weight_kg / (height_m ** 2)

    Categories:
        BMI < 18.5       → "Underweight"
        18.5 <= BMI < 25 → "Normal"
        25 <= BMI < 30   → "Overweight"
        BMI >= 30        → "Obese"

    Return the BMI rounded to 1 decimal place.

    If weight or height is <= 0, return (0.0, "Invalid").

    Examples:
        calculate_bmi(70, 1.75)  -> (22.9, "Normal")
        calculate_bmi(50, 1.80)  -> (15.4, "Underweight")
        calculate_bmi(90, 1.70)  -> (31.1, "Obese")
        calculate_bmi(0, 1.75)   -> (0.0, "Invalid")
    """
    if weight_kg <= 0 or height_m <= 0:
        return (0.0, "Invalid")

    bmi = round(weight_kg / (height_m ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return (bmi, category)
