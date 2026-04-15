"""
Day 03: Strings Deep Dive — Examples
"""

# === String Creation ===

single = 'Hello'
double = "Hello"
multiline = """This is
a multiline
string."""

print(single, double)
print(multiline)

# === Indexing ===

s = "Python"
print(f"s[0]  = {s[0]}")    # P
print(f"s[-1] = {s[-1]}")   # n
print(f"s[2]  = {s[2]}")    # t

# === Slicing ===

s = "Hello, World!"
print(f"s[0:5]   = {s[0:5]}")     # Hello
print(f"s[7:]    = {s[7:]}")       # World!
print(f"s[:5]    = {s[:5]}")       # Hello
print(f"s[::2]   = {s[::2]}")     # Hlo ol!
print(f"s[::-1]  = {s[::-1]}")    # !dlroW ,olleH

# === Escape Characters ===

print("Line one\nLine two")
print("Col1\tCol2")
print("She said \"hello\"")
print("Backslash: \\")

# === Raw Strings ===

raw = r"C:\Users\name\new_folder"
print(f"Raw string: {raw}")

# === Case Methods ===

text = "hello, world"
print(f"upper:      {text.upper()}")
print(f"lower:      {text.lower()}")
print(f"title:      {text.title()}")
print(f"capitalize: {text.capitalize()}")
print(f"swapcase:   {text.swapcase()}")

# === Search Methods ===

s = "banana"
print(f"find('ana'):      {s.find('ana')}")        # 1
print(f"count('a'):       {s.count('a')}")          # 3
print(f"startswith('ban'):{s.startswith('ban')}")    # True
print(f"endswith('ana'):  {s.endswith('ana')}")      # True

# === Modification Methods ===

padded = "  hello  "
print(f"strip:   '{padded.strip()}'")
print(f"lstrip:  '{padded.lstrip()}'")
print(f"rstrip:  '{padded.rstrip()}'")

print(f"replace: {'hello'.replace('l', 'r')}")   # herro

csv_data = "apple,banana,cherry"
print(f"split:   {csv_data.split(',')}")

fruits = ["apple", "banana", "cherry"]
print(f"join:    {', '.join(fruits)}")

print(f"center:  '{'hello'.center(15, '-')}'")
print(f"zfill:   {'42'.zfill(5)}")

# === Validation Methods ===

print(f"'hello'.isalpha():  {'hello'.isalpha()}")
print(f"'123'.isdigit():    {'123'.isdigit()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'  '.isspace():     {'  '.isspace()}")

# === f-string Formatting ===

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"Next year: {age + 1}")

pi = 3.14159
print(f"Pi (2 dec): {pi:.2f}")
print(f"Big number: {1_000_000:,}")
print(f"Left:   |{'hello':<15}|")
print(f"Right:  |{'hello':>15}|")
print(f"Center: |{'hello':^15}|")
print(f"Padded: |{'hello':*^15}|")

# === format() Method ===

print("Hello, {}!".format("Bob"))
print("Hello, {name}!".format(name="Charlie"))
print("{0} vs {1}".format("Python", "Java"))

# === String Concatenation & Repetition ===

greeting = "Hello" + " " + "World"
print(greeting)

line = "-" * 40
print(line)

words = ["Python", "is", "awesome"]
print(" ".join(words))

# === Immutability Demonstration ===

s = "hello"
# s[0] = "H"  # This would raise TypeError
s = "H" + s[1:]
print(f"New string: {s}")

# === Useful Patterns ===

# Check if a string contains a substring
print(f"'Py' in 'Python': {'Py' in 'Python'}")

# Iterate over characters
for char in "Hi!":
    print(char, end=" ")
print()

# Get string length
print(f"len('Python') = {len('Python')}")
