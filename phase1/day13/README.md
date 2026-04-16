# Day 13: Modules & Packages

## Overview
As your code grows, you need to **organize** it into reusable, maintainable
pieces. Python's module and package system lets you split code across files,
share it between projects, and leverage thousands of third-party libraries.
Understanding how imports work, how packages are structured, and how to manage
dependencies with `pip` is fundamental to professional Python development.

---

## 1. What Is a Module?

A **module** is simply a `.py` file. Every Python file you create is already a
module.

```python
# mymath.py — a simple module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

---

## 2. Importing Modules

```python
# Import the whole module
import mymath
print(mymath.add(2, 3))
print(mymath.PI)

# Import specific names
from mymath import add, PI
print(add(2, 3))

# Import everything (generally discouraged)
from mymath import *

# Import with an alias
import mymath as mm
print(mm.multiply(4, 5))

# Alias a specific import
from mymath import multiply as mul
print(mul(4, 5))
```

> ⚠️ Avoid `from module import *` — it pollutes your namespace and makes it
> hard to trace where names come from.

---

## 3. The `__name__` Guard

When a module is run directly, Python sets `__name__` to `"__main__"`. When
it's imported, `__name__` is set to the module's name.

```python
# mymath.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # This block only runs when executed directly:
    #   python mymath.py
    # It does NOT run when imported:
    #   import mymath
    print("Testing add:", add(2, 3))
```

This pattern lets a file work both as a reusable module and as a standalone
script.

---

## 4. Standard Library Highlights

Python ships with an extensive standard library:

| Module | Purpose |
|--------|---------|
| `math` | Mathematical functions (`sqrt`, `sin`, `pi`, …) |
| `random` | Random number generation |
| `datetime` | Dates, times, and time deltas |
| `os` | Operating system interface |
| `sys` | System-specific parameters |
| `json` | JSON encoding/decoding |
| `csv` | CSV file reading/writing |
| `pathlib` | Object-oriented file paths |
| `collections` | Specialized container types |
| `itertools` | Iterator building blocks |
| `functools` | Higher-order functions |
| `re` | Regular expressions |

```python
import math
import random
import datetime

print(math.sqrt(16))                           # 4.0
print(random.randint(1, 100))                  # Random int 1–100
print(datetime.date.today())                   # 2024-01-15
print(datetime.datetime.now().isoformat())     # ISO timestamp
```

---

## 5. Creating Packages

A **package** is a directory containing an `__init__.py` file (which can be
empty). Packages let you group related modules.

```
myproject/
├── __init__.py          # Makes myproject a package
├── utils.py
├── models.py
└── data/
    ├── __init__.py      # Makes data a sub-package
    └── loader.py
```

```python
# Importing from packages
from myproject import utils
from myproject.data import loader
from myproject.models import User
```

### `__init__.py`

```python
# myproject/__init__.py
# Can be empty, or define what is exported:
from .utils import helper_function
from .models import User

__all__ = ["helper_function", "User"]   # Controls `from myproject import *`
```

---

## 6. Relative vs Absolute Imports

```python
# Absolute import (recommended)
from myproject.utils import helper_function

# Relative import (within the same package)
from .utils import helper_function      # Same package
from ..data import loader               # Parent package's sibling
```

> 💡 Use absolute imports in most cases. Relative imports are useful inside
> large packages to avoid long import paths.

---

## 7. `sys.path` — How Python Finds Modules

Python searches for modules in this order:
1. The directory of the running script
2. Directories in `PYTHONPATH` environment variable
3. Standard library directories
4. `site-packages` (where pip installs packages)

```python
import sys
for p in sys.path:
    print(p)
```

---

## 8. `pip` — The Package Manager

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install from requirements.txt
pip install -r requirements.txt

# List installed packages
pip list

# Show package info
pip show requests

# Freeze current packages
pip freeze > requirements.txt

# Uninstall
pip uninstall requests
```

---

## 9. Virtual Environments

Virtual environments isolate project dependencies from system-wide packages.

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
source myenv/bin/activate      # macOS/Linux
myenv\Scripts\activate         # Windows

# Now pip installs into this env
pip install pandas numpy

# Deactivate
deactivate
```

> 💡 **Always** use a virtual environment for every project. This prevents
> version conflicts between projects.

---

## 10. `requirements.txt`

List your project's dependencies so others can reproduce the environment:

```
# requirements.txt
requests==2.31.0
pandas>=2.0,<3.0
numpy~=1.24
python-dotenv
```

```bash
pip install -r requirements.txt
```

---

## Key Takeaways
- A module is a `.py` file; a package is a directory with `__init__.py`.
- Use `import`, `from...import`, and aliases to bring names into scope.
- The `if __name__ == "__main__":` guard separates script logic from reusable code.
- The standard library is vast — learn it before reaching for third-party packages.
- Use `pip` and `requirements.txt` to manage third-party dependencies.
- Always develop inside a virtual environment.

---

## Further Reading
- [Python Docs — Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Docs — The Import System](https://docs.python.org/3/reference/import.html)
- [Python Docs — venv](https://docs.python.org/3/library/venv.html)
- [Real Python — Modules and Packages](https://realpython.com/python-modules-packages/)
- [pip Documentation](https://pip.pypa.io/en/stable/)
