"""
Day 12: Error Handling — Examples
"""

import logging

# === Basic try/except ===

print("--- Basic try/except ---")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError: cannot divide by zero")

try:
    number = int("not_a_number")
except ValueError as e:
    print(f"Caught ValueError: {e}")

# === Multiple except Clauses ===

print("\n--- Multiple except ---")

test_cases = [("10", 2), ("abc", 1), ("0", 0), ([1], 1)]

for value, divisor in test_cases:
    try:
        num = int(value)
        result = 100 / num
        print(f"  int({value!r}) / {divisor} → {result:.1f}")
    except ValueError:
        print(f"  {value!r} → ValueError: not a number")
    except ZeroDivisionError:
        print(f"  {value!r} → ZeroDivisionError: division by zero")
    except (TypeError, OverflowError) as e:
        print(f"  {value!r} → {type(e).__name__}: {e}")

# === else and finally ===

print("\n--- else / finally ---")

def read_file_safe(path):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(f"  File not found: {path}")
    else:
        content = f.read()
        f.close()
        print(f"  Read {len(content)} chars from {path}")
    finally:
        print(f"  Finished attempt for {path}")

read_file_safe("exercises.py")   # Should succeed
read_file_safe("nonexistent.txt")  # Should fail gracefully

# === Accessing Exception Details ===

print("\n--- Exception Details ---")

try:
    int("xyz")
except ValueError as e:
    print(f"Type: {type(e).__name__}")
    print(f"Message: {e}")
    print(f"Args: {e.args}")

# === Raising Exceptions ===

print("\n--- Raising Exceptions ---")

def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance={balance}, amount={amount}")
    return balance - amount

# Successful withdrawal
new_balance = withdraw(100, 30)
print(f"Withdraw 30 from 100: balance = {new_balance}")

# Failed withdrawal
try:
    withdraw(50, 100)
except ValueError as e:
    print(f"Caught: {e}")

try:
    withdraw(50, -10)
except ValueError as e:
    print(f"Caught: {e}")

# === Re-raising Exceptions ===

print("\n--- Re-raising ---")

def process_data(data):
    try:
        return int(data) * 2
    except ValueError:
        print(f"  Logging: bad data {data!r}")
        raise  # Re-raise so caller knows

try:
    process_data("abc")
except ValueError as e:
    print(f"  Caller caught re-raised: {e}")

# === Custom Exceptions ===

print("\n--- Custom Exceptions ---")

class AppError(Exception):
    """Base exception for our application."""
    pass

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class NotFoundError(AppError):
    """Raised when a resource is not found."""
    def __init__(self, resource, identifier):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} '{identifier}' not found")

# Using custom exceptions
try:
    raise ValidationError("email", "must contain @")
except ValidationError as e:
    print(f"ValidationError — field={e.field}, msg={e.message}")

try:
    raise NotFoundError("User", 42)
except NotFoundError as e:
    print(f"NotFoundError — {e.resource} {e.identifier}")

# Catch all app errors
try:
    raise NotFoundError("Product", "ABC-123")
except AppError as e:
    print(f"Caught via base class: {type(e).__name__}: {e}")

# === EAFP vs LBYL ===

print("\n--- EAFP vs LBYL ---")

config = {"debug": True, "timeout": 30}

# LBYL style
if "retries" in config:
    retries = config["retries"]
else:
    retries = 3
print(f"LBYL — retries: {retries}")

# EAFP style (Pythonic)
try:
    retries = config["retries"]
except KeyError:
    retries = 3
print(f"EAFP — retries: {retries}")

# === Assertions ===

print("\n--- Assertions ---")

def calculate_average(numbers):
    assert len(numbers) > 0, "List must not be empty"
    return sum(numbers) / len(numbers)

print(f"Average of [10, 20, 30]: {calculate_average([10, 20, 30])}")

try:
    calculate_average([])
except AssertionError as e:
    print(f"AssertionError: {e}")

# === Logging Module ===

print("\n--- Logging ---")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    force=True,
)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Disk space low")
logging.error("Failed to connect to database")
logging.critical("System shutting down")

# Logging an exception with traceback
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division by zero occurred")

# === Chaining Exceptions ===

print("\n--- Exception Chaining ---")

def load_config(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Config unavailable: {path}") from e

try:
    load_config("missing_config.yaml")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"  Caused by: {e.__cause__}")
