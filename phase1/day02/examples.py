"""
Day 02: Variables & Data Types — Examples
"""

# === Variable Assignment ===

name = "Alice"
age = 30
height = 5.7
is_student = True

print(name, age, height, is_student)

# === Multiple Assignment ===

x, y, z = 10, 20, 30
print(x, y, z)

a = b = c = 0
print(a, b, c)

# === Swapping Variables ===

x, y = 1, 2
print("Before swap:", x, y)
x, y = y, x
print("After swap:", x, y)

# === Core Data Types ===

# int
count = 42
big = 1_000_000
print(type(count), count)
print(type(big), big)

# float
price = 19.99
scientific = 2.5e10
print(type(price), price)
print(type(scientific), scientific)

# str
greeting = "Hello, World!"
single = 'single quotes work too'
multiline = """This string
spans multiple
lines."""
print(type(greeting), greeting)
print(multiline)

# bool
is_active = True
is_empty = False
print(type(is_active), is_active)
print("bool is subclass of int:", True == 1, False == 0)

# None
result = None
print(type(result), result)

# === The type() Function ===

values = [42, 3.14, "hello", True, None]
for v in values:
    print(f"type({v!r}) = {type(v).__name__}")

# === Type Conversion (Casting) ===

# str -> int
age_str = "25"
age_int = int(age_str)
print(f"int('{age_str}') = {age_int}, type = {type(age_int).__name__}")

# str -> float
pi_str = "3.14159"
pi_float = float(pi_str)
print(f"float('{pi_str}') = {pi_float}")

# int -> str
num = 100
num_str = str(num)
print(f"str({num}) = '{num_str}', type = {type(num_str).__name__}")

# float -> int (truncates, does not round)
print(f"int(3.9) = {int(3.9)}")
print(f"int(-3.9) = {int(-3.9)}")

# Implicit conversion: int + float -> float
result = 5 + 2.0
print(f"5 + 2.0 = {result}, type = {type(result).__name__}")

# === Truthy and Falsy Values ===

falsy_values = [0, 0.0, "", None, False, [], {}, set()]
for v in falsy_values:
    print(f"bool({v!r:10s}) = {bool(v)}")

print()

truthy_values = [1, -1, 3.14, "hello", True, [1], {"a": 1}]
for v in truthy_values:
    print(f"bool({str(v):12s}) = {bool(v)}")

# === Constants (by convention) ===

PI = 3.14159
MAX_RETRIES = 5
BASE_URL = "https://api.example.com"

print(f"PI = {PI}")
print(f"MAX_RETRIES = {MAX_RETRIES}")
print(f"BASE_URL = {BASE_URL}")

# === Floating-Point Precision ===

print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
