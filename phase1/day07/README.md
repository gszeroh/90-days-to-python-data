# Day 07: Functions — Basics

## Overview
Functions are reusable blocks of code that perform a specific task. They help you
organize code, avoid repetition, and make programs easier to read, test, and maintain.

---

## 1. Defining a Function

Use the `def` keyword, followed by the function name, parentheses, and a colon.

```python
def greet():
    print("Hello, World!")

greet()  # Call the function
```

### Naming Conventions
- Use **snake_case** for function names: `calculate_total`, `get_user_name`.
- Choose descriptive names that indicate what the function does.
- Avoid single-letter names except for trivial cases (`f`, `x` in math contexts).

---

## 2. Parameters and Arguments

**Parameters** are variables listed in the function definition.
**Arguments** are the values passed when calling the function.

```python
def greet(name):         # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")           # "Alice" is an argument
```

### Multiple Parameters
```python
def add(a, b):
    return a + b

result = add(3, 5)      # 8
```

---

## 3. Return Values

Use `return` to send a value back to the caller. Without `return`, a function
returns `None` by default.

```python
def square(n):
    return n ** 2

result = square(4)       # 16
```

### Returning Multiple Values
Python allows returning multiple values as a tuple.

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)    # q=3, r=2
```

### Early Return
```python
def absolute_value(n):
    if n < 0:
        return -n
    return n
```

---

## 4. Default Arguments

Provide default values for parameters. Arguments with defaults are optional
when calling the function.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                # Hello, Alice!
greet("Bob", "Good morning")  # Good morning, Bob!
```

> ⚠️ **Important:** Default arguments are evaluated **once** when the function
> is defined. Never use a mutable object (like a list or dict) as a default.

```python
# BAD — shared mutable default
def add_item(item, items=[]):
    items.append(item)
    return items

# GOOD — use None sentinel
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 5. Keyword Arguments

Pass arguments by name for clarity and to skip optional parameters.

```python
def create_profile(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

# Positional arguments
create_profile("Alice", 30, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(age=30, name="Alice", city="NYC")

# Mixing positional and keyword (positional must come first)
create_profile("Alice", city="NYC", age=30)
```

---

## 6. Scope — Local vs. Global

Variables defined inside a function are **local** and cannot be accessed outside.
Variables defined at the module level are **global**.

```python
x = 10          # global

def my_function():
    y = 5       # local
    print(x)    # can read global
    print(y)    # can read local

my_function()
# print(y)     # NameError — y is not defined here
```

### The `global` Keyword
To **modify** a global variable inside a function, use the `global` keyword.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

> ⚠️ **Best Practice:** Avoid `global`. Instead, pass values as arguments and
> return results. Global state makes code harder to reason about and test.

### The LEGB Rule
Python resolves names in this order:
1. **L**ocal — inside the current function
2. **E**nclosing — in any enclosing (outer) function
3. **G**lobal — at the module level
4. **B**uilt-in — Python's built-in names (`len`, `print`, etc.)

---

## 7. Docstrings

Document your functions with a docstring — a string literal on the first line
of the function body.

```python
def factorial(n):
    """Return the factorial of a non-negative integer n.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n (n!).

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Accessing Docstrings
```python
print(factorial.__doc__)
help(factorial)
```

---

## 8. Type Hints

Type hints make code more readable and enable IDE support. They are **not enforced**
at runtime.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, times: int = 1) -> None:
    for _ in range(times):
        print(f"Hello, {name}!")
```

---

## 9. Common Patterns

### Boolean Functions (Predicates)
```python
def is_even(n):
    return n % 2 == 0

def is_valid_age(age):
    return 0 <= age <= 150
```

### Converter Functions
```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
```

### Accumulator Functions
```python
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
```

---

## Key Takeaways
- Use `def` to define functions. Keep them small and focused.
- Parameters make functions flexible; return values make them composable.
- Default arguments simplify common use cases — but never use mutable defaults.
- Keyword arguments improve readability at call sites.
- Understand scope (LEGB rule) — prefer passing values over using `global`.
- Always write docstrings for public functions.
- Type hints improve readability and tooling support.

---

## Further Reading
- [Python Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 — Type Hints](https://peps.python.org/pep-0484/)
- [Real Python — Defining Your Own Functions](https://realpython.com/defining-your-own-python-function/)
