# Day 08: Functions — Advanced

## Overview
Building on the basics, Python offers powerful tools for writing flexible,
composable functions: variadic arguments, anonymous functions, higher-order
functions, closures, and decorators.

---

## 1. `*args` — Variable Positional Arguments

Collect any number of positional arguments into a **tuple**.

```python
def add_all(*args):
    return sum(args)

add_all(1, 2, 3)        # 6
add_all(10, 20, 30, 40) # 100
```

### Combining with Regular Parameters
```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
```

---

## 2. `**kwargs` — Variable Keyword Arguments

Collect any number of keyword arguments into a **dictionary**.

```python
def build_profile(**kwargs):
    return kwargs

profile = build_profile(name="Alice", age=30, city="NYC")
# {"name": "Alice", "age": 30, "city": "NYC"}
```

### Combining `*args` and `**kwargs`
```python
def universal(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

universal(1, 2, 3, x=10, y=20)
# args: (1, 2, 3)
# kwargs: {"x": 10, "y": 20}
```

### Parameter Order
The correct order for parameters is:
1. Regular parameters
2. `*args`
3. Keyword-only parameters
4. `**kwargs`

```python
def example(a, b, *args, option=True, **kwargs):
    pass
```

---

## 3. Unpacking Arguments

Use `*` and `**` to **unpack** iterables and dicts when calling functions.

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
add(*numbers)           # Same as add(1, 2, 3)

params = {"a": 10, "b": 20, "c": 30}
add(**params)           # Same as add(a=10, b=20, c=30)
```

---

## 4. Lambda Functions

Anonymous, single-expression functions defined with the `lambda` keyword.

```python
square = lambda x: x ** 2
square(5)               # 25

add = lambda a, b: a + b
add(3, 4)               # 7
```

### When to Use Lambdas
- As short callbacks to `sorted()`, `map()`, `filter()`.
- When a full `def` would be overkill.
- **Not** for complex logic — use `def` for readability.

```python
pairs = [(1, "b"), (3, "a"), (2, "c")]
sorted(pairs, key=lambda p: p[1])  # Sort by second element
```

---

## 5. Higher-Order Functions: `map()`, `filter()`, `reduce()`

Functions that **take other functions as arguments**.

### `map(func, iterable)` — Transform Each Element
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]
```

### `filter(func, iterable)` — Keep Elements Where func Returns True
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8]
```

### `reduce(func, iterable)` — Accumulate to a Single Value
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
# 120  (1 * 2 * 3 * 4 * 5)
```

### Comparison with Comprehensions
```python
# map + lambda
squared = list(map(lambda x: x ** 2, numbers))

# List comprehension (preferred in most cases)
squared = [x ** 2 for x in numbers]
```

> 💡 **Tip:** List comprehensions are generally more Pythonic and readable than
> `map()`/`filter()` with lambdas.

---

## 6. Closures

A **closure** is a function that remembers values from its enclosing scope even
after that scope has finished executing.

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)   # 10
triple(5)   # 15
```

### Closure with State
```python
def make_counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
counter()  # 1
counter()  # 2
counter()  # 3
```

The `nonlocal` keyword lets an inner function **modify** a variable in the
enclosing scope.

---

## 7. Decorators

A **decorator** is a function that wraps another function to extend or modify its
behavior without changing its source code.

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

add(3, 5)
# Calling add...
# add returned 8
```

### Using `functools.wraps`

Without `functools.wraps`, the decorated function loses its original name and
docstring.

```python
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        return result
    return wrapper
```

### Decorators with Arguments
```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" three times
```

### Common Built-in Decorators
- `@staticmethod` — method that doesn't need `self`
- `@classmethod` — method that receives the class instead of an instance
- `@property` — make a method behave like an attribute
- `@functools.lru_cache` — memoize function results

---

## 8. `functools` Highlights

```python
from functools import lru_cache, partial

# lru_cache — memoization
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# partial — fix some arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(3)    # 27
```

---

## Key Takeaways
- `*args` and `**kwargs` make functions flexible and generic.
- Lambda functions are for short, throwaway functions — not complex logic.
- `map()`, `filter()`, and `reduce()` enable functional-style programming.
- Closures capture enclosing scope — useful for factories and state.
- Decorators modify function behavior without changing the function itself.
- `functools.wraps` preserves the original function's metadata.
- `functools.lru_cache` and `partial` are powerful everyday tools.

---

## Further Reading
- [Python Docs — More on Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Python Docs — functools](https://docs.python.org/3/library/functools.html)
- [Real Python — Primer on Decorators](https://realpython.com/primer-on-python-decorators/)
- [Real Python — Python Closures](https://realpython.com/python-closure/)
