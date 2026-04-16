# Day 05: Control Flow — Conditionals

## Overview
Conditionals let your program make decisions and execute different code paths based on
conditions. They are the foundation of all program logic.

---

## 1. The `if` Statement

The simplest conditional: run a block of code only if a condition is `True`.

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
```

### Indentation Matters
Python uses **indentation** (typically 4 spaces) to define code blocks — not braces
`{}` like C or Java. Every line in the block must be indented equally.

```python
if True:
    print("This is inside the if block")
    print("So is this")
print("This is outside — always runs")
```

---

## 2. `if` / `else`

Provide an alternative path when the condition is `False`.

```python
age = 16

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
```

---

## 3. `if` / `elif` / `else`

Handle multiple conditions in sequence. Python evaluates them top-to-bottom and
executes the **first** matching block.

```python
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

print(f"Your grade: {grade}")
```

### Key Rules
- You can have **zero or more** `elif` clauses.
- The `else` clause is **optional**.
- Only **one** block executes — the first whose condition is `True`.

---

## 4. Nested Conditionals

You can place conditionals inside other conditionals.

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Welcome to the show!")
    else:
        print("You need a guardian.")
else:
    print("Please buy a ticket first.")
```

> ⚠️ **Tip:** Deeply nested conditionals hurt readability. Consider refactoring with
> early returns or combining conditions with logical operators.

```python
# Flattened equivalent
if not has_ticket:
    print("Please buy a ticket first.")
elif age >= 18:
    print("Welcome to the show!")
else:
    print("You need a guardian.")
```

---

## 5. Ternary (Conditional) Expression

A one-line shorthand for simple `if`/`else`:

```python
# Syntax: value_if_true if condition else value_if_false

status = "adult" if age >= 18 else "minor"
print(status)

# Can be used inline
print("even" if 4 % 2 == 0 else "odd")
```

Use ternary expressions for **simple** cases. For complex logic, stick with full
`if`/`else` blocks.

---

## 6. `match` / `case` (Python 3.10+)

Structural pattern matching — similar to `switch` in other languages but more
powerful.

```python
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "quit" | "exit":
        print("Goodbye!")
    case _:
        print(f"Unknown command: {command}")
```

### Key Features
- `_` is the **wildcard** pattern — matches anything (like `default` in a switch).
- `|` combines multiple patterns (OR).
- Patterns can destructure tuples, lists, and objects.

### Pattern Matching with Values
```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On the Y-axis at y={y}")
    case (x, 0):
        print(f"On the X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

---

## 7. Truthy and Falsy Values in Conditions

Python evaluates **any** value in a boolean context. These are **falsy**:

| Falsy Value | Type |
|-------------|------|
| `False` | bool |
| `None` | NoneType |
| `0`, `0.0`, `0j` | numeric zeros |
| `""` | empty string |
| `[]`, `()`, `{}`, `set()` | empty collections |

Everything else is **truthy**.

```python
name = ""

if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty!")

# Common pattern: check if a list has items
items = [1, 2, 3]
if items:
    print(f"Processing {len(items)} items")
```

---

## 8. Common Patterns

### Guard Clauses (Early Return)
```python
def process_order(order):
    if order is None:
        return "No order provided"
    if order["quantity"] <= 0:
        return "Invalid quantity"
    # Main logic here
    return f"Processing {order['quantity']} items"
```

### Conditional Assignment
```python
# Using ternary
label = "positive" if value > 0 else "non-positive"

# Using or for defaults
username = input_name or "Anonymous"
```

### Multiple Conditions with Logical Operators
```python
if age >= 18 and has_id:
    print("Access granted")

if not logged_in or session_expired:
    print("Please log in")
```

---

## Key Takeaways
- `if`/`elif`/`else` chains evaluate top-to-bottom; only the first match runs.
- Indentation defines code blocks — be consistent (4 spaces).
- Ternary expressions are concise for simple conditions.
- `match`/`case` (3.10+) is powerful for pattern matching.
- Leverage truthy/falsy values for cleaner conditions.
- Avoid deep nesting — use guard clauses and logical operators.

---

## Further Reading
- [Python Docs — if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [PEP 634 — Structural Pattern Matching](https://peps.python.org/pep-0634/)
- [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/)
