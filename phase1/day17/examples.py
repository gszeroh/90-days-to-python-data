"""
Day 17: Iterators & Generators (Examples)
Topics: Iterator protocol, generators, generator expressions, itertools
"""

import sys
import itertools


# === Custom Iterator Class ===

class Countdown:
    """Iterator that counts down from a starting number to 1."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("=== Custom Iterator: Countdown ===")
for n in Countdown(5):
    print(n, end=" ")
print()

# Iterators are one-shot
counter = Countdown(3)
print(f"First pass:  {list(counter)}")
print(f"Second pass: {list(counter)}")  # empty — exhausted


# === Iterable vs Iterator ===

class RepeatWord:
    """An iterable (not an iterator) — can be looped multiple times."""

    def __init__(self, word, times):
        self.word = word
        self.times = times

    def __iter__(self):
        # Return a fresh iterator each time
        for _ in range(self.times):
            yield self.word


print("\n=== Iterable vs Iterator ===")
repeater = RepeatWord("hello", 3)
print(f"First loop:  {list(repeater)}")
print(f"Second loop: {list(repeater)}")  # works again


# === Generator Functions ===

def fibonacci():
    """Infinite Fibonacci generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n, iterable):
    """Take the first n elements from an iterable."""
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item


print("\n=== Generator Functions ===")
fib = fibonacci()
print(f"First 10 Fibonacci: {list(take(10, fib))}")


def powers_of_two(max_exp):
    """Finite generator: yields 2^0, 2^1, ..., 2^max_exp."""
    for exp in range(max_exp + 1):
        yield 2 ** exp


print(f"Powers of 2: {list(powers_of_two(8))}")


# === Generator with State ===

def running_average():
    """Generator that yields the running average of sent values."""
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        if value is not None:
            total += value
            count += 1


print("\n=== Generator with State (send) ===")
avg = running_average()
next(avg)  # prime the generator
for v in [10, 20, 30, 40]:
    result = avg.send(v)
    print(f"  Sent {v}, running average: {result}")


# === Generator Expressions ===

print("\n=== Generator Expressions ===")
squares_list = [x ** 2 for x in range(10)]
squares_gen = (x ** 2 for x in range(10))
print(f"List:      {squares_list}")
print(f"Generator: {squares_gen}")
print(f"From gen:  {list(squares_gen)}")

# Useful in function calls — no extra parentheses needed
total = sum(x ** 2 for x in range(10))
print(f"Sum of squares: {total}")
has_even = any(x % 2 == 0 for x in [1, 3, 4, 7])
print(f"Has even: {has_even}")


# === yield from ===

def flatten(nested):
    """Recursively flatten nested lists."""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


print("\n=== yield from ===")
nested = [1, [2, [3, 4], 5], [6, 7], 8]
print(f"Flattened: {list(flatten(nested))}")


# === Memory Efficiency ===

print("\n=== Memory Efficiency ===")
big_list = [x for x in range(1_000_000)]
big_gen = (x for x in range(1_000_000))
print(f"List of 1M ints:  {sys.getsizeof(big_list):>10,} bytes")
print(f"Generator:        {sys.getsizeof(big_gen):>10,} bytes")
print(f"Ratio: ~{sys.getsizeof(big_list) / sys.getsizeof(big_gen):.0f}x more memory for list")


# === itertools: Infinite Iterators ===

print("\n=== itertools: Infinite Iterators ===")
# count: start, start+step, start+2*step, ...
print(f"count(10):    {list(itertools.islice(itertools.count(10), 5))}")
# cycle: repeat a sequence endlessly
print(f"cycle('ABC'): {list(itertools.islice(itertools.cycle('ABC'), 7))}")
# repeat: repeat a value
print(f"repeat(42, 4): {list(itertools.repeat(42, 4))}")


# === itertools: Finite Iterators ===

print("\n=== itertools: Finite Iterators ===")
# chain: concatenate iterables
print(f"chain: {list(itertools.chain([1, 2], [3, 4], [5]))}")
# islice: slice an iterator
print(f"islice(range(100), 5, 10): {list(itertools.islice(range(100), 5, 10))}")
# accumulate: running totals
print(f"accumulate: {list(itertools.accumulate([1, 2, 3, 4, 5]))}")
# takewhile / dropwhile
nums = [2, 4, 6, 7, 8, 10]
print(f"takewhile even: {list(itertools.takewhile(lambda x: x % 2 == 0, nums))}")
print(f"dropwhile even: {list(itertools.dropwhile(lambda x: x % 2 == 0, nums))}")
# compress: filter by selectors
data = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]
print(f"compress: {list(itertools.compress(data, selectors))}")
# zip_longest
print(f"zip_longest: {list(itertools.zip_longest([1, 2, 3], ['a', 'b'], fillvalue='-'))}")


# === itertools: Combinatoric Iterators ===

print("\n=== itertools: Combinatoric Iterators ===")
# product: Cartesian product
print(f"product: {list(itertools.product('AB', [1, 2]))}")
# permutations
print(f"permutations('ABC', 2): {list(itertools.permutations('ABC', 2))}")
# combinations
print(f"combinations('ABCD', 2): {list(itertools.combinations('ABCD', 2))}")
# combinations with replacement
print(f"combinations_w_rep('AB', 3): "
      f"{list(itertools.combinations_with_replacement('AB', 3))}")


# === itertools: groupby ===

print("\n=== itertools: groupby ===")
data = [
    {"name": "Alice", "dept": "Engineering"},
    {"name": "Bob", "dept": "Engineering"},
    {"name": "Carol", "dept": "Marketing"},
    {"name": "Dave", "dept": "Marketing"},
    {"name": "Eve", "dept": "Sales"},
]
# Data must be sorted by key for groupby to work correctly
for dept, members in itertools.groupby(data, key=lambda x: x["dept"]):
    member_list = [m["name"] for m in members]
    print(f"  {dept}: {member_list}")


# === Generator Pipeline ===

print("\n=== Generator Pipeline ===")


def integers():
    """Infinite sequence of positive integers."""
    n = 1
    while True:
        yield n
        n += 1


def squares(nums):
    for n in nums:
        yield n ** 2


def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n


# Compose a lazy pipeline
pipeline = evens(squares(integers()))
first_5 = list(itertools.islice(pipeline, 5))
print(f"First 5 even squares: {first_5}")
