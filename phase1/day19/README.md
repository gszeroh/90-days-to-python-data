# Day 19: Testing & Debugging

## Overview

Writing tests is one of the most important skills for producing reliable software.
Testing ensures your code works correctly, prevents regressions when you make
changes, and serves as living documentation. Python offers excellent testing tools
— from the built-in `unittest` to the popular `pytest` framework.

---

## 1. Why Test?

- **Catch bugs early** — before they reach production.
- **Enable refactoring** — change code confidently knowing tests will catch
  breakage.
- **Document behavior** — tests show how code is meant to be used.
- **Design feedback** — hard-to-test code often indicates design problems.

---

## 2. `unittest` — The Standard Library

Python's built-in `unittest` module follows the xUnit pattern:

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        """Called before each test method."""
        self.data = [1, 2, 3, 4, 5]

    def tearDown(self):
        """Called after each test method."""
        self.data = None

    def test_sum(self):
        self.assertEqual(sum(self.data), 15)

    def test_max(self):
        self.assertEqual(max(self.data), 5)

    def test_min(self):
        self.assertEqual(min(self.data), 1)

if __name__ == '__main__':
    unittest.main()
```

### Common Assertions

| Method                        | Checks                     |
|-------------------------------|----------------------------|
| `assertEqual(a, b)`          | `a == b`                   |
| `assertNotEqual(a, b)`       | `a != b`                   |
| `assertTrue(x)`              | `bool(x) is True`          |
| `assertFalse(x)`             | `bool(x) is False`         |
| `assertIs(a, b)`             | `a is b`                   |
| `assertIsNone(x)`            | `x is None`                |
| `assertIn(a, b)`             | `a in b`                   |
| `assertIsInstance(a, b)`     | `isinstance(a, b)`         |
| `assertRaises(exc)`          | Exception is raised        |
| `assertAlmostEqual(a, b)`    | `round(a-b, 7) == 0`      |

---

## 3. `pytest` — The Modern Standard

`pytest` is simpler, more powerful, and the de facto standard in the Python
community.

```python
# test_math.py
def test_sum():
    assert sum([1, 2, 3]) == 6

def test_max():
    assert max([1, 2, 3]) == 3
```

### Key Advantages Over `unittest`

- **Plain `assert`** — no need to learn special assertion methods.
- **Better output** — detailed failure diffs.
- **Fixtures** — powerful dependency injection via `@pytest.fixture`.
- **Parametrize** — run the same test with different inputs.
- **Plugins** — rich ecosystem (pytest-cov, pytest-mock, pytest-xdist).

### Running Tests

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Run specific file
pytest test_math.py

# Run specific test
pytest test_math.py::test_sum

# Stop on first failure
pytest -x

# Show print output
pytest -s
```

---

## 4. Test Organization

### Naming Conventions

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*` (no `__init__`)

### Project Structure

```
project/
├── src/
│   ├── calculator.py
│   └── utils.py
└── tests/
    ├── __init__.py
    ├── test_calculator.py
    └── test_utils.py
```

### Test Structure: Arrange-Act-Assert (AAA)

```python
def test_discount():
    # Arrange
    price = 100.0
    discount = 0.2

    # Act
    result = apply_discount(price, discount)

    # Assert
    assert result == 80.0
```

---

## 5. Fixtures

Fixtures provide reusable setup/teardown logic:

```python
import pytest

@pytest.fixture
def sample_list():
    """Provides a fresh list for each test."""
    return [3, 1, 4, 1, 5, 9, 2, 6]

@pytest.fixture
def database():
    """Setup and teardown a database connection."""
    db = connect_to_db()
    yield db          # test runs here
    db.disconnect()   # teardown

def test_sort(sample_list):
    sample_list.sort()
    assert sample_list == [1, 1, 2, 3, 4, 5, 6, 9]

def test_length(sample_list):
    assert len(sample_list) == 8
