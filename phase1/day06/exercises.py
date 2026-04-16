"""
Day 06: Control Flow — Loops — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""


# === Exercise 1: Sum of Range ===

def sum_range(start, end):
    """Return the sum of all integers from start to end (inclusive).

    Use a for loop with range().

    Examples:
        sum_range(1, 5)   -> 15
        sum_range(3, 7)   -> 25
        sum_range(10, 10) -> 10
        sum_range(0, 0)   -> 0
    """
    pass


# === Exercise 2: FizzBuzz List ===

def fizzbuzz_list(n):
    """Return a list of FizzBuzz results from 1 to n (inclusive).

    Rules for each number:
        - Divisible by both 3 and 5 → "FizzBuzz"
        - Divisible by 3 only → "Fizz"
        - Divisible by 5 only → "Buzz"
        - Otherwise → the number as a string

    Use a for loop to build the list.

    Examples:
        fizzbuzz_list(5)  -> ["1", "2", "Fizz", "4", "Buzz"]
        fizzbuzz_list(15) -> ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
                              "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    """
    pass


# === Exercise 3: Right Triangle Pattern ===

def right_triangle(rows):
    """Return a string of a right-aligned triangle made of '*' characters.

    Each row i (starting at 1) has i stars, right-aligned to `rows` width.
    Rows are separated by newline characters. No trailing newline.

    Use nested loops or string multiplication.

    Examples:
        right_triangle(3) -> "  *\\n **\\n***"
            Which prints as:
              *
             **
            ***

        right_triangle(5) -> "    *\\n   **\\n  ***\\n ****\\n*****"
    """
    pass


# === Exercise 4: Find First Duplicate ===

def first_duplicate(items):
    """Return the first element that appears more than once in the list.

    Iterate through the list and keep track of elements you've seen.
    Return None if there are no duplicates.

    Examples:
        first_duplicate([1, 2, 3, 2, 1])     -> 2
        first_duplicate(["a", "b", "c", "b"]) -> "b"
        first_duplicate([1, 2, 3, 4])         -> None
        first_duplicate([])                    -> None
    """
    pass


# === Exercise 5: Collatz Steps ===

def collatz_steps(n):
    """Return the number of steps to reach 1 using the Collatz sequence.

    Starting from n, apply these rules repeatedly:
        - If n is even: n = n // 2
        - If n is odd:  n = 3 * n + 1

    Count how many steps it takes to reach 1. If n is already 1, return 0.
    If n is less than 1, return -1.

    Use a while loop.

    Examples:
        collatz_steps(1)  -> 0
        collatz_steps(2)  -> 1
        collatz_steps(6)  -> 8
        collatz_steps(27) -> 111
        collatz_steps(0)  -> -1
    """
    pass
