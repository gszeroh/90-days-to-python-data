"""
Day 13: Modules & Packages — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""


# === Exercise 1: Math Utilities Module ===

def math_summary(numbers):
    """Return a summary dictionary of a list of numbers.

    Use the `math` module where appropriate.

    The returned dict should have:
        "count":   number of elements
        "sum":     sum of all elements
        "mean":    arithmetic mean
        "min":     minimum value
        "max":     maximum value
        "sqrt_of_sum": square root of the sum (use math.sqrt)

    If the list is empty, return all values as 0 (sqrt_of_sum as 0.0).

    Args:
        numbers: List of int or float.

    Returns:
        dict: Summary statistics.

    Examples:
        math_summary([1, 4, 9, 16])
        -> {
            "count": 4,
            "sum": 30,
            "mean": 7.5,
            "min": 1,
            "max": 16,
            "sqrt_of_sum": 5.477225575051661,
        }

        math_summary([]) -> {"count": 0, "sum": 0, "mean": 0,
                             "min": 0, "max": 0, "sqrt_of_sum": 0.0}
    """
    pass


# === Exercise 2: Random Password Generator ===

def generate_password(length=12, use_digits=True, use_special=True):
    """Generate a random password string.

    Use the `random` and `string` modules.

    The password should contain:
        - Lowercase letters (always included)
        - Uppercase letters (always included)
        - Digits (if use_digits is True)
        - Special characters from "!@#$%^&*" (if use_special is True)

    The password must contain at least one character from each included
    category.  The minimum length is 4.  If length < 4, raise ValueError.

    Args:
        length: Desired password length (default 12, minimum 4).
        use_digits: Include digits (default True).
        use_special: Include special characters (default True).

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length < 4.

    Examples:
        pw = generate_password(16)
        len(pw) == 16   # True
        any(c.islower() for c in pw)  # True
        any(c.isupper() for c in pw)  # True
    """
    pass


# === Exercise 3: Date Utilities ===

def days_between(date_str_a, date_str_b):
    """Calculate the number of days between two date strings.

    Use the `datetime` module.  Date strings are in "YYYY-MM-DD" format.
    Return the absolute number of days (always non-negative).

    Args:
        date_str_a: First date as a string.
        date_str_b: Second date as a string.

    Returns:
        int: Absolute number of days between the two dates.

    Examples:
        days_between("2024-01-01", "2024-01-31") -> 30
        days_between("2024-03-01", "2024-01-01") -> 60
        days_between("2024-06-15", "2024-06-15") -> 0
    """
    pass


# === Exercise 4: Organize Functions by Category ===

def categorize_builtins():
    """Categorize a selection of Python built-in functions.

    Return a dictionary grouping these built-in names by category:

        "type_conversion": ["bool", "int", "float", "str", "list",
                            "tuple", "set", "dict"]
        "math":            ["abs", "round", "min", "max", "sum", "pow"]
        "iteration":       ["range", "enumerate", "zip", "map",
                            "filter", "sorted", "reversed"]
        "io":              ["print", "input", "open"]

    Each value should be a **sorted** list of function names (strings).

    Returns:
        dict: Category name → sorted list of built-in function names.

    Examples:
        result = categorize_builtins()
        result["math"]  -> ["abs", "max", "min", "pow", "round", "sum"]
    """
    pass


# === Exercise 5: Module Inspector ===

def inspect_module(module_name):
    """Import a module by name and return info about it.

    Use `importlib.import_module` to import the module dynamically.

    Return a dict with:
        "name":       module's __name__
        "doc":        first line of module's docstring (or "" if None)
        "functions":  sorted list of public function names
                      (callable attributes that don't start with '_')
        "constants":  sorted list of public ALL_CAPS attribute names
                      (non-callable, all uppercase, no leading '_')

    Args:
        module_name: Name of the module to inspect (e.g. "math").

    Returns:
        dict: Module information.

    Examples:
        info = inspect_module("math")
        info["name"]  -> "math"
        "sqrt" in info["functions"]  -> True
        "pi" in info["constants"]    -> False  (not ALL_CAPS)
        "PI" would be in constants if it existed
    """
    pass
