# Day 18: Regular Expressions

## Overview

Regular expressions (regex) are a powerful language for pattern matching and text
manipulation. Python's `re` module provides full regex support. In data science,
regex is essential for cleaning messy text data, extracting structured information
from unstructured text, and validating input formats.

---

## 1. Getting Started with `re`

```python
import re

# Does the pattern exist anywhere in the string?
result = re.search(r'\d+', 'Order #12345')
print(result.group())  # '12345'
```

### Key Functions

| Function              | Purpose                                          |
|-----------------------|--------------------------------------------------|
| `re.search(p, s)`    | Find first match anywhere in string              |
| `re.match(p, s)`     | Match only at the beginning of string            |
| `re.fullmatch(p, s)` | Match the entire string                          |
| `re.findall(p, s)`   | Return all non-overlapping matches as a list     |
| `re.finditer(p, s)`  | Return an iterator of match objects              |
| `re.sub(p, r, s)`    | Replace all matches with replacement             |
| `re.split(p, s)`     | Split string by pattern                          |
| `re.compile(p)`      | Compile pattern for reuse                        |

---

## 2. Pattern Syntax

### Basic Matchers

| Pattern | Matches                                    |
|---------|--------------------------------------------|
| `.`     | Any character except newline               |
| `\d`    | Digit `[0-9]`                              |
| `\D`    | Non-digit `[^0-9]`                         |
| `\w`    | Word character `[a-zA-Z0-9_]`             |
| `\W`    | Non-word character                         |
| `\s`    | Whitespace `[ \t\n\r\f\v]`                |
| `\S`    | Non-whitespace                             |

### Quantifiers

| Pattern  | Meaning                          |
|----------|----------------------------------|
| `*`      | 0 or more (greedy)               |
| `+`      | 1 or more (greedy)               |
| `?`      | 0 or 1 (optional)                |
| `{n}`    | Exactly n                        |
| `{n,m}`  | Between n and m (inclusive)      |
| `{n,}`   | n or more                        |
| `*?`     | 0 or more (lazy/non-greedy)     |
| `+?`     | 1 or more (lazy/non-greedy)     |

### Anchors

| Pattern | Matches                            |
|---------|------------------------------------|
| `^`     | Start of string (or line with `MULTILINE`) |
| `$`     | End of string (or line with `MULTILINE`)   |
| `\b`    | Word boundary                      |
| `\B`    | Non-word boundary                  |

### Character Classes

| Pattern       | Meaning                               |
|---------------|---------------------------------------|
| `[abc]`       | Any one of a, b, c                    |
| `[a-z]`       | Any lowercase letter                  |
| `[^abc]`      | Any character except a, b, c          |
| `[a-zA-Z0-9]` | Alphanumeric                         |

### Alternation and Grouping

| Pattern       | Meaning                               |
|---------------|---------------------------------------|
| `a\|b`        | a or b                                |
| `(abc)`       | Capturing group                       |
| `(?:abc)`     | Non-capturing group                   |
| `(?P<name>x)` | Named capturing group                |

---

## 3. Groups

Groups let you extract parts of a match:

```python
import re

pattern = r'(\d{4})-(\d{2})-(\d{2})'
match = re.search(pattern, 'Date: 2024-01-15')

print(match.group())    # '2024-01-15' (entire match)
print(match.group(1))   # '2024' (first group)
print(match.group(2))   # '01' (second group)
print(match.groups())   # ('2024', '01', '15')
```

### Named Groups

```python
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, '2024-01-15')

print(match.group('year'))   # '2024'
print(match.groupdict())     # {'year': '2024', 'month': '01', 'day': '15'}
```

---

## 4. Lookahead and Lookbehind

These are **zero-width assertions** — they check for a pattern without consuming
characters.

| Pattern      | Name               | Meaning                              |
|--------------|--------------------|--------------------------------------|
| `(?=...)`    | Positive lookahead | Followed by ...                      |
| `(?!...)`    | Negative lookahead | NOT followed by ...                  |
| `(?<=...)`   | Positive lookbehind| Preceded by ...                      |
| `(?<!...)`   | Negative lookbehind| NOT preceded by ...                  |

```python
# Match a number only if followed by "px"
re.findall(r'\d+(?=px)', '12px 14em 16px')  # ['12', '16']

# Match a word not preceded by "Mr. "
re.findall(r'(?<!Mr\. )\b[A-Z][a-z]+', 'Mr. Smith and Alice')  # ['Alice']
```

---

## 5. Flags

| Flag               | Short | Purpose                                    |
|--------------------|-------|--------------------------------------------|
| `re.IGNORECASE`    | `re.I`| Case-insensitive matching                  |
| `re.MULTILINE`     | `re.M`| `^`/`$` match start/end of each line       |
| `re.DOTALL`        | `re.S`| `.` matches newline too                    |
| `re.VERBOSE`       | `re.X`| Allow comments and whitespace in pattern   |

```python
# Verbose mode for readable patterns
pattern = re.compile(r"""
    ^                   # start of string
    (?P<protocol>https?)  # http or https
    ://                 # literal ://
    (?P<domain>[^/]+)   # domain name
    (?P<path>/.*)?      # optional path
    $                   # end of string
""", re.VERBOSE)
```

---

## 6. Compiled Patterns

When reusing a pattern, compile it for better performance:

```python
email_re = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

emails = [
    "user@example.com",
    "invalid@",
    "test@domain.org",
]
for email in emails:
    if email_re.fullmatch(email):
        print(f"Valid:   {email}")
    else:
        print(f"Invalid: {email}")
```

---

## 7. Common Real-World Patterns

| Use Case      | Pattern                                            |
|---------------|----------------------------------------------------|
| Email         | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |
| Phone (US)    | `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}`             |
| Date (ISO)    | `\d{4}-\d{2}-\d{2}`                                |
| IPv4 Address  | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`              |
| URL           | `https?://[^\s]+`                                   |
| Hex Color     | `#[0-9a-fA-F]{6}`                                  |

---

## 8. `re.sub` — Search and Replace

```python
# Replace digits with X
re.sub(r'\d', 'X', 'Call 555-1234')  # 'Call XXX-XXXX'

# Use a function for dynamic replacement
def censor(match):
    return '*' * len(match.group())

re.sub(r'\b\w{4}\b', censor, 'This is a test line')  # '**** is a **** ****'
```

### Backreferences in Replacement

```python
# Swap first and last name
re.sub(r'(\w+) (\w+)', r'\2, \1', 'John Smith')  # 'Smith, John'
```

---

## Key Takeaways

1. Use raw strings (`r'...'`) for regex patterns to avoid backslash issues.
2. `re.search()` finds the first match anywhere; `re.match()` only at the start.
3. Groups `()` let you extract sub-parts of a match.
4. Named groups `(?P<name>...)` make patterns self-documenting.
5. Lookahead/lookbehind assert context without consuming characters.
6. Compile patterns with `re.compile()` when reusing them.
7. Use `re.VERBOSE` for complex patterns to maintain readability.

---

## Further Reading

- [re module documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [regex101.com](https://regex101.com/) — interactive regex tester
