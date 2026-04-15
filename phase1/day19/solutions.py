"""
Day 19: Testing & Debugging (Solutions)
"""

import unittest
from unittest.mock import Mock, patch


# === Code Under Test (copied from exercises.py) ===

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

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333, places=3)
        self.assertEqual(self.calc.divide(-6, 2), -3.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))

    def test_history_tracking(self):
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        self.assertEqual(len(self.calc.history), 2)
        self.assertEqual(self.calc.history[0], ("add", 1, 2, 3))
        self.assertEqual(self.calc.history[1], ("multiply", 3, 4, 12))

    def test_last_result(self):
        self.assertIsNone(self.calc.last_result())
        self.calc.add(5, 3)
        self.assertEqual(self.calc.last_result(), 8)
        self.calc.multiply(2, 4)
        self.assertEqual(self.calc.last_result(), 8)

    def test_clear_history(self):
        self.calc.add(1, 1)
        self.calc.subtract(5, 3)
        self.assertEqual(len(self.calc.history), 2)
        self.calc.clear_history()
        self.assertEqual(len(self.calc.history), 0)
        self.assertIsNone(self.calc.last_result())


# === Exercise 2: Test StringUtils ===

class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(StringUtils.reverse("hello"), "olleh")
        self.assertEqual(StringUtils.reverse("abc"), "cba")
        self.assertEqual(StringUtils.reverse("a"), "a")

    def test_reverse_empty(self):
        self.assertEqual(StringUtils.reverse(""), "")

    def test_reverse_type_error(self):
        with self.assertRaises(TypeError):
            StringUtils.reverse(123)
        with self.assertRaises(TypeError):
            StringUtils.reverse(None)

    def test_is_palindrome(self):
        self.assertTrue(StringUtils.is_palindrome("racecar"))
        self.assertTrue(StringUtils.is_palindrome("madam"))
        self.assertFalse(StringUtils.is_palindrome("hello"))
        self.assertTrue(StringUtils.is_palindrome(""))

    def test_is_palindrome_with_spaces(self):
        self.assertTrue(StringUtils.is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(StringUtils.is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(StringUtils.is_palindrome("No 'x' in Nixon"))

    def test_word_count(self):
        self.assertEqual(StringUtils.word_count("hello world"), 2)
        self.assertEqual(StringUtils.word_count("one"), 1)
        self.assertEqual(StringUtils.word_count("  multiple   spaces  here  "), 3)

    def test_word_count_empty(self):
        self.assertEqual(StringUtils.word_count(""), 0)
        self.assertEqual(StringUtils.word_count("   "), 0)

    def test_truncate_short(self):
        self.assertEqual(StringUtils.truncate("hi", 10), "hi")
        self.assertEqual(StringUtils.truncate("exact", 5), "exact")

    def test_truncate_long(self):
        self.assertEqual(StringUtils.truncate("Hello, World!", 8), "Hello...")
        self.assertEqual(
            StringUtils.truncate("abcdefgh", 6, suffix=".."),
            "abcd.."
        )

    def test_truncate_invalid_length(self):
        with self.assertRaises(ValueError):
            StringUtils.truncate("hello", 2, suffix="...")


# === Exercise 3: Parameterized Tests ===

class TestCalculatorParameterized(unittest.TestCase):
    def test_add_cases(self):
        calc = Calculator()
        cases = [
            (1, 1, 2, "positive + positive"),
            (-1, -1, -2, "negative + negative"),
            (-1, 1, 0, "negative + positive"),
            (0, 0, 0, "zero + zero"),
            (0.1, 0.2, 0.3, "float + float"),
            (1000000, 2000000, 3000000, "large numbers"),
        ]
        for a, b, expected, desc in cases:
            with self.subTest(case=desc, a=a, b=b):
                result = calc.add(a, b)
                self.assertAlmostEqual(result, expected, places=7,
                                       msg=f"Failed: {desc}")


# === Exercise 4: Mock External API ===

class TestFetchWeather(unittest.TestCase):
    def _create_mock_api(self, status_code=200, json_data=None):
        """Helper to create a configured mock API client."""
        mock_api = Mock()
        mock_api.get.return_value.status_code = status_code
        if json_data:
            mock_api.get.return_value.json.return_value = json_data
        return mock_api

    def test_successful_fetch(self):
        mock_api = self._create_mock_api(200, {
            "temp": 72,
            "description": "Sunny",
        })
        result = fetch_weather(mock_api, "Seattle")
        self.assertEqual(result["city"], "Seattle")
        self.assertEqual(result["temperature"], 72)
        self.assertEqual(result["description"], "Sunny")

    def test_api_error(self):
        mock_api = self._create_mock_api(500)
        with self.assertRaises(ConnectionError) as ctx:
            fetch_weather(mock_api, "Seattle")
        self.assertIn("500", str(ctx.exception))

    def test_correct_url_called(self):
        mock_api = self._create_mock_api(200, {
            "temp": 65,
            "description": "Cloudy",
        })
        fetch_weather(mock_api, "Portland")
        mock_api.get.assert_called_once_with("/weather?city=Portland")

    def test_response_structure(self):
        mock_api = self._create_mock_api(200, {
            "temp": 80,
            "description": "Hot",
        })
        result = fetch_weather(mock_api, "Phoenix")
        self.assertIn("city", result)
        self.assertIn("temperature", result)
        self.assertIn("description", result)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result["temperature"], (int, float))
        self.assertIsInstance(result["description"], str)


# === Exercise 5: Test Exception Handling ===

class TestExceptions(unittest.TestCase):
    def test_divide_zero_raises_value_error(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_divide_zero_message(self):
        calc = Calculator()
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calc.divide(10, 0)

    def test_reverse_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            StringUtils.reverse(42)
        self.assertEqual(str(ctx.exception), "Input must be a string")

    def test_truncate_value_error(self):
        with self.assertRaisesRegex(ValueError, "max_length must be"):
            StringUtils.truncate("hello", 1, suffix="...")

    def test_word_count_type_error(self):
        with self.assertRaises(TypeError):
            StringUtils.word_count(123)
        with self.assertRaises(TypeError):
            StringUtils.word_count(["hello", "world"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
