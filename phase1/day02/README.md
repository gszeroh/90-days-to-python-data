# Day 02: Variables & Data Types

## Overview
Variables are the fundamental way to store and manipulate data in Python. Today we
explore Python's core data types, how to create variables, and how to convert between
types.

---

## 1. Variables

A variable is a name that refers to a value stored in memory.

```python
age = 25
name = "Alice"
pi = 3.14159
```

### Assignment
- Python uses `=` for assignment (not equality).
- Variables are created the moment you first assign a value.
- No need to declare a type — Python infers it automatically (**dynamic typing**).

### Multiple Assignment
```python
x, y, z = 1, 2, 3
a = b = c = 0          # All three point to the same value
```

### Swapping Variables
```python
x, y = y, x            # Pythonic swap — no temp variable needed
```

---

## 2. Variable Naming Rules & Conventions

### Rules (enforced by Python)
- Must start with a letter or underscore (`_`).
- Can contain letters, digits, and underscores.
- Case-sensitive (`age`, `Age`, and `AGE` are different variables).
- Cannot be a Python keyword (`if`, `for`, `class`, etc.).

### Conventions (PEP 8)
| Style | Usage | Example |
|-------|-------|---------|
| `snake_case` | Variables, functions | `user_name`, `total_count` |
| `UPPER_SNAKE_CASE` | Constants | `MAX_SIZE`, `PI` |
| `PascalCase` | Classes | `DataLoader`, `UserProfile` |
| `_leading_underscore` | Internal / private | `_helper`, `_cache` |

---

## 3. Core Data Types

### `int` — Integer
Whole numbers with no decimal point. Python integers have **arbitrary precision**
(no overflow).

```python
count = 42
big_number = 1_000_000   # Underscores improve readability
negative = -17
```

### `float` — Floating Point
Numbers with a decimal point. Stored as IEEE 754 double precision.

```python
price = 19.99
scientific = 2.5e10       # 25000000000.0
tiny = 1.2e-4             # 0.00012
```

> ⚠️ **Floating-point gotcha:** `0.1 + 0.2` is `0.30000000000000004`, not `0.3`.

### `str` — String
A sequence of characters enclosed in single or double quotes.

```python
greeting = "Hello"
letter = 'A'
multiline = """This spans
multiple lines"""
```

### `bool` — Boolean
Represents truth values: `True` or `False`.

```python
is_active = True
has_access = False
```

Booleans are a subclass of `int`: `True == 1`, `False == 0`.

### `None` — The Absence of Value
`None` represents "nothing" or "no value". It is **not** the same as `0`, `""`, or
`False`.

```python
result = None
```

---

## 4. The `type()` Function

Use `type()` to inspect the type of any value or variable.

```python
type(42)          # <class 'int'>
type(3.14)        # <class 'float'>
type("hello")     # <class 'str'>
type(True)        # <class 'bool'>
type(None)        # <class 'NoneType'>
```

---

## 5. Type Conversion (Casting)

Convert between types using constructor functions:

| Function | Converts To | Example |
|----------|-------------|---------|
| `int()`  | Integer     | `int("42")` → `42` |
| `float()` | Float     | `float("3.14")` → `3.14` |
| `str()`  | String      | `str(42)` → `"42"` |
| `bool()` | Boolean     | `bool(0)` → `False` |

### Implicit vs. Explicit Conversion
```python
# Implicit — Python converts automatically
result = 5 + 2.0     # int + float → float (7.0)

# Explicit — You convert manually
age_str = "25"
age_int = int(age_str)   # "25" → 25
```

### Truthy and Falsy Conversions
```python
bool(0)       # False
bool(42)      # True
bool("")      # False
bool("hello") # True
bool(None)    # False
bool([])      # False (empty list)
bool([1])     # True  (non-empty list)
```

---

## 6. Constants

Python has no true constant keyword. By convention, use `UPPER_SNAKE_CASE` to
signal that a value should not be changed.

```python
PI = 3.14159
MAX_RETRIES = 5
BASE_URL = "https://api.example.com"
```

---

## Key Takeaways
- Variables are created on assignment — no declaration needed.
- Python's core scalar types: `int`, `float`, `str`, `bool`, `None`.
- Use `type()` to inspect types and casting functions to convert.
- Follow PEP 8 naming conventions: `snake_case` for variables, `UPPER_CASE` for constants.
- Be aware of floating-point precision limitations.

---

## Further Reading
- [Python Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [Real Python — Variables](https://realpython.com/python-variables/)
