"""
Day 01: Python Setup & Hello World — Solutions
"""


# === Exercise 1: Hello World ===

def hello_world():
    """Return the string 'Hello, World!'."""
    return "Hello, World!"


# === Exercise 2: Greeting ===

def greeting(name):
    """Return a greeting string in the format 'Hello, <name>!'

    Example:
        greeting("Alice") -> "Hello, Alice!"
    """
    return f"Hello, {name}!"


# === Exercise 3: Repeat Message ===

def repeat_message(message, times):
    """Return the message repeated `times` times, separated by spaces.

    Example:
        repeat_message("go", 3) -> "go go go"
    """
    return " ".join([message] * times)


# === Exercise 4: Format Date ===

def format_date(year, month, day):
    """Return a date string in the format 'YYYY-MM-DD'.

    All parts should be strings. Use a dash as the separator.

    Example:
        format_date("2024", "01", "15") -> "2024-01-15"
    """
    return f"{year}-{month}-{day}"


# === Exercise 5: Personal Info ===

def personal_info(name, age, city):
    """Return a string: 'My name is <name>, I am <age> years old, and I live in <city>.'

    Example:
        personal_info("Alice", 30, "London")
        -> "My name is Alice, I am 30 years old, and I live in London."
    """
    return f"My name is {name}, I am {age} years old, and I live in {city}."
