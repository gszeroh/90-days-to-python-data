# Day 03: Strings Deep Dive

## Overview
Strings are one of the most commonly used data types in Python — especially in data
science where you regularly clean, parse, and format text. Today we explore Python's
rich set of string operations.

---

## 1. Creating Strings

```python
single = 'Hello'
double = "Hello"
multiline = """This is
a multiline
string."""
multiline_single = '''Also
multiline.'''
```

Single and double quotes are interchangeable. Use whichever avoids the need for
escaping.

---

## 2. String Indexing & Slicing

Strings are **sequences** — each character has a position (index).

```
 H   e   l   l   o
 0   1   2   3   4
-5  -4  -3  -2  -1
```

### Indexing
```python
s = "Hello"
s[0]    # 'H'
s[-1]   # 'o'
```

### Slicing `[start:stop:step]`
```python
s = "Hello, World!"
s[0:5]      # 'Hello'     — start to stop-1
s[7:]       # 'World!'    — start to end
s[:5]       # 'Hello'     — beginning to stop-1
s[::2]      # 'Hlo ol!'   — every 2nd character
s[::-1]     # '!dlroW ,olleH'  — reversed
```

---

## 3. Escape Characters

| Escape | Meaning |
|--------|---------|
| `\n`   | Newline |
| `\t`   | Tab |
| `\\`   | Backslash |
| `\'`   | Single quote |
| `\"`   | Double quote |
| `\r`   | Carriage return |
| `\0`   | Null character |

### Raw Strings
Prefix with `r` to treat backslashes as literal characters:
```python
path = r"C:\Users\name\documents"
# Without r: C:\Users\<newline>ame\documents
```

---

## 4. String Methods

Python strings have dozens of built-in methods. Here are the most important ones:

### Case Methods
```python
"hello".upper()          # "HELLO"
"HELLO".lower()          # "hello"
"hello world".title()    # "Hello World"
"hello world".capitalize()  # "Hello world"
"Hello".swapcase()       # "hELLO"
```

### Search Methods
```python
"hello".find("ll")       # 2  (index of first match, -1 if not found)
"hello".index("ll")      # 2  (same but raises ValueError if not found)
"hello".count("l")       # 2
"hello".startswith("he") # True
"hello".endswith("lo")   # True
```

### Modification Methods
```python
"  hello  ".strip()       # "hello"
"  hello  ".lstrip()      # "hello  "
"  hello  ".rstrip()      # "  hello"
"hello".replace("l", "r") # "herro"
"a,b,c".split(",")        # ["a", "b", "c"]
"-".join(["a", "b", "c"]) # "a-b-c"
"hello".center(11, "-")   # "---hello---"
"42".zfill(5)             # "00042"
```

### Validation Methods
```python
"hello".isalpha()    # True  — only letters
"123".isdigit()      # True  — only digits
"abc123".isalnum()   # True  — letters and digits
"  ".isspace()       # True  — only whitespace
"Hello".isupper()    # False
"hello".islower()    # True
```

---

## 5. String Formatting

### f-strings (Python 3.6+ — recommended)
```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Expressions inside braces
print(f"Next year I'll be {age + 1}.")

# Format specifiers
pi = 3.14159
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Big number: {1000000:,}")
print(f"Left aligned: {'hello':<20}")
print(f"Right aligned: {'hello':>20}")
print(f"Centered: {'hello':^20}")
```

### `format()` Method
```python
"Hello, {}!".format("Alice")
"Hello, {name}!".format(name="Alice")
"{0} and {1}".format("Alice", "Bob")
```

### `%` Formatting (legacy)
```python
"Hello, %s! You are %d years old." % ("Alice", 30)
```

---

## 6. String Concatenation & Repetition

```python
# Concatenation
first = "Hello"
last = "World"
full = first + ", " + last + "!"   # "Hello, World!"

# Repetition
line = "-" * 40   # "----------------------------------------"

# Join is more efficient for multiple strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)   # "Python is awesome"
```

---

## 7. Multiline Strings & `textwrap`

```python
import textwrap

long_text = """\
    This is indented in source code
    but we can remove the leading whitespace
    using textwrap.dedent()."""

print(textwrap.dedent(long_text))
```

---

## 8. String Immutability

Strings in Python are **immutable** — you cannot change individual characters.

```python
s = "hello"
# s[0] = "H"  # TypeError!
s = "H" + s[1:]  # Create a new string instead
```

---

## Key Takeaways
- Strings are immutable sequences of characters.
- Slicing with `[start:stop:step]` is powerful and versatile.
- f-strings are the modern, preferred way to format strings.
- Master `split()`, `join()`, `strip()`, `replace()`, and `find()` — they appear everywhere.
- Raw strings (`r"..."`) are essential for regex and file paths.

---

## Further Reading
- [Python Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 498 — f-strings](https://peps.python.org/pep-0498/)
- [Real Python — Strings](https://realpython.com/python-strings/)
