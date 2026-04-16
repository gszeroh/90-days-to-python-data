# Day 12: Error Handling

## Overview
Errors are inevitable — files go missing, networks drop, users type garbage.
Python's **exception handling** system lets you anticipate problems, recover
gracefully, and communicate failures clearly. Mastering `try`/`except`,
custom exceptions, and the `logging` module is essential for writing
production-quality code.

---

## 1. The Exception Hierarchy

All exceptions inherit from `BaseException`. The ones you'll catch most often
descend from `Exception`:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── FileNotFoundError
    ├── OSError / IOError
    ├── AttributeError
    └── ...
```

> ⚠️ Never catch `BaseException` unless you have a very specific reason — it
> would swallow `KeyboardInterrupt` and `SystemExit`.

---

## 2. Basic `try` / `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Catch specific exceptions** — avoid bare `except:` which catches everything
including `KeyboardInterrupt`.

---

## 3. Multiple `except` Clauses

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except (TypeError, OverflowError) as e:
    print(f"Unexpected error: {e}")
```

---

## 4. `else` and `finally`

```python
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    # Runs only if NO exception occurred
    content = f.read()
    f.close()
    print("File read successfully.")
finally:
    # ALWAYS runs — cleanup goes here
    print("Operation complete.")
```

| Block | When it runs |
|-------|-------------|
| `try` | Always attempted |
| `except` | Only if a matching exception occurs |
| `else` | Only if no exception occurred |
| `finally` | Always — even if an exception propagates |

---

## 5. Accessing Exception Details

```python
try:
    int("abc")
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"Args: {e.args}")
```

---

## 6. Raising Exceptions

```python
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: {balance} < {amount}")
    return balance - amount
```

**Re-raising** the current exception:

```python
try:
    risky_operation()
except Exception:
    print("Logging the error...")
    raise               # Re-raise the original exception
```

---

## 7. Custom Exceptions

```python
class AppError(Exception):
    """Base exception for this application."""
    pass

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    """Raised when a resource is not found."""
    pass

# Usage
try:
    raise ValidationError("email", "Invalid format")
except ValidationError as e:
    print(f"Validation failed — {e.field}: {e.message}")
```

> 💡 Create a base exception for your application and derive specific
> exceptions from it. This lets callers catch all your app errors at once or
> handle specific ones.

---

## 8. EAFP vs LBYL

| Style | Philosophy |
|-------|-----------|
| **EAFP** | *Easier to Ask Forgiveness than Permission* — try it, handle errors |
| **LBYL** | *Look Before You Leap* — check conditions before acting |

```python
# LBYL
if "key" in my_dict:
    value = my_dict["key"]
else:
    value = "default"

# EAFP (Pythonic)
try:
    value = my_dict["key"]
except KeyError:
    value = "default"
```

Python favours EAFP. Use it when:
- Checks would be expensive or racy (e.g., file existence before opening).
- The common case is success (exceptions are rare).

---

## 9. Assertions

Assertions check invariants during development. They are stripped out when
Python runs with the `-O` flag, so **never use them for input validation**.

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List must not be empty"
    return sum(numbers) / len(numbers)
```

---

## 10. The `logging` Module

`logging` is far superior to `print()` for diagnostics.

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logging.debug("Detailed diagnostic info")
logging.info("General operational info")
logging.warning("Something unexpected")
logging.error("An error occurred")
logging.critical("System is going down!")
```

**Log levels** (lowest → highest): `DEBUG`, `INFO`, `WARNING`, `ERROR`,
`CRITICAL`.

Logging exceptions with tracebacks:

```python
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division failed")   # Includes traceback
```

---

## Key Takeaways
- Catch **specific** exceptions — never use bare `except:`.
- Use `else` for code that should run only on success; `finally` for cleanup.
- Raise exceptions early when inputs are invalid.
- Build a custom exception hierarchy for non-trivial applications.
- Prefer EAFP over LBYL — it's the Pythonic style.
- Use `logging` instead of `print()` for operational diagnostics.
- Never rely on `assert` for runtime validation — it can be disabled.

---

## Further Reading
- [Python Docs — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Docs — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Docs — logging](https://docs.python.org/3/library/logging.html)
- [Real Python — Exception Handling](https://realpython.com/python-exceptions/)
- [Real Python — Logging](https://realpython.com/python-logging/)
