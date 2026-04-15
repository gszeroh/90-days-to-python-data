"""
Day 05: Control Flow — Conditionals — Examples
"""

# === Basic if Statement ===

temperature = 35

if temperature > 30:
    print("It's hot outside!")

# === if / else ===

age = 16

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# === if / elif / else ===

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")

# === Multiple elif Branches ===

day = "Wednesday"

if day == "Monday":
    print("Start of the work week")
elif day == "Friday":
    print("Almost the weekend!")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print(f"It's {day} — keep going!")

# === Nested Conditionals ===

has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Welcome to the show!")
    else:
        print("You need a guardian.")
else:
    print("Please buy a ticket first.")

# Flattened equivalent (preferred)
if not has_ticket:
    print("Please buy a ticket first.")
elif age >= 18:
    print("Welcome to the show!")
else:
    print("You need a guardian.")

# === Ternary (Conditional) Expression ===

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Inline usage
number = 7
print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")

# Nested ternary (use sparingly)
x = 0
sign = "positive" if x > 0 else ("negative" if x < 0 else "zero")
print(f"{x} is {sign}")

# === Truthy and Falsy Values ===

# Empty string is falsy
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("No name provided.")

# Zero is falsy
count = 0
if count:
    print(f"Count: {count}")
else:
    print("Count is zero.")

# None is falsy
result = None
if result is not None:
    print(f"Result: {result}")
else:
    print("No result yet.")

# Non-empty list is truthy
items = [1, 2, 3]
if items:
    print(f"Processing {len(items)} items")

# Empty list is falsy
empty = []
if not empty:
    print("List is empty!")

# === Combining Conditions with Logical Operators ===

age = 25
has_id = True
is_vip = False

if age >= 21 and has_id:
    print("You may enter the venue.")

if is_vip or age >= 65:
    print("You get a discount!")
else:
    print("Regular price.")

if not is_vip:
    print("Consider upgrading to VIP!")

# === match / case (Python 3.10+) ===

command = "quit"

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "quit" | "exit":
        print("Goodbye!")
    case _:
        print(f"Unknown command: {command}")

# Pattern matching with values
http_status = 404

match http_status:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Status code: {http_status}")

# Pattern matching with destructuring
point = (3, 0)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# === Guard Clauses Pattern ===

def categorize_age(age):
    """Demonstrate guard clauses for clean control flow."""
    if age < 0:
        return "Invalid age"
    if age < 13:
        return "Child"
    if age < 18:
        return "Teenager"
    if age < 65:
        return "Adult"
    return "Senior"

for test_age in [-1, 5, 15, 30, 70]:
    print(f"Age {test_age}: {categorize_age(test_age)}")

# === Conditional Assignment Patterns ===

# Default value with or
user_input = ""
username = user_input or "Anonymous"
print(f"Welcome, {username}!")

# Conditional expression in f-string
count = 1
print(f"You have {count} {'item' if count == 1 else 'items'} in your cart.")
