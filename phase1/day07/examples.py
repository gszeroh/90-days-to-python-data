"""
Day 07: Functions — Basics — Examples
"""

# === Defining and Calling Functions ===

def greet():
    """Print a simple greeting."""
    print("Hello, World!")

greet()


def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# === Parameters and Arguments ===

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# Multiple parameters
def describe_pet(name, animal_type, age):
    """Print a description of a pet."""
    print(f"{name} is a {age}-year-old {animal_type}.")

describe_pet("Buddy", "dog", 3)

# === Return Values ===

def square(n):
    """Return n squared."""
    return n ** 2

print(f"7 squared = {square(7)}")

# Returning multiple values (as a tuple)
def divide(a, b):
    """Return the quotient and remainder."""
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

# Functions without return give None
def say_hello():
    print("Hi!")

result = say_hello()
print(f"Return value: {result}")  # None

# === Default Arguments ===

def greet_with_style(name, greeting="Hello", punctuation="!"):
    """Greet with customizable greeting and punctuation."""
    print(f"{greeting}, {name}{punctuation}")

greet_with_style("Alice")
greet_with_style("Bob", "Good morning")
greet_with_style("Charlie", "Hey", ".")

# Safe mutable defaults
def append_to_list(value, items=None):
    """Safely append a value to a list."""
    if items is None:
        items = []
    items.append(value)
    return items

print(append_to_list(1))        # [1]
print(append_to_list(2))        # [2] — not [1, 2]
print(append_to_list(3, [10]))  # [10, 3]

# === Keyword Arguments ===

def create_profile(name, age, city="Unknown", role="Member"):
    """Create a user profile dictionary."""
    return {
        "name": name,
        "age": age,
        "city": city,
        "role": role,
    }

# Positional
print(create_profile("Alice", 30, "NYC", "Admin"))

# Keyword — order doesn't matter
print(create_profile(age=25, name="Bob", role="Editor"))

# Mixed — positional first, then keyword
print(create_profile("Charlie", 35, role="Viewer"))

# === Scope — Local vs. Global ===

x = "global"

def show_scope():
    """Demonstrate local vs. global scope."""
    y = "local"
    print(f"Inside function: x = {x}, y = {y}")

show_scope()
print(f"Outside function: x = {x}")
# print(y)  # Would raise NameError

# Shadowing a global variable
z = 100

def shadow_example():
    """Local variable shadows the global."""
    z = 999
    print(f"Inside: z = {z}")

shadow_example()
print(f"Outside: z = {z}")  # Still 100

# Using global keyword (avoid when possible)
counter = 0

def increment():
    """Increment the global counter."""
    global counter
    counter += 1

increment()
increment()
increment()
print(f"Counter after 3 increments: {counter}")

# === LEGB Rule Demo ===

def outer():
    """Demonstrate enclosing scope."""
    msg = "enclosing"

    def inner():
        print(f"Inner sees: {msg}")

    inner()

outer()

# === Docstrings ===

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return celsius * 9 / 5 + 32

# Using the function
temps_c = [0, 20, 37, 100]
for c in temps_c:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f}°F")

# Accessing the docstring
print(f"\nDocstring:\n{celsius_to_fahrenheit.__doc__}")

# === Type Hints ===

def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b

def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0

print(f"\nmultiply(6, 7) = {multiply(6, 7)}")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")

# === Boolean / Predicate Functions ===

def is_positive(n):
    """Return True if n is positive."""
    return n > 0

def is_leap_year(year):
    """Return True if year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

for year in [2000, 1900, 2024, 2023]:
    print(f"{year}: leap={is_leap_year(year)}")

# === Early Return Pattern ===

def get_ticket_price(age):
    """Return ticket price with guard clauses."""
    if age < 0:
        return None
    if age < 12:
        return 5
    if age >= 65:
        return 7
    return 12

for age in [-1, 5, 30, 70]:
    price = get_ticket_price(age)
    print(f"Age {age}: price = {price}")

# === Functions Calling Functions ===

def hypotenuse(a, b):
    """Calculate the hypotenuse of a right triangle."""
    return (a ** 2 + b ** 2) ** 0.5

def distance(x1, y1, x2, y2):
    """Calculate distance between two points using hypotenuse."""
    return hypotenuse(x2 - x1, y2 - y1)

print(f"\nDistance from (0,0) to (3,4): {distance(0, 0, 3, 4)}")
print(f"Distance from (1,2) to (4,6): {distance(1, 2, 4, 6):.2f}")
