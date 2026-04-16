"""
Day 12: Error Handling — Solutions
"""

import functools


# === Exercise 1: Safe Division ===

def safe_divide(a, b):
    """Divide a by b, handling errors gracefully.

    Return the result of a / b.  If b is zero, return None.
    If either argument is not a number (int or float), raise a
    TypeError with the message "Both arguments must be numbers".

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        float or None: The result, or None if b is zero.

    Examples:
        safe_divide(10, 3)    -> 3.3333333333333335
        safe_divide(10, 0)    -> None
        safe_divide("a", 2)   -> raises TypeError
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    try:
        return a / b
    except ZeroDivisionError:
        return None


# === Exercise 2: Validate User Input ===

def validate_user(data):
    """Validate a user dictionary.

    The dictionary must contain:
        - "name": a non-empty string
        - "age": an integer between 0 and 150 (inclusive)
        - "email": a string containing "@"

    Return True if valid.  Raise ValueError with a descriptive message
    if any field is invalid or missing.

    Args:
        data: dict with user information.

    Returns:
        True if all validations pass.

    Raises:
        ValueError: If any field is missing or invalid.

    Examples:
        validate_user({"name": "Alice", "age": 30, "email": "a@b.com"})
            -> True
        validate_user({"name": "", "age": 30, "email": "a@b.com"})
            -> raises ValueError("name must be a non-empty string")
        validate_user({"name": "Bob", "age": -1, "email": "b@b.com"})
            -> raises ValueError("age must be an integer between 0 and 150")
    """
    if "name" not in data or not isinstance(data["name"], str) or not data["name"].strip():
        raise ValueError("name must be a non-empty string")

    if "age" not in data or not isinstance(data["age"], int) or not (0 <= data["age"] <= 150):
        raise ValueError("age must be an integer between 0 and 150")

    if "email" not in data or not isinstance(data["email"], str) or "@" not in data["email"]:
        raise ValueError("email must be a string containing @")

    return True


# === Exercise 3: Custom Exception Class ===

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance.

    Attributes:
        balance: Current balance at time of withdrawal.
        amount: Attempted withdrawal amount.
        deficit: How much the withdrawal exceeds the balance.
    """

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw {amount}: only {balance} available "
            f"(short by {self.deficit})"
        )


def process_withdrawal(balance, amount):
    """Process a withdrawal, raising InsufficientFundsError if needed.

    Args:
        balance: Current account balance (must be >= 0).
        amount: Amount to withdraw (must be > 0).

    Returns:
        float: New balance after withdrawal.

    Raises:
        ValueError: If amount <= 0 or balance < 0.
        InsufficientFundsError: If amount > balance.

    Examples:
        process_withdrawal(100, 30)  -> 70
        process_withdrawal(50, 100)  -> raises InsufficientFundsError
        process_withdrawal(50, -10)  -> raises ValueError
    """
    if balance < 0:
        raise ValueError("Balance must be non-negative")
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


# === Exercise 4: Retry Decorator ===

def retry(max_attempts=3):
    """Return a decorator that retries a function up to max_attempts times.

    If the function raises any exception, retry it.  If all attempts
    fail, re-raise the last exception.

    Args:
        max_attempts: Maximum number of times to try (default 3).

    Returns:
        A decorator function.

    Examples:
        call_count = 0

        @retry(max_attempts=3)
        def flaky():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ConnectionError("fail")
            return "success"

        flaky()       -> "success"  (called 3 times total)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator


# === Exercise 5: Error Logger ===

def run_with_logging(func, *args, **kwargs):
    """Run a function and return a result dictionary.

    Always return a dict with:
        "success": bool — whether the function completed without error
        "result":  the return value (None if an error occurred)
        "error":   None on success, or a dict with:
            "type":    exception class name (str)
            "message": exception message (str)

    Args:
        func: Callable to execute.
        *args: Positional arguments for func.
        **kwargs: Keyword arguments for func.

    Returns:
        dict: Result dictionary.

    Examples:
        run_with_logging(int, "42")
        -> {"success": True, "result": 42, "error": None}

        run_with_logging(int, "abc")
        -> {
            "success": False,
            "result": None,
            "error": {
                "type": "ValueError",
                "message": "invalid literal for int() with base 10: 'abc'"
            }
        }
    """
    try:
        result = func(*args, **kwargs)
        return {"success": True, "result": result, "error": None}
    except Exception as e:
        return {
            "success": False,
            "result": None,
            "error": {
                "type": type(e).__name__,
                "message": str(e),
            },
        }
