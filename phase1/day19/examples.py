"""
Day 19: Testing & Debugging (Examples)
Topics: unittest, pytest, fixtures, mocking, pdb, TDD
Run this file to see unittest examples. For pytest examples, run:
    pytest examples.py -v
"""

import unittest
from unittest.mock import Mock, patch, MagicMock


# === Sample Code to Test ===

class Calculator:
    """A simple calculator for demonstration."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @property
    def history(self):
        return getattr(self, '_history', [])


def fetch_user_data(api_client, user_id):
    """Function that depends on an external API."""
    response = api_client.get(f"/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None


# === unittest Examples ===

class TestCalculatorUnittest(unittest.TestCase):
    """unittest-style test class."""

    def setUp(self):
        """Create a fresh calculator for each test."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333, places=3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))

    def test_add_floats(self):
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3)


# === pytest-style Tests (Functions) ===

def test_add_pytest():
    """pytest uses plain assert statements."""
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtract_pytest():
    calc = Calculator()
    assert calc.subtract(10, 3) == 7


def test_divide_by_zero_pytest():
    """pytest.raises for exception testing."""
    import pytest
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


# === pytest Fixtures ===

def _make_calculator():
    """Factory function simulating a pytest fixture."""
    return Calculator()


def test_with_factory():
    calc = _make_calculator()
    assert calc.multiply(3, 4) == 12


# === Parameterized Tests (pytest style) ===

# These would use @pytest.mark.parametrize in a real test file:
# @pytest.mark.parametrize("a, b, expected", [
#     (1, 1, 2),
#     (0, 0, 0),
#     (-1, 1, 0),
#     (100, 200, 300),
# ])
# def test_add_parametrize(a, b, expected):
#     calc = Calculator()
#     assert calc.add(a, b) == expected

# Demonstrating the concept with a loop:
def test_add_multiple_cases():
    calc = Calculator()
    cases = [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (0.1, 0.2, 0.3),
    ]
    for a, b, expected in cases:
        result = calc.add(a, b)
        assert abs(result - expected) < 1e-9, f"add({a}, {b}) = {result}, expected {expected}"


# === Mocking Examples ===

class TestMocking(unittest.TestCase):
    """Examples of mocking external dependencies."""

    def test_mock_basic(self):
        """Create a mock object from scratch."""
        mock_api = Mock()
        mock_api.get.return_value.status_code = 200
        mock_api.get.return_value.json.return_value = {
            "id": 1,
            "name": "Alice",
        }

        result = fetch_user_data(mock_api, 1)

        self.assertEqual(result["name"], "Alice")
        mock_api.get.assert_called_once_with("/users/1")

    def test_mock_not_found(self):
        """Mock a 404 response."""
        mock_api = Mock()
        mock_api.get.return_value.status_code = 404

        result = fetch_user_data(mock_api, 999)

        self.assertIsNone(result)

    def test_mock_side_effect(self):
        """Use side_effect for dynamic behavior."""
        mock_api = Mock()
        mock_api.get.side_effect = ConnectionError("Network down")

        with self.assertRaises(ConnectionError):
            fetch_user_data(mock_api, 1)

    def test_mock_call_tracking(self):
        """Mocks track all calls automatically."""
        mock_func = Mock()
        mock_func(1, 2, key="value")
        mock_func(3, 4)

        self.assertEqual(mock_func.call_count, 2)
        mock_func.assert_any_call(1, 2, key="value")
        mock_func.assert_called_with(3, 4)  # last call


class TestMagicMock(unittest.TestCase):
    """MagicMock supports magic methods out of the box."""

    def test_magic_mock_container(self):
        mock_list = MagicMock()
        mock_list.__len__.return_value = 5
        mock_list.__getitem__.return_value = "item"

        self.assertEqual(len(mock_list), 5)
        self.assertEqual(mock_list[0], "item")

    def test_magic_mock_context_manager(self):
        mock_file = MagicMock()
        mock_file.__enter__.return_value.read.return_value = "file contents"

        with mock_file as f:
            data = f.read()

        self.assertEqual(data, "file contents")


# === Debugging Examples ===

def demonstrate_debugging():
    """
    Debugging techniques (not run in tests).

    Using breakpoint():
        def buggy_sort(items):
            for i in range(len(items)):
                breakpoint()  # Pause here to inspect state
                for j in range(i + 1, len(items)):
                    if items[i] > items[j]:
                        items[i], items[j] = items[j], items[i]
            return items

    In the pdb prompt:
        (Pdb) p items       # print the list
        (Pdb) p i, j        # print loop variables
        (Pdb) n             # next line
        (Pdb) c             # continue to next breakpoint
        (Pdb) q             # quit debugger

    Using assert for defensive programming:
        def process_age(age):
            assert isinstance(age, int), f"Expected int, got {type(age)}"
            assert 0 <= age <= 150, f"Invalid age: {age}"
            return age
    """
    print("See docstring for debugging examples.")
    print("Use breakpoint() in your code to drop into pdb.")
    print("Common commands: n(ext), s(tep), c(ontinue), p(rint), q(uit)")


# === TDD Example: FizzBuzz ===

class TestFizzBuzz(unittest.TestCase):
    """TDD example: tests written first, then implementation."""

    def test_regular_number(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")

    def test_divisible_by_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_divisible_by_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_divisible_by_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")


def fizzbuzz(n):
    """Implementation driven by the tests above."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# === Run Examples ===

if __name__ == "__main__":
    print("=== Running unittest Examples ===")
    print("(Use `python -m pytest examples.py -v` for pytest-style output)\n")

    demonstrate_debugging()
    print()

    # Run the unittest tests
    unittest.main(verbosity=2)
