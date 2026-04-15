"""
Day 19: Testing & Debugging (Exercises)
Complete each exercise by replacing `pass` with your implementation.

Each exercise asks you to write tests for given code. The code under test
is provided — your job is to write thorough test cases.
"""

import unittest
from unittest.mock import Mock, patch


# === Code Under Test (DO NOT MODIFY) ===

class Calculator:
    """A calculator with history tracking."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(("add", a, b, result))
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(("subtract", a, b, result))
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(("multiply", a, b, result))
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(("divide", a, b, result))
        return result

    def clear_history(self):
        self.history = []

    def last_result(self):
        if not self.history:
            return None
        return self.history[-1][3]


class StringUtils:
    """String utility functions."""

    @staticmethod
    def reverse(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def word_count(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        return len(s.split()) if s.strip() else 0

    @staticmethod
    def truncate(s, max_length, suffix="..."):
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        if max_length < len(suffix):
            raise ValueError("max_length must be >= suffix length")
        if len(s) <= max_length:
            return s
        return s[:max_length - len(suffix)] + suffix


def fetch_weather(api_client, city):
    """Fetch weather data from an external API."""
    response = api_client.get(f"/weather?city={city}")
    if response.status_code != 200:
        raise ConnectionError(f"API error: {response.status_code}")
    data = response.json()
    return {
        "city": city,
        "temperature": data["temp"],
        "description": data["description"],
    }


# === Exercise 1: Test the Calculator ===
# Write a TestCase class with at least 8 tests covering:
# - Basic operations (add, subtract, multiply, divide)
# - Edge cases (negative numbers, zero, floats)
# - Division by zero exception
# - History tracking
# - last_result method
# - clear_history method

class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        pass

    def test_subtract(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass

    def test_divide_by_zero(self):
        pass

    def test_history_tracking(self):
        pass

    def test_last_result(self):
        pass

    def test_clear_history(self):
        pass


# === Exercise 2: Test StringUtils ===
# Write tests for the StringUtils class covering:
# - reverse: normal strings, empty string, palindromes
# - is_palindrome: various cases including spaces and punctuation
# - word_count: normal text, empty string, multiple spaces
# - truncate: short string, long string, edge cases
# - Type errors for non-string inputs

class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        pass

    def test_reverse_empty(self):
        pass

    def test_reverse_type_error(self):
        pass

    def test_is_palindrome(self):
        pass

    def test_is_palindrome_with_spaces(self):
        pass

    def test_word_count(self):
        pass

    def test_word_count_empty(self):
        pass

    def test_truncate_short(self):
        pass

    def test_truncate_long(self):
        pass

    def test_truncate_invalid_length(self):
        pass


# === Exercise 3: Parameterized Tests ===
# Write a test that checks multiple inputs for Calculator.add
# using subTest (unittest's built-in parameterization).
# Test at least 6 cases including: positives, negatives, zero, floats.

class TestCalculatorParameterized(unittest.TestCase):
    def test_add_cases(self):
        pass


# === Exercise 4: Mock External API ===
# Write tests for fetch_weather() using Mock objects.
# Test:
# - Successful API response (200)
# - API error response (500) — should raise ConnectionError
# - Verify the API was called with correct URL
# - Verify the returned data structure

class TestFetchWeather(unittest.TestCase):
    def test_successful_fetch(self):
        pass

    def test_api_error(self):
        pass

    def test_correct_url_called(self):
        pass

    def test_response_structure(self):
        pass


# === Exercise 5: Test Exception Handling ===
# Write comprehensive exception tests for Calculator and StringUtils:
# - Test that specific exceptions are raised
# - Test that exception messages are correct
# - Test that exceptions contain expected information
# - Use both assertRaises and assertRaisesRegex

class TestExceptions(unittest.TestCase):
    def test_divide_zero_raises_value_error(self):
        pass

    def test_divide_zero_message(self):
        pass

    def test_reverse_type_error(self):
        pass

    def test_truncate_value_error(self):
        pass

    def test_word_count_type_error(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
