# Day 09: Lists & Tuples

## Overview
Lists and tuples are Python's core **sequence** types. Lists are mutable
(changeable); tuples are immutable (fixed after creation). Both support indexing,
slicing, and iteration, making them essential for data manipulation.

---

## 1. Creating Lists

```python
# Literal syntax
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []

# From other iterables
from_range = list(range(5))           # [0, 1, 2, 3, 4]
from_string = list("hello")           # ['h', 'e', 'l', 'l', 'o']
from_tuple = list((10, 20, 30))       # [10, 20, 30]
```

---

## 2. Indexing and Slicing

### Indexing
```python
colors = ["red", "green", "blue", "yellow", "purple"]

colors[0]     # "red"       — first element
colors[-1]    # "purple"    — last element
colors[2]     # "blue"      — third element
```

### Slicing — `list[start:stop:step]`
```python
colors[1:4]    # ["green", "blue", "yellow"]   — index 1 to 3
colors[:3]     # ["red", "green", "blue"]       — first 3
colors[2:]     # ["blue", "yellow", "purple"]   — from index 2 onward
colors[::2]    # ["red", "blue", "purple"]      — every 2nd element
colors[::-1]   # ["purple", "yellow", "blue", "green", "red"] — reversed
```

Slicing creates a **shallow copy** of the list.

---

## 3. List Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `append(x)` | Add `x` to the end | `None` |
| `extend(iterable)` | Add all items from iterable | `None` |
| `insert(i, x)` | Insert `x` at position `i` | `None` |
| `remove(x)` | Remove first occurrence of `x` | `None` |
| `pop(i)` | Remove and return item at `i` (default: last) | removed item |
| `index(x)` | Return index of first `x` | `int` |
| `count(x)` | Count occurrences of `x` | `int` |
| `sort()` | Sort in place | `None` |
| `reverse()` | Reverse in place | `None` |
| `copy()` | Return a shallow copy | `list` |
| `clear()` | Remove all items | `None` |

```python
nums = [3, 1, 4, 1, 5]

nums.append(9)        # [3, 1, 4, 1, 5, 9]
nums.extend([2, 6])   # [3, 1, 4, 1, 5, 9, 2, 6]
nums.insert(0, 0)     # [0, 3, 1, 4, 1, 5, 9, 2, 6]
nums.remove(1)        # [0, 3, 4, 1, 5, 9, 2, 6]  — first 1 removed
last = nums.pop()     # last=6, nums=[0, 3, 4, 1, 5, 9, 2]
nums.sort()           # [0, 1, 2, 3, 4, 5, 9]
nums.reverse()        # [9, 5, 4, 3, 2, 1, 0]
```

> ⚠️ **Note:** `sort()` and `reverse()` modify the list **in place** and return
> `None`. Use `sorted()` and `reversed()` for non-mutating alternatives.

---

## 4. List Comprehensions

A concise way to create lists from existing iterables.

```python
# Basic: [expression for item in iterable]
squares = [x ** 2 for x in range(10)]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]

# With transformation and condition
upper_long = [w.upper() for w in words if len(w) > 3]

# Nested comprehension (flatten)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6]
```

### When to Use Comprehensions
- ✅ Simple transformations and filters.
- ❌ Complex logic with side effects — use a regular `for` loop instead.

---

## 5. Creating Tuples

Tuples are **immutable** sequences — once created, they cannot be changed.

```python
# Literal syntax
point = (3, 4)
rgb = (255, 128, 0)
single = (42,)          # Note the comma — (42) is just an int!
empty = ()

# From other iterables
from_list = tuple([1, 2, 3])
from_range = tuple(range(5))
```

---

## 6. Tuple Unpacking

Assign tuple elements to variables in a single statement.

```python
# Basic unpacking
x, y = (3, 4)

# Swap values
a, b = 1, 2
a, b = b, a              # a=2, b=1

# Extended unpacking with *
first, *rest = [1, 2, 3, 4, 5]
# first=1, rest=[2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2, 3, 4], last=5

# In loops
pairs = [(1, "a"), (2, "b"), (3, "c")]
for number, letter in pairs:
    print(f"{number}: {letter}")
```

---

## 7. Named Tuples

Give meaningful names to tuple fields for self-documenting code.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(p.x)      # 3
print(p.y)      # 4
print(p[0])     # 3  — still supports indexing
print(p)         # Point(x=3, y=4)

# With defaults (Python 3.6.1+)
Color = namedtuple("Color", ["r", "g", "b"], defaults=[0, 0, 0])
black = Color()          # Color(r=0, g=0, b=0)
red = Color(255)         # Color(r=255, g=0, b=0)
```

### `typing.NamedTuple` (Modern Alternative)
```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(3.0, 4.0)
```

---

## 8. Lists vs. Tuples

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Hashable | ❌ No | ✅ Yes (if contents are hashable) |
| Use as dict key | ❌ No | ✅ Yes |
| Performance | Slightly slower | Slightly faster |
| Use case | Collections that change | Fixed records, dict keys, return values |

**Rule of thumb:** Use a list for homogeneous collections of varying length.
Use a tuple for heterogeneous fixed-structure records.

---

## 9. Useful Built-in Functions

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

len(nums)         # 8
min(nums)         # 1
max(nums)         # 9
sum(nums)         # 31
sorted(nums)      # [1, 1, 2, 3, 4, 5, 6, 9]  — returns new list
any([0, 0, 1])    # True  — at least one truthy
all([1, 1, 1])    # True  — all truthy
```

---

## Key Takeaways
- Lists are mutable and versatile — use for collections that grow/shrink.
- Tuples are immutable — use for fixed records, dict keys, and multiple return values.
- Slicing creates copies; indexing gives individual elements.
- List comprehensions are concise but keep them simple.
- Named tuples add readability to tuple-based data.
- Prefer `sorted()` over `.sort()` when you need the original list unchanged.

---

## Further Reading
- [Python Docs — Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Docs — Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Docs — namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)
- [Real Python — Lists and Tuples](https://realpython.com/python-lists-tuples/)
