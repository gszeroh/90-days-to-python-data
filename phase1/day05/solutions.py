"""
Day 05: Control Flow — Conditionals — Solutions
"""


# === Exercise 1: Absolute Value ===

def absolute_value(n):
    """Return the absolute value of `n` without using the built-in abs().

    Use an if/else statement.

    Examples:
        absolute_value(5)   -> 5
        absolute_value(-3)  -> 3
        absolute_value(0)   -> 0
    """
    if n < 0:
        return -n
    return n


# === Exercise 2: Grade Calculator ===

def letter_grade(score):
    """Return the letter grade for a numeric score.

    Grading scale:
        90-100 → "A"
        80-89  → "B"
        70-79  → "C"
        60-69  → "D"
        0-59   → "F"

    If score is outside 0-100, return "Invalid".

    Examples:
        letter_grade(95)  -> "A"
        letter_grade(83)  -> "B"
        letter_grade(72)  -> "C"
        letter_grade(61)  -> "D"
        letter_grade(45)  -> "F"
        letter_grade(-5)  -> "Invalid"
        letter_grade(105) -> "Invalid"
    """
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# === Exercise 3: Fizz Buzz ===

def fizz_buzz(n):
    """Return a string based on the Fizz Buzz rules:

    - If n is divisible by both 3 and 5, return "FizzBuzz"
    - If n is divisible by 3 only, return "Fizz"
    - If n is divisible by 5 only, return "Buzz"
    - Otherwise, return the number as a string

    Examples:
        fizz_buzz(15)  -> "FizzBuzz"
        fizz_buzz(9)   -> "Fizz"
        fizz_buzz(10)  -> "Buzz"
        fizz_buzz(7)   -> "7"
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


# === Exercise 4: Ticket Price ===

def ticket_price(age, is_student):
    """Calculate ticket price based on age and student status.

    Rules:
        - Children (under 12): $5
        - Seniors (65 and over): $7
        - Students (any age 12-64 with is_student=True): $8
        - Regular adults (12-64, not student): $12

    Return the price as an integer.

    Examples:
        ticket_price(8, False)   -> 5
        ticket_price(70, False)  -> 7
        ticket_price(20, True)   -> 8
        ticket_price(35, False)  -> 12
    """
    if age < 12:
        return 5
    elif age >= 65:
        return 7
    elif is_student:
        return 8
    else:
        return 12


# === Exercise 5: Season Finder ===

def get_season(month):
    """Return the season for a given month number (1-12).

    Seasons (Northern Hemisphere):
        Spring: 3, 4, 5
        Summer: 6, 7, 8
        Autumn: 9, 10, 11
        Winter: 12, 1, 2

    If month is not 1-12, return "Invalid".

    Examples:
        get_season(3)  -> "Spring"
        get_season(7)  -> "Summer"
        get_season(10) -> "Autumn"
        get_season(1)  -> "Winter"
        get_season(13) -> "Invalid"
    """
    if month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Autumn"
    elif month in (12, 1, 2):
        return "Winter"
    else:
        return "Invalid"
