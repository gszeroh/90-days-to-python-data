"""
Day 09: Lists & Tuples — Examples
"""

# === Creating Lists ===

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []

print(f"fruits: {fruits}")
print(f"numbers: {numbers}")
print(f"mixed types: {mixed}")

# From other iterables
from_range = list(range(1, 6))
from_string = list("hello")
print(f"from range: {from_range}")
print(f"from string: {from_string}")

# === Indexing ===

colors = ["red", "green", "blue", "yellow", "purple"]

print(f"\ncolors = {colors}")
print(f"colors[0]  = {colors[0]}")      # First
print(f"colors[-1] = {colors[-1]}")      # Last
print(f"colors[2]  = {colors[2]}")       # Third

# === Slicing ===

print(f"\ncolors[1:4]  = {colors[1:4]}")    # Index 1 to 3
print(f"colors[:3]   = {colors[:3]}")        # First 3
print(f"colors[2:]   = {colors[2:]}")        # From index 2 onward
print(f"colors[::2]  = {colors[::2]}")       # Every 2nd
print(f"colors[::-1] = {colors[::-1]}")      # Reversed

# Slice assignment (lists are mutable)
nums = [0, 1, 2, 3, 4, 5]
nums[1:4] = [10, 20, 30]
print(f"After slice assignment: {nums}")

# === List Methods ===

print("\n--- List Methods ---")

items = [3, 1, 4, 1, 5]
print(f"Original: {items}")

items.append(9)
print(f"append(9): {items}")

items.extend([2, 6])
print(f"extend([2, 6]): {items}")

items.insert(0, 0)
print(f"insert(0, 0): {items}")

items.remove(1)
print(f"remove(1): {items}")

popped = items.pop()
print(f"pop(): removed {popped}, list = {items}")

popped_at = items.pop(2)
print(f"pop(2): removed {popped_at}, list = {items}")

print(f"count(1): {items.count(1)}")
print(f"index(5): {items.index(5)}")

# Sort and reverse
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(f"\nsort(): {nums}")

nums.reverse()
print(f"reverse(): {nums}")

# sorted() — non-mutating
original = [5, 2, 8, 1, 9]
sorted_copy = sorted(original)
print(f"\noriginal: {original}")
print(f"sorted():  {sorted_copy}")

# Sort with key
words = ["banana", "apple", "cherry", "date"]
by_length = sorted(words, key=len)
print(f"sorted by length: {by_length}")

# === List Comprehensions ===

print("\n--- List Comprehensions ---")

squares = [x ** 2 for x in range(10)]
print(f"Squares 0-9: {squares}")

evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens 0-19: {evens}")

# Transform + filter
words = ["hello", "Hi", "PYTHON", "world", "ok"]
long_lower = [w.lower() for w in words if len(w) > 2]
print(f"Long words lowered: {long_lower}")

# Nested comprehension — flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flattened matrix: {flat}")

# Comprehension with conditional expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(f"Even/odd labels: {labels}")

# 2D comprehension — create a matrix
grid = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 grid:")
for row in grid:
    print(f"  {row}")

# === Creating Tuples ===

print("\n--- Tuples ---")

point = (3, 4)
rgb = (255, 128, 0)
single = (42,)
empty_tuple = ()

print(f"point: {point}")
print(f"rgb: {rgb}")
print(f"single element tuple: {single}")
print(f"type of (42,): {type(single)}")
print(f"type of (42):  {type((42))}")  # int, not tuple!

# Tuple from iterable
from_list = tuple([1, 2, 3])
from_range = tuple(range(5))
print(f"from list: {from_list}")
print(f"from range: {from_range}")

# Tuples are immutable
# point[0] = 10  # TypeError: 'tuple' does not support item assignment

# Tuple methods
nums_tuple = (1, 2, 3, 2, 1, 2)
print(f"\ncount(2): {nums_tuple.count(2)}")
print(f"index(3): {nums_tuple.index(3)}")

# === Tuple Unpacking ===

print("\n--- Tuple Unpacking ---")

x, y = (3, 4)
print(f"x={x}, y={y}")

# Swap
a, b = 1, 2
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# Unpacking in loops
students = [("Alice", 92), ("Bob", 85), ("Charlie", 78)]
for name, score in students:
    print(f"  {name}: {score}")

# Nested unpacking
data = [(1, (2, 3)), (4, (5, 6))]
for a, (b, c) in data:
    print(f"  a={a}, b={b}, c={c}")

# === Named Tuples ===

print("\n--- Named Tuples ---")

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(f"Point: {p}")
print(f"p.x = {p.x}, p.y = {p.y}")
print(f"p[0] = {p[0]}, p[1] = {p[1]}")

# Named tuple methods
print(f"_asdict(): {p._asdict()}")
p2 = p._replace(x=10)
print(f"_replace(x=10): {p2}")

# With defaults
Color = namedtuple("Color", ["r", "g", "b"], defaults=[0, 0, 0])
black = Color()
red = Color(255)
white = Color(255, 255, 255)
print(f"\nblack: {black}")
print(f"red:   {red}")
print(f"white: {white}")

# Named tuple for structured data
Student = namedtuple("Student", ["name", "age", "gpa"])
students = [
    Student("Alice", 20, 3.8),
    Student("Bob", 22, 3.5),
    Student("Charlie", 21, 3.9),
]

# Sort by GPA descending
for s in sorted(students, key=lambda s: s.gpa, reverse=True):
    print(f"  {s.name}: GPA {s.gpa}")

# === Useful Built-in Functions with Sequences ===

print("\n--- Built-in Functions ---")

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"nums = {nums}")
print(f"len:    {len(nums)}")
print(f"min:    {min(nums)}")
print(f"max:    {max(nums)}")
print(f"sum:    {sum(nums)}")
print(f"any:    {any([0, 0, 1])}")
print(f"all:    {all([1, 1, 1])}")

# Membership testing
print(f"\n5 in nums: {5 in nums}")
print(f"7 in nums: {7 in nums}")

# Concatenation and repetition
a = [1, 2, 3]
b = [4, 5, 6]
print(f"\n{a} + {b} = {a + b}")
print(f"{a} * 3 = {a * 3}")
