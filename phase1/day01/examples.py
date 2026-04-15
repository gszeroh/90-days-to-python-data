"""
Day 01: Python Setup & Hello World — Examples
"""

# === Hello World ===

print("Hello, World!")

# === Print Variations ===

# Multiple arguments — separated by a space by default
print("Hello", "Python", "World")

# Custom separator
print("2024", "01", "15", sep="-")

# Custom end character (no newline)
print("Loading", end="... ")
print("Done!")

# Printing numbers alongside strings
print("The answer is", 42)
print("Pi is approximately", 3.14159)

# Empty print produces a blank line
print()

# === Comments ===

# This is a single-line comment — Python ignores everything after the #
name = "Alice"  # Inline comment: assigning a name

# You can stack single-line comments
# to write longer explanations
# across multiple lines.

# === Docstrings ===

"""
Docstrings are triple-quoted strings.
They are often used at the top of modules, functions,
and classes to describe their purpose.
"""

# === REPL-Style Exploration ===
# In the REPL you can type expressions and see their value immediately.
# In a script, you need print() to see output.

print(2 + 3)          # 5
print(10 / 3)         # 3.3333...
print("Hello" * 3)    # HelloHelloHello
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>

# === Escape Characters in print() ===

print("Line one\nLine two")      # \n = newline
print("Column1\tColumn2")        # \t = tab
print("She said \"hello\"")      # \" = literal quote
print('It\'s a beautiful day')   # \' = literal single quote
print("Backslash: \\")           # \\ = literal backslash

# === Using sep and end Together ===

print("Python", "is", "fun", sep=" ~ ", end="!\n")
# Output: Python ~ is ~ fun!
