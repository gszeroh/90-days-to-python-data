# Day 01: Python Setup & Hello World

## Overview
Welcome to Day 1 of your 90-day journey to Python for Data Science! Today we set up
our development environment, write our first program, and explore the building blocks
of every Python script.

---

## 1. Installing Python

### Windows
1. Visit [python.org/downloads](https://www.python.org/downloads/).
2. Download the latest **Python 3.x** installer.
3. **Check "Add Python to PATH"** during installation.
4. Verify in a terminal:
   ```bash
   python --version
   ```

### macOS
1. Install via Homebrew (recommended):
   ```bash
   brew install python
   ```
2. Or download from [python.org](https://www.python.org/downloads/).
3. Verify:
   ```bash
   python3 --version
   ```

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

---

## 2. Choosing an IDE / Editor

| Editor | Best For | Key Feature |
|--------|----------|-------------|
| **VS Code** | General-purpose, lightweight | Extensions ecosystem, integrated terminal |
| **PyCharm** | Dedicated Python development | Smart code completion, built-in debugger |
| **Jupyter Notebook** | Data science exploration | Inline visualization, cell-based execution |

### VS Code Quick Setup
1. Install [VS Code](https://code.visualstudio.com/).
2. Install the **Python** extension by Microsoft.
3. Select a Python interpreter: `Ctrl+Shift+P` → *Python: Select Interpreter*.

### PyCharm Quick Setup
1. Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/).
2. Create a new project — PyCharm auto-detects your Python installation.

---

## 3. The Python REPL (Read-Eval-Print Loop)

The REPL is an interactive shell where you can type Python code and see results
immediately. Start it by typing `python` or `python3` in your terminal.

```python
>>> 2 + 3
5
>>> "Hello, World!"
'Hello, World!'
>>> type(42)
<class 'int'>
```

- **Read** — Python reads your input.
- **Eval** — Python evaluates the expression.
- **Print** — Python prints the result.
- **Loop** — Python waits for more input.

Exit the REPL with `exit()` or `Ctrl+D` (Linux/macOS) / `Ctrl+Z` then Enter (Windows).

---

## 4. Your First Program — Hello, World!

Create a file named `hello.py`:

```python
print("Hello, World!")
```

Run it:
```bash
python hello.py
```

That single line is a complete Python program. `print()` is a **built-in function**
that sends text to the console.

---

## 5. The `print()` Function

`print()` is more versatile than it first appears:

```python
# Multiple arguments (separated by spaces by default)
print("Hello", "World")          # Hello World

# Custom separator
print("2024", "01", "15", sep="-")  # 2024-01-15

# Custom end character (default is newline)
print("Loading", end="...")      # Loading...

# Printing numbers and mixed types
print("The answer is", 42)       # The answer is 42
```

### Key Parameters
| Parameter | Default | Purpose |
|-----------|---------|---------|
| `sep`     | `" "`   | Separator between multiple arguments |
| `end`     | `"\n"`  | String appended after the last argument |

---

## 6. Comments

Comments are notes in your code that Python ignores. They exist for humans.

```python
# This is a single-line comment

print("Hello")  # Inline comment

# Multi-line comments use multiple single-line comments
# There is no dedicated multi-line comment syntax,
# but triple-quoted strings are sometimes used as such.

"""
This is a docstring (documentation string).
It is technically a string literal, not a comment,
but it is often used for multi-line documentation.
"""
```

### Best Practices
- Write comments that explain **why**, not **what**.
- Keep comments up to date with the code.
- Use docstrings (`"""..."""`) for functions, classes, and modules.

---

## Key Takeaways
- Python 3.x is the current standard — always use Python 3.
- The REPL is perfect for quick experiments.
- `print()` is your primary tool for output.
- Comments make code readable; prefer explaining intent over mechanics.

---

## Further Reading
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [VS Code Python Docs](https://code.visualstudio.com/docs/python/python-tutorial)
- [Real Python — Getting Started](https://realpython.com/python-first-steps/)
