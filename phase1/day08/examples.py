"""
Day 08: Functions — Advanced — Examples
"""

# === *args — Variable Positional Arguments ===

def add_all(*args):
    """Sum any number of arguments."""
    print(f"args = {args} (type: {type(args).__name__})")
    return sum(args)

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))

# Mixing regular params with *args
def greet(greeting, *names):
    """Greet multiple people."""
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")

# === **kwargs — Variable Keyword Arguments ===

def build_profile(**kwargs):
    """Build a profile dict from keyword arguments."""
    print(f"kwargs = {kwargs} (type: {type(kwargs).__name__})")
    return kwargs

profile = build_profile(name="Alice", age=30, city="NYC")
print(f"Profile: {profile}")

# Mixing *args and **kwargs
def universal(*args, **kwargs):
    """Accept anything."""
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")

print("\nuniversal(1, 2, 3, x=10, y=20):")
universal(1, 2, 3, x=10, y=20)

# Full parameter order
def full_example(a, b, *args, option=True, **kwargs):
    """Demonstrate the full parameter order."""
    print(f"  a={a}, b={b}")
    print(f"  args={args}")
    print(f"  option={option}")
    print(f"  kwargs={kwargs}")

print("\nfull_example(1, 2, 3, 4, option=False, x=10):")
full_example(1, 2, 3, 4, option=False, x=10)

# === Unpacking Arguments ===

def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
print(f"\nUnpacking list: add(*{numbers}) = {add(*numbers)}")

params = {"a": 100, "b": 200, "c": 300}
print(f"Unpacking dict: add(**{params}) = {add(**params)}")

# === Lambda Functions ===

square = lambda x: x ** 2
print(f"\nlambda square(5) = {square(5)}")

add_lambda = lambda a, b: a + b
print(f"lambda add(3, 4) = {add_lambda(3, 4)}")

# Lambda with conditional
classify = lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero")
for val in [-3, 0, 7]:
    print(f"  {val} is {classify(val)}")

# Sorting with lambda
pairs = [(1, "banana"), (3, "apple"), (2, "cherry")]
sorted_pairs = sorted(pairs, key=lambda p: p[1])
print(f"\nSorted by name: {sorted_pairs}")

students = [
    {"name": "Charlie", "grade": 85},
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 78},
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print("Sorted by grade (descending):")
for s in sorted_students:
    print(f"  {s['name']}: {s['grade']}")

# === map() ===

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(f"\nmap — squared: {squared}")

# map with a named function
def fahrenheit_to_celsius(f):
    return round((f - 32) * 5 / 9, 1)

temps_f = [32, 68, 100, 212]
temps_c = list(map(fahrenheit_to_celsius, temps_f))
print(f"map — F to C: {temps_f} → {temps_c}")

# map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(f"map — pairwise sum: {sums}")

# === filter() ===

numbers = list(range(1, 21))

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nfilter — evens from 1-20: {evens}")

# Filter strings
words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))  # None removes falsy values
print(f"filter(None) — non-empty: {non_empty}")

# Filter with a named function
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

primes = list(filter(is_prime, range(2, 50)))
print(f"filter — primes under 50: {primes}")

# === reduce() ===

from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)
print(f"\nreduce — product: {product}")

# Find the maximum using reduce
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"reduce — max: {maximum}")

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print(f"reduce — flatten: {flat}")

# === Closures ===

def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"\nClosure — double(5) = {double(5)}")
print(f"Closure — triple(5) = {triple(5)}")

# Closure with state using nonlocal
def make_counter(start=0):
    """Return an increment function that maintains state."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(f"\nCounter: {counter()}, {counter()}, {counter()}")

counter_from_10 = make_counter(10)
print(f"Counter from 10: {counter_from_10()}, {counter_from_10()}")

# Closure as a function factory
def make_greeting(template):
    """Create a greeting function from a template."""
    def greet(name):
        return template.format(name=name)
    return greet

formal = make_greeting("Dear {name}, it is a pleasure.")
casual = make_greeting("Hey {name}!")

print(f"\n{formal('Dr. Smith')}")
print(casual("Alice"))

# === Decorators ===

from functools import wraps

def log_call(func):
    """Decorator that logs function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  → Calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"  ← {func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def multiply(a, b):
    """Return a * b."""
    return a * b

print("\nDecorator — log_call:")
multiply(6, 7)

# Verify wraps preserves metadata
print(f"Function name: {multiply.__name__}")
print(f"Docstring: {multiply.__doc__}")

# Timer decorator
import time

def timer(func):
    """Decorator that measures execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum numbers from 0 to n."""
    return sum(range(n + 1))

print("\nDecorator — timer:")
slow_sum(1_000_000)

# Decorator with arguments
def repeat(n):
    """Decorator that calls a function n times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(message):
    """Print a message."""
    print(f"  {message}")

print("\nDecorator with args — repeat(3):")
say("Hello!")

# === functools Extras ===

from functools import lru_cache, partial

# lru_cache for memoization
@lru_cache(maxsize=128)
def fib(n):
    """Return the nth Fibonacci number (memoized)."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f"\nlru_cache — fib(30) = {fib(30)}")
print(f"Cache info: {fib.cache_info()}")

# partial — fix some arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"\npartial — square(5) = {square(5)}")
print(f"partial — cube(3) = {cube(3)}")
