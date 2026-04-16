"""
Day 04: Operators & Expressions — Solutions
"""


# === Exercise 1: Even or Odd ===

def is_even(n):
    """Return True if `n` is even, False otherwise.

    Use the modulo operator.

    Examples:
        is_even(4)  -> True
        is_even(7)  -> False
        is_even(0)  -> True
    """
    return n % 2 == 0


# === Exercise 2: Within Range ===

def within_range(value, low, high):
    """Return True if `value` is between `low` and `high` (inclusive).

    Use a chained comparison.

    Examples:
        within_range(5, 1, 10)  -> True
        within_range(0, 1, 10)  -> False
        within_range(10, 1, 10) -> True
    """
    return low <= value <= high


# === Exercise 3: Leap Year ===

def is_leap_year(year):
    """Return True if `year` is a leap year, False otherwise.

    Leap year rules:
        - Divisible by 4 AND
        - NOT divisible by 100, UNLESS also divisible by 400

    Examples:
        is_leap_year(2000) -> True   (divisible by 400)
        is_leap_year(1900) -> False  (divisible by 100 but not 400)
        is_leap_year(2024) -> True   (divisible by 4, not by 100)
        is_leap_year(2023) -> False  (not divisible by 4)
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# === Exercise 4: Calculate Expression ===

def calculate(a, b, operator):
    """Perform the arithmetic operation specified by `operator` on `a` and `b`.

    Supported operators: '+', '-', '*', '/', '//', '%', '**'
    If the operator is not recognized, return None.
    For '/' and '//', if b is 0, return None.

    Examples:
        calculate(10, 3, '+')  -> 13
        calculate(10, 3, '/')  -> 3.3333333333333335
        calculate(10, 3, '//') -> 3
        calculate(10, 0, '/')  -> None
        calculate(2, 10, '**') -> 1024
        calculate(10, 3, '^')  -> None
    """
    if operator in ('/', '//') and b == 0:
        return None

    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '**': a ** b,
        '%': a % b if b != 0 else None,
    }

    if operator == '/':
        return a / b
    elif operator == '//':
        return a // b
    else:
        return operations.get(operator)


# === Exercise 5: Clamp Value ===

def clamp(value, minimum, maximum):
    """Clamp `value` so that it falls within [minimum, maximum].

    If value < minimum, return minimum.
    If value > maximum, return maximum.
    Otherwise, return value.

    Use comparison operators (no if/elif/else — try using min/max builtins).

    Examples:
        clamp(5, 0, 10)   -> 5
        clamp(-3, 0, 10)  -> 0
        clamp(15, 0, 10)  -> 10
    """
    return max(minimum, min(value, maximum))
