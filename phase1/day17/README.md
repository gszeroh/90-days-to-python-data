# Day 17: Iterators & Generators

## Overview

Iterators and generators are at the heart of Python's approach to handling
sequences of data. They enable **lazy evaluation** — producing values one at a
time instead of computing everything upfront. This is critical for data science,
where datasets can be too large to fit in memory.

---

## 1. The Iterator Protocol

Any object is **iterable** if it implements `__iter__()` (returns an iterator).
An **iterator** is an object that implements:

- `__iter__()` — returns itself.
- `__next__()` — returns the next value, or raises `StopIteration` when exhausted.

```python
class CountUp:
    """Iterator that counts from start up to (not including) stop."""

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for n in CountUp(1, 4):
    print(n)  # 1, 2, 3
```

### How `for` Loops Work Internally

```python
# This:
for x in iterable:
    process(x)

# Is equivalent to:
iterator = iter(iterable)   # calls iterable.__iter__()
while True:
    try:
        x = next(iterator)  # calls iterator.__next__()
        process(x)
    except StopIteration:
        break
```

### Iterable vs Iterator

| Concept    | Has `__iter__` | Has `__next__` | Reusable? |
|------------|----------------|----------------|-----------|
| Iterable   | ✅             | ❌             | ✅ Yes     |
| Iterator   | ✅             | ✅             | ❌ No      |

A **list** is an iterable (you can loop over it many times). A list **iterator**
is a one-pass object — once exhausted, you must create a new one.

---

## 2. Generators

Generators are a concise way to create iterators using functions with `yield`.

```python
def count_up(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1
```

### How Generators Work

1. Calling a generator function returns a **generator object** (does not run the
   body).
2. Each call to `next()` executes the body until the next `yield`, which
   **suspends** execution and returns the yielded value.
3. Execution **resumes** from where it left off on the next `next()` call.
4. When the function returns (or falls off the end), `StopIteration` is raised.

### Generator Expressions

Like list comprehensions, but lazy and wrapped in parentheses:

```python
# List comprehension — creates all values in memory
squares_list = [x ** 2 for x in range(1_000_000)]

# Generator expression — creates values on demand
squares_gen = (x ** 2 for x in range(1_000_000))
```

Generator expressions use virtually no memory regardless of size.

---

## 3. `yield from`

Delegate to a sub-generator:

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

list(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
```

---

## 4. The `itertools` Module

Python's `itertools` provides efficient building blocks for working with
iterators.

### Infinite Iterators

| Function       | Description                  | Example                     |
|----------------|------------------------------|-----------------------------|
| `count(n)`     | n, n+1, n+2, ...            | `count(10)` → 10, 11, 12…  |
| `cycle(p)`     | Repeat sequence forever      | `cycle('AB')` → A, B, A…   |
| `repeat(x, n)` | Repeat x, n times (or ∞)    | `repeat(5, 3)` → 5, 5, 5   |

### Finite Iterators

| Function                  | Description                              |
|---------------------------|------------------------------------------|
| `chain(*iterables)`       | Chain iterables into one sequence        |
| `islice(it, stop)`        | Slice an iterator                        |
| `compress(data, sel)`     | Filter by selector                       |
| `dropwhile(pred, it)`     | Drop while predicate is true             |
| `takewhile(pred, it)`     | Take while predicate is true             |
| `groupby(it, key)`        | Group consecutive items by key           |
| `zip_longest(*its)`       | Zip, filling missing values              |
| `accumulate(it)`          | Running totals                           |

### Combinatoric Iterators

| Function                    | Description                          |
|-----------------------------|--------------------------------------|
| `product(*its)`             | Cartesian product                    |
| `permutations(it, r)`       | r-length permutations               |
| `combinations(it, r)`       | r-length combinations (no repeats)   |
| `combinations_with_replacement(it, r)` | With repeats              |

---

## 5. Memory Efficiency

### Why Lazy Evaluation Matters

```python
import sys

# List: all values in memory at once
big_list = [x for x in range(1_000_000)]
print(sys.getsizeof(big_list))  # ~8 MB

# Generator: virtually zero memory
big_gen = (x for x in range(1_000_000))
print(sys.getsizeof(big_gen))   # ~200 bytes
```

### When to Use Generators

- **Large files**: Process line by line instead of loading entire file.
- **Database results**: Stream rows instead of fetching all at once.
- **Data pipelines**: Chain transformations without intermediate lists.
- **Infinite sequences**: Fibonacci, sensor data, event streams.

### Generator Pipelines

```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    for line in lines:
        if not line.startswith('#'):
            yield line

def to_upper(lines):
    for line in lines:
        yield line.upper()

# Compose a pipeline — no intermediate lists!
pipeline = to_upper(filter_comments(read_lines("data.txt")))
for line in pipeline:
    print(line)
```

---

## Key Takeaways

1. The iterator protocol (`__iter__` + `__next__`) is the foundation of Python's
   `for` loop.
2. Generators (`yield`) create iterators with minimal code.
3. Generator expressions are lazy comprehensions wrapped in `()`.
4. `itertools` provides powerful, memory-efficient iterator building blocks.
5. Lazy evaluation lets you work with datasets larger than available memory.

---

## Further Reading

- [Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)
- [Generators](https://docs.python.org/3/howto/functional.html#generators)
- [itertools documentation](https://docs.python.org/3/library/itertools.html)
- [itertools recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes)
