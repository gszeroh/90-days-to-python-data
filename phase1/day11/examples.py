"""
Day 11: File I/O — Examples
"""

import csv
import json
import os
from pathlib import Path

# === Writing and Reading Text Files ===

print("--- Writing and Reading Text Files ---")

# Write a file using a context manager
with open("sample.txt", "w") as f:
    f.write("Hello, File I/O!\n")
    f.write("This is line two.\n")
    f.write("And line three.\n")

# Read the entire file
with open("sample.txt", "r") as f:
    content = f.read()
print(f"Full content:\n{content}")

# Read line by line (memory-efficient)
print("Line by line:")
with open("sample.txt", "r") as f:
    for line in f:
        print(f"  {line.strip()}")

# Read all lines into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(f"\nAs list: {lines}")

# === File Modes ===

print("\n--- File Modes ---")

# Append mode
with open("sample.txt", "a") as f:
    f.write("Appended line four.\n")

with open("sample.txt", "r") as f:
    print(f"After append:\n{f.read()}")

# Write mode truncates
with open("fresh.txt", "w") as f:
    f.write("Brand new content.\n")

with open("fresh.txt", "r") as f:
    print(f"Fresh file: {f.read().strip()}")

# === Using print() to Write Files ===

print("\n--- print() to file ---")

with open("printed.txt", "w") as f:
    print("Name:", "Alice", file=f)
    print("Age:", 30, file=f)
    print("Score:", 95.5, file=f)

with open("printed.txt", "r") as f:
    print(f.read())

# === CSV Files ===

print("--- CSV Files ---")

# Write CSV
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerows([
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"],
    ])
print("Wrote people.csv")

# Read CSV with csv.reader
print("\nReading with csv.reader:")
with open("people.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"  Header: {header}")
    for row in reader:
        print(f"  Row: {row}")

# Read CSV with DictReader
print("\nReading with DictReader:")
with open("people.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']} is {row['age']} from {row['city']}")

# Write CSV with DictWriter
with open("scores.csv", "w", newline="") as f:
    fieldnames = ["student", "math", "science"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"student": "Alice", "math": 92, "science": 88})
    writer.writerow({"student": "Bob", "math": 85, "science": 91})

print("\nWrote scores.csv")
with open("scores.csv", "r") as f:
    print(f.read())

# === JSON Files ===

print("--- JSON Files ---")

data = {
    "name": "Alice",
    "age": 30,
    "languages": ["Python", "JavaScript", "SQL"],
    "address": {
        "city": "New York",
        "zip": "10001",
    },
}

# Write JSON
with open("profile.json", "w") as f:
    json.dump(data, f, indent=2)
print("Wrote profile.json")

# Read JSON
with open("profile.json", "r") as f:
    loaded = json.load(f)
print(f"Loaded: {loaded}")
print(f"Name: {loaded['name']}")
print(f"Languages: {loaded['languages']}")

# JSON string conversion
json_str = json.dumps(data, indent=2)
print(f"\nJSON string:\n{json_str}")

parsed = json.loads(json_str)
print(f"\nParsed back: {parsed['name']}")

# === pathlib ===

print("\n--- pathlib ---")

# Build paths with / operator
p = Path("data") / "reports" / "summary.txt"
print(f"Path: {p}")
print(f"  name:   {p.name}")
print(f"  stem:   {p.stem}")
print(f"  suffix: {p.suffix}")
print(f"  parent: {p.parent}")
print(f"  parts:  {p.parts}")

# Current directory
cwd = Path.cwd()
print(f"\nCurrent dir: {cwd}")

# Check existence
print(f"sample.txt exists: {Path('sample.txt').exists()}")
print(f"sample.txt is file: {Path('sample.txt').is_file()}")
print(f". is dir: {Path('.').is_dir()}")

# Read/write shortcuts
Path("pathlib_demo.txt").write_text("Written via pathlib!\n")
content = Path("pathlib_demo.txt").read_text()
print(f"\npathlib read: {content.strip()}")

# List directory contents
print("\nFiles in current directory:")
for child in sorted(Path(".").iterdir()):
    kind = "DIR " if child.is_dir() else "FILE"
    print(f"  [{kind}] {child.name}")

# Glob for .py files
print("\n.py files (glob):")
for py_file in sorted(Path(".").glob("*.py")):
    print(f"  {py_file}")

# === os.path (legacy) ===

print("\n--- os.path ---")

joined = os.path.join("data", "reports", "file.csv")
print(f"os.path.join: {joined}")

print(f"basename: {os.path.basename('/a/b/c.txt')}")
print(f"dirname:  {os.path.dirname('/a/b/c.txt')}")
print(f"splitext: {os.path.splitext('archive.tar.gz')}")
print(f"exists:   {os.path.exists('sample.txt')}")

# File size
size = os.path.getsize("sample.txt")
print(f"sample.txt size: {size} bytes")

# === Cleanup demo files ===

for f in ["sample.txt", "fresh.txt", "printed.txt", "people.csv",
          "scores.csv", "profile.json", "pathlib_demo.txt"]:
    Path(f).unlink(missing_ok=True)

print("\nCleaned up demo files.")
