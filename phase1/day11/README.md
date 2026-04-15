# Day 11: File I/O

## Overview
Programs become truly useful when they can persist and exchange data. Python
provides a rich set of tools for **reading** and **writing** files — from plain
text and CSV spreadsheets to structured JSON documents. Combined with the
**`pathlib`** module for cross-platform path manipulation, you can build robust
data pipelines that load, transform, and save information reliably.

---

## 1. Opening and Closing Files

```python
# Basic open/close
f = open("data.txt", "r")
content = f.read()
f.close()                       # Don't forget this!
```

> ⚠️ Forgetting to call `close()` can lead to data loss and resource leaks.

---

## 2. Context Managers — The `with` Statement

The `with` statement guarantees the file is closed when the block exits, even
if an exception occurs.

```python
with open("data.txt", "r") as f:
    content = f.read()
# f is automatically closed here
```

**Always use `with` for file operations.**

---

## 3. File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read text (default) — file must exist |
| `"w"` | Write text — creates or **truncates** |
| `"a"` | Append text — creates or appends |
| `"x"` | Exclusive create — fails if file exists |
| `"rb"` | Read binary |
| `"wb"` | Write binary |
| `"r+"` | Read and write (file must exist) |

```python
# Write
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

# Append
with open("output.txt", "a") as f:
    f.write("Another line.\n")
```

---

## 4. Reading Techniques

```python
with open("data.txt", "r") as f:
    # Read entire file as a single string
    content = f.read()

    # Read one line at a time
    f.seek(0)
    first_line = f.readline()

    # Read all lines into a list
    f.seek(0)
    lines = f.readlines()       # Each element includes '\n'

    # Iterate line by line (memory-efficient)
    f.seek(0)
    for line in f:
        print(line.strip())
```

> 💡 **Tip:** Iterating directly over the file object is the most
> memory-efficient approach for large files.

---

## 5. Writing Techniques

```python
# Write a single string
with open("out.txt", "w") as f:
    f.write("line one\n")
    f.write("line two\n")

# Write multiple lines at once
lines = ["alpha\n", "beta\n", "gamma\n"]
with open("out.txt", "w") as f:
    f.writelines(lines)         # Does NOT add newlines automatically

# print() to a file
with open("out.txt", "w") as f:
    print("Hello", "World", sep=", ", file=f)
```

---

## 6. Working with CSV Files

The `csv` module handles the nuances of the CSV format (quoting, escaping,
different delimiters).

```python
import csv

# Reading CSV
with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)       # First row
    for row in reader:
        print(row)              # Each row is a list of strings

# Writing CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 30, "NYC"])
    writer.writerows([
        ["Bob", 25, "LA"],
        ["Charlie", 35, "Chicago"],
    ])

# DictReader / DictWriter — access columns by name
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

> Always pass `newline=""` when opening CSV files to prevent blank-row issues
> on Windows.

---

## 7. Working with JSON Files

JSON is the lingua franca for web APIs and configuration files.

```python
import json

# Read JSON
with open("config.json", "r") as f:
    data = json.load(f)         # Parse file → Python dict/list

# Write JSON
with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

# Convert between strings and objects
json_string = json.dumps({"key": "value"}, indent=2)
obj = json.loads(json_string)
```

| Function | Direction |
|----------|-----------|
| `json.load(file)` | File → Python object |
| `json.dump(obj, file)` | Python object → File |
| `json.loads(string)` | String → Python object |
| `json.dumps(obj)` | Python object → String |

---

## 8. Path Manipulation with `pathlib`

`pathlib` provides an object-oriented interface for filesystem paths.

```python
from pathlib import Path

# Create path objects
p = Path("data") / "reports" / "summary.txt"
print(p)            # data/reports/summary.txt

# Useful properties
p.name              # "summary.txt"
p.stem              # "summary"
p.suffix            # ".txt"
p.parent            # Path("data/reports")
p.parts             # ("data", "reports", "summary.txt")

# Check existence
p.exists()
p.is_file()
p.is_dir()

# Read / Write shortcuts
p.write_text("Hello, pathlib!")
content = p.read_text()

# Iterate directory contents
for child in Path(".").iterdir():
    print(child)

# Glob patterns
for py_file in Path(".").glob("**/*.py"):
    print(py_file)
```

---

## 9. Legacy Path Tools — `os.path`

```python
import os

os.path.join("data", "file.txt")       # "data/file.txt"
os.path.exists("data/file.txt")         # True/False
os.path.basename("/a/b/c.txt")          # "c.txt"
os.path.dirname("/a/b/c.txt")           # "/a/b"
os.path.splitext("file.tar.gz")         # ("file.tar", ".gz")
os.path.getsize("data.txt")             # Size in bytes
```

> 💡 Prefer `pathlib` for new code — it is more readable and Pythonic.

---

## 10. Encoding

```python
# Specify encoding explicitly (good practice)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Handle encoding errors
with open("data.txt", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()
```

---

## Key Takeaways
- Always use the `with` statement for file I/O to ensure proper cleanup.
- Choose the right file mode (`r`, `w`, `a`, `rb`, `wb`) for your task.
- Use `csv.reader` / `csv.DictReader` for CSV — don't parse by hand.
- Use `json.load` / `json.dump` for JSON serialization.
- Prefer `pathlib.Path` over `os.path` for path manipulation.
- Specify `encoding="utf-8"` explicitly to avoid platform-dependent defaults.

---

## Further Reading
- [Python Docs — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Docs — csv module](https://docs.python.org/3/library/csv.html)
- [Python Docs — json module](https://docs.python.org/3/library/json.html)
- [Python Docs — pathlib](https://docs.python.org/3/library/pathlib.html)
- [Real Python — Working with Files](https://realpython.com/working-with-files-in-python/)
