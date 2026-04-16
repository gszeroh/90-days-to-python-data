"""
Day 06: Control Flow — Loops — Solutions
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
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


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
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


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
    lines = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * i
        lines.append(spaces + stars)
    return "\n".join(lines)


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
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None


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
    if n < 1:
        return -1

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
