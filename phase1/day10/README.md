# Day 10: Dictionaries & Sets

## Overview
Dictionaries and sets are Python's **hash-based** collections. Dicts store
key-value pairs with O(1) average lookup time. Sets store unique elements and
support powerful mathematical set operations. Together they solve a vast range
of data processing problems efficiently.

---

## 1. Creating Dictionaries

```python
# Literal syntax
person = {"name": "Alice", "age": 30, "city": "NYC"}

# dict() constructor
config = dict(debug=True, verbose=False, timeout=30)

# From a list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)

# Empty dict
empty = {}
```

---

## 2. Accessing and Modifying Values

```python
person = {"name": "Alice", "age": 30}

# Access
person["name"]             # "Alice"
person.get("age")          # 30
person.get("email", "N/A") # "N/A" — default if key missing

# Modify / Add
person["age"] = 31
person["email"] = "alice@example.com"

# Delete
del person["email"]
removed = person.pop("age")        # removed=31
removed = person.pop("missing", 0) # 0 — no KeyError
```

> ⚠️ `dict["key"]` raises `KeyError` if the key doesn't exist. Prefer `.get()`
> when the key might be absent.

---

## 3. Dictionary Methods

| Method | Description |
|--------|-------------|
| `get(key, default)` | Return value or default (no KeyError) |
| `keys()` | View of all keys |
| `values()` | View of all values |
| `items()` | View of (key, value) pairs |
| `update(other)` | Merge another dict (overwrites existing keys) |
| `pop(key, default)` | Remove and return value |
| `setdefault(key, default)` | Get value; if missing, set it to default |
| `clear()` | Remove all items |
| `copy()` | Shallow copy |

```python
d = {"a": 1, "b": 2, "c": 3}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(f"{key}: {value}")

d.update({"b": 20, "d": 4})  # {"a": 1, "b": 20, "c": 3, "d": 4}
```

---

## 4. Dictionary Comprehensions

```python
# Basic: {key_expr: value_expr for item in iterable}
squares = {x: x ** 2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Inverting a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

---

## 5. Merge Operators (Python 3.9+)

```python
defaults = {"color": "blue", "size": "medium"}
custom = {"size": "large", "weight": "heavy"}

# | creates a new merged dict (right side wins on conflicts)
merged = defaults | custom
# {"color": "blue", "size": "large", "weight": "heavy"}

# |= updates in place
defaults |= custom
```

---

## 6. `defaultdict`

A dict subclass that provides a default value for missing keys.

```python
from collections import defaultdict

# Group items by category
word_lengths = defaultdict(list)
for word in ["hello", "hi", "hey", "howdy", "hola"]:
    word_lengths[len(word)].append(word)

# {5: ["hello", "howdy"], 2: ["hi"], 3: ["hey"], 4: ["hola"]}

# Count items
counter = defaultdict(int)
for char in "mississippi":
    counter[char] += 1
# {"m": 1, "i": 4, "s": 4, "p": 2}
```

---

## 7. `Counter`

Specialized dict for counting hashable objects.

```python
from collections import Counter

# Count elements
c = Counter("mississippi")
# Counter({"s": 4, "i": 4, "p": 2, "m": 1})

c.most_common(2)    # [("s", 4), ("i", 4)]

# Count from a list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words)
# Counter({"apple": 3, "banana": 2, "cherry": 1})

# Arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2    # Counter({"a": 4, "b": 3})
c1 - c2    # Counter({"a": 2})
```

---

## 8. Creating Sets

Sets are **unordered** collections of **unique** elements.

```python
# Literal syntax
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From an iterable (removes duplicates)
unique = set([1, 2, 2, 3, 3, 3])   # {1, 2, 3}

# Empty set (NOT {} — that's a dict)
empty = set()
```

---

## 9. Set Operations

| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `a \| b` | `a.union(b)` |
| Intersection | `a & b` | `a.intersection(b)` |
| Difference | `a - b` | `a.difference(b)` |
| Symmetric Difference | `a ^ b` | `a.symmetric_difference(b)` |
| Subset | `a <= b` | `a.issubset(b)` |
| Superset | `a >= b` | `a.issuperset(b)` |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # {1, 2, 3, 4, 5, 6}   — union
a & b    # {3, 4}                — intersection
a - b    # {1, 2}                — in a but not b
b - a    # {5, 6}                — in b but not a
a ^ b    # {1, 2, 5, 6}         — in one but not both
```

---

## 10. Set Methods

```python
s = {1, 2, 3}

s.add(4)           # {1, 2, 3, 4}
s.discard(2)       # {1, 3, 4}    — no error if missing
s.remove(3)        # {1, 4}       — KeyError if missing
popped = s.pop()   # removes arbitrary element
s.clear()          # set()
```

---

## 11. `frozenset`

An **immutable** set. Can be used as a dict key or as an element of another set.

```python
fs = frozenset([1, 2, 3])

# Can be a dict key
cache = {fs: "result"}

# Can be a set element
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
```

---

## 12. Performance Characteristics

| Operation | dict | list |
|-----------|------|------|
| Lookup (`in`) | O(1) avg | O(n) |
| Insert | O(1) avg | O(1) append, O(n) insert |
| Delete | O(1) avg | O(n) |

Sets have the same O(1) average for `in`, `add`, and `discard`.

> 💡 **Tip:** When you need to check membership in a large collection, convert
> it to a set first for dramatic speedups.

---

## Key Takeaways
- Dicts map keys to values with O(1) lookups — use `.get()` to avoid KeyError.
- Dict comprehensions are concise for building dicts from iterables.
- `defaultdict` auto-initializes missing keys — great for grouping and counting.
- `Counter` is purpose-built for frequency counting.
- Sets store unique elements and support mathematical operations.
- `frozenset` is the immutable variant — usable as dict keys and set elements.
- Hash-based collections (dict, set) are far faster than lists for lookups.

---

## Further Reading
- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Docs — collections](https://docs.python.org/3/library/collections.html)
- [Real Python — Dictionaries](https://realpython.com/python-dicts/)
- [Real Python — Sets](https://realpython.com/python-sets/)
