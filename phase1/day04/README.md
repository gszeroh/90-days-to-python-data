# Day 04: Operators & Expressions

## Overview
Operators are symbols that perform operations on values and variables. Understanding
operators and their precedence is essential for writing correct expressions in Python.

---

## 1. Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | Division (true) | `7 / 3` | `2.3333...` |
| `//` | Floor division | `7 // 3` | `2` |
| `%` | Modulo (remainder) | `7 % 3` | `1` |
| `**` | Exponentiation | `2 ** 10` | `1024` |

### Notes
- `/` always returns a `float`, even when dividing evenly: `6 / 3` → `2.0`.
- `//` returns the floor of the division (rounds toward negative infinity).
- `%` is useful for checking divisibility: `n % 2 == 0` means `n` is even.
- `**` has higher precedence than unary `-`: `-2 ** 2` = `-(2**2)` = `-4`.

---

## 2. Comparison Operators

Comparison operators return `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<`  | Less than | `3 < 5` | `True` |
| `>`  | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `3 <= 3` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |

### Chained Comparisons
Python supports chained comparisons — a unique and readable feature:
```python
1 < x < 10       # True if x is between 1 and 10 (exclusive)
0 <= score <= 100 # True if score is in [0, 100]
```

---

## 3. Logical Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and False` | `False` |
| `or` | At least one True | `True or False` | `True` |
| `not` | Negation | `not True` | `False` |

### Truth Tables

#### `and`
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

#### `or`
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

#### `not`
| A | not A |
|---|-------|
| True | False |
| False | True |

### Short-Circuit Evaluation
- `and` stops at the first falsy value and returns it.
- `or` stops at the first truthy value and returns it.

```python
0 and "hello"    # 0       (first falsy)
"" or "default"  # "default" (first truthy)
```

---

## 4. Assignment Operators

| Operator | Equivalent | Example |
|----------|-----------|---------|
| `=` | — | `x = 5` |
| `+=` | `x = x + n` | `x += 3` |
| `-=` | `x = x - n` | `x -= 2` |
| `*=` | `x = x * n` | `x *= 4` |
| `/=` | `x = x / n` | `x /= 2` |
| `//=` | `x = x // n` | `x //= 3` |
| `%=` | `x = x % n` | `x %= 2` |
| `**=` | `x = x ** n` | `x **= 2` |

---

## 5. Identity & Membership Operators

### Identity: `is` / `is not`
Check if two variables reference the **same object** in memory.
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b     # True  — same object
a is c     # False — equal but different objects
a == c     # True  — equal values
```

### Membership: `in` / `not in`
Check if a value exists in a sequence.
```python
"a" in "apple"        # True
5 in [1, 2, 3, 4, 5]  # True
"x" not in "hello"    # True
```

---

## 6. Bitwise Operators

These operate on integers at the binary level.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

```
  5 in binary:  101
  3 in binary:  011
  5 & 3:        001 = 1
  5 | 3:        111 = 7
  5 ^ 3:        110 = 6
```

---

## 7. Operator Precedence (Highest to Lowest)

| Precedence | Operator(s) |
|------------|-------------|
| 1 (highest) | `()` Parentheses |
| 2 | `**` Exponentiation |
| 3 | `+x`, `-x`, `~x` Unary |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `\|` |
| 10 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `in` |
| 11 | `not` |
| 12 | `and` |
| 13 (lowest) | `or` |

**When in doubt, use parentheses** to make your intent explicit.

---

## Key Takeaways
- `/` always yields a float; use `//` for integer division.
- Chained comparisons like `1 < x < 10` are Pythonic and readable.
- Logical operators short-circuit — this enables patterns like `value or default`.
- `is` checks identity (same object), `==` checks equality (same value).
- Use parentheses to clarify precedence.

---

## Further Reading
- [Python Docs — Expressions](https://docs.python.org/3/reference/expressions.html)
- [Real Python — Operators](https://realpython.com/python-operators-expressions/)