```

### Fixture Scopes

| Scope       | Lifetime                    |
|-------------|-----------------------------|
| `function`  | Each test (default)         |
| `class`     | Each test class             |
| `module`    | Each test module            |
| `session`   | Entire test session         |

---

## 6. Parameterized Tests

```python
import pytest

@pytest.mark.parametrize("input_val, expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (-1, 1),
])
def test_square(input_val, expected):
    assert input_val ** 2 == expected
```

---

## 7. Testing Exceptions

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

---

## 8. Mocking with `unittest.mock`

Mocking replaces real objects with controlled substitutes during testing:

```python
from unittest.mock import Mock, patch, MagicMock

# Create a mock object
mock_api = Mock()
mock_api.get_user.return_value = {"name": "Alice", "age": 30}

# Use the mock
result = mock_api.get_user(1)
assert result["name"] == "Alice"
mock_api.get_user.assert_called_once_with(1)
```

### `@patch` Decorator

```python
from unittest.mock import patch

# Replace a module-level function during a test
@patch('mymodule.requests.get')
def test_fetch_data(mock_get):
    mock_get.return_value.json.return_value = {"status": "ok"}
    result = fetch_data("https://api.example.com")
    assert result == {"status": "ok"}
    mock_get.assert_called_once()
```

### When to Mock

- External APIs and network calls
- Database operations
- File system operations
- Time-dependent code
- Third-party services

---

## 9. Debugging

### `breakpoint()` (Python 3.7+)

```python
def buggy_function(data):
    result = []
    for item in data:
        breakpoint()  # drops into pdb here
        result.append(item * 2)
    return result
```

### Common `pdb` Commands

| Command      | Action                                |
|--------------|---------------------------------------|
| `n` (next)   | Execute next line                     |
| `s` (step)   | Step into function                    |
| `c` (continue)| Continue to next breakpoint          |
| `p expr`     | Print expression                      |
| `pp expr`    | Pretty-print expression               |
| `l` (list)   | Show source code                      |
| `w` (where)  | Show call stack                       |
| `q` (quit)   | Quit debugger                         |
| `b N`        | Set breakpoint at line N              |
| `h` (help)   | Show help                             |

### Debugging Tips

1. **Print debugging**: Quick but messy — use for simple cases.
2. **`breakpoint()`**: Interactive investigation of state.
3. **Logging**: Better than print — configurable levels and output.
4. **IDE debugger**: Visual breakpoints, watches, and stepping.
5. **`assert` statements**: Catch invalid state early.

---

## 10. Test-Driven Development (TDD)

TDD follows the **Red-Green-Refactor** cycle:

1. **Red**: Write a failing test for the desired behavior.
2. **Green**: Write the minimum code to make the test pass.
3. **Refactor**: Clean up the code while keeping tests green.

```python
# Step 1 (Red): Write the test
def test_fizzbuzz_3():
    assert fizzbuzz(3) == "Fizz"

# Step 2 (Green): Implement
def fizzbuzz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)

# Step 3 (Refactor): Improve
```

---

## 11. Test Coverage

```bash
# Install coverage tool
pip install pytest-cov

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Generate HTML report
pytest --cov=src --cov-report=html
```

Aim for high coverage, but remember: **100% coverage doesn't mean 100% correct**.
Focus on testing behavior, edge cases, and error paths.

---

## Key Takeaways

1. Write tests early and often — they save time in the long run.
2. Use `pytest` for most projects; `unittest` when you need the standard library.
3. Structure tests with Arrange-Act-Assert.
4. Use fixtures for reusable test setup.
5. Mock external dependencies — test your code, not the internet.
6. Use `breakpoint()` for interactive debugging.
7. TDD (Red-Green-Refactor) helps design clean, testable code.

---

## Further Reading

- [pytest documentation](https://docs.pytest.org/)
- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [pdb documentation](https://docs.python.org/3/library/pdb.html)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
