"""
Day 13: Modules & Packages — Examples
"""

# === Importing Standard Library Modules ===

print("--- Importing Standard Library Modules ---")

import math

print(f"math.pi      = {math.pi}")
print(f"math.e       = {math.e}")
print(f"math.sqrt(16)= {math.sqrt(16)}")
print(f"math.ceil(4.2)= {math.ceil(4.2)}")
print(f"math.floor(4.8)= {math.floor(4.8)}")
print(f"math.log(100, 10) = {math.log(100, 10)}")

# === from ... import ===

print("\n--- from ... import ---")

from math import sqrt, pi, factorial
print(f"sqrt(25) = {sqrt(25)}")
print(f"pi = {pi}")
print(f"factorial(5) = {factorial(5)}")

# === Aliased Imports ===

print("\n--- Aliased Imports ---")

import datetime as dt

today = dt.date.today()
now = dt.datetime.now()
print(f"Today: {today}")
print(f"Now:   {now.strftime('%Y-%m-%d %H:%M:%S')}")

delta = dt.timedelta(days=7)
next_week = today + delta
print(f"Next week: {next_week}")

from collections import Counter as Cnt
c = Cnt("abracadabra")
print(f"\nCounter: {c}")

# === The random Module ===

print("\n--- random module ---")

import random

random.seed(42)  # For reproducibility

print(f"randint(1, 10):  {random.randint(1, 10)}")
print(f"random():        {random.random():.4f}")
print(f"uniform(1, 100): {random.uniform(1, 100):.2f}")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"choice: {random.choice(fruits)}")
print(f"sample(3): {random.sample(fruits, 3)}")

shuffled = fruits.copy()
random.shuffle(shuffled)
print(f"shuffled: {shuffled}")

# === The os and sys Modules ===

print("\n--- os and sys ---")

import os
import sys

print(f"Current working dir: {os.getcwd()}")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

print(f"\nsys.path (first 3 entries):")
for p in sys.path[:3]:
    print(f"  {p}")

# === The __name__ Guard ===

print("\n--- __name__ guard ---")

print(f"This module's __name__: {__name__}")
print(f"math's __name__: {math.__name__}")

# Simulating the guard pattern
def main():
    print("  This runs only when the script is executed directly.")

if __name__ == "__main__":
    main()

# === Module Attributes ===

print("\n--- Module Attributes ---")

print(f"math.__name__: {math.__name__}")
print(f"math.__doc__[:60]: {math.__doc__[:60]}...")
print(f"math.__file__: {getattr(math, '__file__', 'built-in')}")

# List functions in a module (first 10)
public_names = [name for name in dir(math) if not name.startswith("_")]
print(f"\nPublic names in math (first 10): {public_names[:10]}")

# === Creating and Using a Simple Module ===

print("\n--- Creating a module at runtime ---")

# We'll write a small module file and import it
from pathlib import Path

module_code = '''"""A tiny utility module."""

def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

VERSION = "1.0.0"
'''

Path("tiny_module.py").write_text(module_code)

import importlib
tiny = importlib.import_module("tiny_module")

print(f"tiny_module.greet('World'): {tiny.greet('World')}")
print(f"tiny_module.add(3, 4): {tiny.add(3, 4)}")
print(f"tiny_module.VERSION: {tiny.VERSION}")

# === Package Structure Demo ===

print("\n--- Package Structure (conceptual) ---")

# We'll create a mini package to demonstrate
pkg_dir = Path("demo_pkg")
pkg_dir.mkdir(exist_ok=True)

(pkg_dir / "__init__.py").write_text(
    '"""Demo package."""\n'
    'from .helpers import double\n'
    '__all__ = ["double"]\n'
)

(pkg_dir / "helpers.py").write_text(
    'def double(x):\n'
    '    """Return x * 2."""\n'
    '    return x * 2\n'
    '\n'
    'def triple(x):\n'
    '    """Return x * 3."""\n'
    '    return x * 3\n'
)

# Import from our package
import demo_pkg

print(f"demo_pkg.double(5): {demo_pkg.double(5)}")

from demo_pkg.helpers import triple
print(f"triple(5): {triple(5)}")

# === Inspecting What a Module Provides ===

print("\n--- dir() and help() ---")

print(f"dir(demo_pkg): {[n for n in dir(demo_pkg) if not n.startswith('_')]}")
print(f"demo_pkg.__all__: {demo_pkg.__all__}")

# === Cleanup ===

import shutil
Path("tiny_module.py").unlink(missing_ok=True)
shutil.rmtree("demo_pkg", ignore_errors=True)

# Clean up cached module files
cache = Path("__pycache__")
if cache.exists():
    shutil.rmtree(cache, ignore_errors=True)

print("\nCleaned up demo files.")
