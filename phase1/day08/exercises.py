"""
Day 08: Functions — Advanced — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""

from functools import wraps


# === Exercise 1: Flexible Average ===

def average(*args):
    """Return the average of all given numbers.

    Accept any number of positional numeric arguments.
    Return 0 if no arguments are provided.
    Return the result as a float.

    Examples:
        average(10, 20, 30)    -> 20.0
        average(5)             -> 5.0
        average(1, 2, 3, 4, 5) -> 3.0
        average()              -> 0
    """
    pass


# === Exercise 2: Apply Functions ===

def apply_functions(value, *functions):
    """Apply a series of functions to a value, left to right.

    Take an initial value and any number of functions. Apply each function
    to the result of the previous one, starting with the initial value.

    Examples:
        apply_functions(5, lambda x: x * 2, lambda x: x + 3)  -> 13
        apply_functions("hello", str.upper, lambda s: s + "!")  -> "HELLO!"
        apply_functions(10)  -> 10
    """
    pass


# === Exercise 3: Map and Filter Pipeline ===

def get_long_uppercased(words, min_length):
    """Return a sorted list of uppercased words longer than min_length.

    Use map() and filter() (not list comprehensions).

    Steps:
        1. Filter words that have length > min_length
        2. Convert remaining words to uppercase using map
        3. Return the result sorted alphabetically

    Examples:
        get_long_uppercased(["hi", "hello", "hey", "howdy"], 3)
            -> ["HELLO", "HOWDY"]

        get_long_uppercased(["a", "bb", "ccc", "dddd"], 2)
            -> ["CCC", "DDDD"]

        get_long_uppercased(["short", "tiny"], 10)
            -> []
    """
    pass


# === Exercise 4: Closure Counter ===

def make_accumulator(initial=0):
    """Return a function that accumulates values.

    The returned function accepts a number and adds it to a running total
    (starting from `initial`). Each call returns the new total.

    Use a closure with nonlocal.

    Examples:
        acc = make_accumulator()
        acc(5)   -> 5
        acc(10)  -> 15
        acc(3)   -> 18

        acc2 = make_accumulator(100)
        acc2(10) -> 110
        acc2(20) -> 130
    """
    pass


# === Exercise 5: Retry Decorator ===

def retry(max_attempts=3):
    """Return a decorator that retries a function up to max_attempts times.

    If the function raises an exception, catch it and try again.
    If all attempts fail, re-raise the last exception.
    If the function succeeds, return the result immediately.

    Use functools.wraps to preserve function metadata.

    Examples:
        call_count = 0

        @retry(max_attempts=3)
        def flaky():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("Not yet!")
            return "Success"

        flaky()  -> "Success"  (called 3 times total)

        @retry(max_attempts=1)
        def always_fails():
            raise RuntimeError("Oops")

        always_fails()  # Raises RuntimeError after 1 attempt
    """
    pass
