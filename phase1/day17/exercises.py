"""
Day 17: Iterators & Generators (Exercises)
Complete each exercise by replacing `pass` with your implementation.
"""


# === Exercise 1: Fibonacci Generator ===
# Write a generator function that yields Fibonacci numbers.
# If max_count is provided, yield at most that many numbers.
# If max_count is None, yield indefinitely.
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(max_count=None):
    pass


# === Exercise 2: Custom Range Iterator ===
# Create an iterator class called FloatRange that works like range()
# but supports float step values.
# FloatRange(start, stop, step) should yield values from start up to
# (but not including) stop, incrementing by step.
# Support: iteration, len(), and repr().
# Example: list(FloatRange(0, 1, 0.2)) -> [0, 0.2, 0.4, 0.6, 0.8]

class FloatRange:
    def __init__(self, start, stop, step=1.0):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __len__(self):
        pass

    def __repr__(self):
        pass


# === Exercise 3: Chunk Generator ===
# Write a generator that splits an iterable into chunks of size n.
# The last chunk may have fewer than n elements.
# Example: list(chunked([1,2,3,4,5], 2)) -> [[1,2], [3,4], [5]]
# Important: Must work with any iterable (not just sequences).

def chunked(iterable, n):
    pass


# === Exercise 4: itertools Combinations ===
# Given a list of numbers and a target sum, write a function that finds
# all unique combinations of `size` numbers that add up to the target.
# Use itertools.combinations.
# Example: find_combinations([1,2,3,4,5], target=6, size=2) -> [(1,5), (2,4)]

def find_combinations(numbers, target, size=2):
    pass


# === Exercise 5: Infinite Counter with Transformations ===
# Create a generator class (using __iter__ and __next__) that:
# - Starts counting from a given start value
# - Increments by a given step
# - Has a method apply_filter(predicate) that returns a new generator
#   yielding only values matching the predicate
# - Has a method apply_map(func) that returns a new generator
#   yielding transformed values
# Example usage:
#   counter = InfiniteCounter(1, 2)  # 1, 3, 5, 7, 9, ...
#   evens = counter.apply_filter(lambda x: x % 2 == 0)  # (none from odds)
#   doubled = counter.apply_map(lambda x: x * 2)  # 2, 6, 10, 14, ...

class InfiniteCounter:
    def __init__(self, start=0, step=1):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def apply_filter(self, predicate):
        pass

    def apply_map(self, func):
        pass
