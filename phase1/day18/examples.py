"""
Day 18: Regular Expressions (Examples)
Topics: re module, patterns, groups, lookahead/lookbehind, flags
"""

import re


# === Basic Pattern Matching ===

print("=== Basic Pattern Matching ===")
text = "The price is $42.99 and the tax is $3.50"

# search: find first match
match = re.search(r'\$[\d.]+', text)
print(f"search: {match.group()}")

# match: only at beginning
print(f"match 'The': {re.match(r'The', text) is not None}")
print(f"match 'price': {re.match(r'price', text) is not None}")

# fullmatch: entire string
print(f"fullmatch: {re.fullmatch(r'\d+', '12345') is not None}")
print(f"fullmatch: {re.fullmatch(r'\d+', '123abc') is not None}")

# findall: all non-overlapping matches
prices = re.findall(r'\$[\d.]+', text)
print(f"findall: {prices}")

# finditer: iterator of match objects
print("finditer:")
for m in re.finditer(r'\$(?P<amount>[\d.]+)', text):
    print(f"  Found ${m.group('amount')} at position {m.start()}-{m.end()}")


# === Character Classes & Quantifiers ===

print("\n=== Character Classes & Quantifiers ===")
sample = "abc 123 def456 GHI_789 $pecial!"

print(f"Digits (\\d+):    {re.findall(r'\\d+', sample)}")
print(f"Words (\\w+):     {re.findall(r'\\w+', sample)}")
print(f"Non-words (\\W+): {re.findall(r'\\W+', sample)}")
print(f"Spaces (\\s+):    {re.findall(r'\\s+', sample)}")

# Specific character classes
print(f"Lowercase: {re.findall(r'[a-z]+', sample)}")
print(f"Uppercase: {re.findall(r'[A-Z]+', sample)}")
print(f"Not digits: {re.findall(r'[^0-9 ]+', sample)}")


# === Greedy vs Lazy Matching ===

print("\n=== Greedy vs Lazy Matching ===")
html = "<b>bold</b> and <i>italic</i>"
print(f"Greedy:  {re.findall(r'<.*>', html)}")
print(f"Lazy:    {re.findall(r'<.*?>', html)}")


# === Anchors and Word Boundaries ===

print("\n=== Anchors and Word Boundaries ===")
lines = "cat\ncatalog\nthe cat sat\nscatter"
print(f"^cat (MULTILINE): {re.findall(r'^cat', lines, re.MULTILINE)}")
print(f"\\bcat\\b:          {re.findall(r'\\bcat\\b', lines)}")
print(f"cat$:             {re.findall(r'cat$', lines, re.MULTILINE)}")


# === Groups ===

print("\n=== Groups ===")
date_str = "Meeting on 2024-01-15 and 2024-03-20"
pattern = r'(\d{4})-(\d{2})-(\d{2})'

# findall with groups returns tuples
dates = re.findall(pattern, date_str)
print(f"Date tuples: {dates}")

# Access groups from a match object
match = re.search(pattern, date_str)
print(f"Full match: {match.group()}")
print(f"Year:       {match.group(1)}")
print(f"Month:      {match.group(2)}")
print(f"Day:        {match.group(3)}")
print(f"All groups: {match.groups()}")


# === Named Groups ===

print("\n=== Named Groups ===")
log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] "(?P<method>\w+) (?P<path>[^"]+)"'
log_line = '192.168.1.1 - [2024-01-15] "GET /api/users"'

match = re.search(log_pattern, log_line)
if match:
    print(f"IP:     {match.group('ip')}")
    print(f"Date:   {match.group('date')}")
    print(f"Method: {match.group('method')}")
    print(f"Path:   {match.group('path')}")
    print(f"Dict:   {match.groupdict()}")


# === re.sub — Search and Replace ===

print("\n=== re.sub ===")
# Simple replacement
text = "Call 555-1234 or 555-5678"
censored = re.sub(r'\d', 'X', text)
print(f"Censor digits: {censored}")

# Backreferences
name = "John Smith"
swapped = re.sub(r'(\w+) (\w+)', r'\2, \1', name)
print(f"Swap name: {swapped}")

# Function-based replacement
def double_numbers(match):
    return str(int(match.group()) * 2)

result = re.sub(r'\d+', double_numbers, "I have 3 cats and 5 dogs")
print(f"Doubled: {result}")

# Clean whitespace
messy = "  too   many    spaces   here  "
clean = re.sub(r'\s+', ' ', messy).strip()
print(f"Cleaned: '{clean}'")


# === re.split ===

print("\n=== re.split ===")
text = "one,two;three four\tfive"
parts = re.split(r'[,;\s]+', text)
print(f"Split: {parts}")

# Split with capturing group keeps delimiters
parts = re.split(r'([,;])', "a,b;c,d")
print(f"Split w/ delimiters: {parts}")


# === Compiled Patterns ===

print("\n=== Compiled Patterns ===")
email_re = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)
test_emails = [
    "user@example.com",
    "first.last@domain.org",
    "invalid@",
    "@nodomain.com",
    "spaces in@email.com",
    "valid+tag@sub.domain.co.uk",
]
for email in test_emails:
    status = "VALID" if email_re.match(email) else "INVALID"
    print(f"  {status:>7}: {email}")


# === Lookahead and Lookbehind ===

print("\n=== Lookahead and Lookbehind ===")
text = "12px 14em 16px 20% 24pt"

# Positive lookahead: digits followed by "px"
print(f"Before px: {re.findall(r'\\d+(?=px)', text)}")

# Negative lookahead: digits NOT followed by "px"
print(f"Not before px: {re.findall(r'\\d+(?!px)(?!\\d)', text)}")

# Positive lookbehind: match after $
prices = "Items: $10 $20 €30 $40"
print(f"After $: {re.findall(r'(?<=\\$)\\d+', prices)}")

# Negative lookbehind: word not preceded by "un"
words = "happy unhappy lucky unlucky kind unkind"
print(f"Not un-prefixed: {re.findall(r'(?<!un)(?<=\\b)[a-z]+', words)}")

# Password validation with lookaheads
password_re = re.compile(r"""
    ^
    (?=.*[A-Z])        # at least one uppercase
    (?=.*[a-z])        # at least one lowercase
    (?=.*\d)           # at least one digit
    (?=.*[!@\#$%^&*])  # at least one special char
    .{8,}              # at least 8 characters
    $
""", re.VERBOSE)
passwords = ["Weak", "StronG1!", "NoSpecial1", "sh0rt!", "G00d@Pass"]
for pwd in passwords:
    status = "PASS" if password_re.match(pwd) else "FAIL"
    print(f"  {status}: {pwd}")


# === Flags ===

print("\n=== Flags ===")
# IGNORECASE
print(f"Case-insensitive: {re.findall(r'python', 'Python PYTHON python', re.I)}")

# MULTILINE
multiline_text = """First line
Second line
Third line"""
print(f"Line starts: {re.findall(r'^\\w+', multiline_text, re.MULTILINE)}")

# DOTALL
html_block = "<div>\n  content\n</div>"
print(f"Without DOTALL: {re.findall(r'<div>.*</div>', html_block)}")
print(f"With DOTALL:    {re.findall(r'<div>.*</div>', html_block, re.DOTALL)}")

# VERBOSE for readable patterns
url_pattern = re.compile(r"""
    (?P<protocol>https?)    # http or https
    ://                     # literal ://
    (?P<domain>[^/\s]+)     # domain (no slashes or spaces)
    (?P<path>/[^\s]*)?      # optional path
""", re.VERBOSE)

urls = [
    "https://example.com/path/to/page",
    "http://api.service.io",
    "https://docs.python.org/3/library/re.html",
]
for url in urls:
    m = url_pattern.search(url)
    if m:
        print(f"  {m.group('protocol')}:// {m.group('domain')} -> {m.group('path') or '/'}")


# === Common Real-World Patterns ===

print("\n=== Common Real-World Patterns ===")
mixed_text = """
Contact us at support@company.com or sales@company.org.
Call (555) 123-4567 or 555.987.6543.
Visit https://www.example.com/page or http://api.test.io/v2.
Meeting dates: 2024-01-15, 2024-03-20, 2024-12-01.
Colors: #FF5733, #00AA11, #abc.
IPs: 192.168.1.1, 10.0.0.255.
"""

patterns = {
    "Emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "Phones": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "URLs": r'https?://[^\s,]+',
    "Dates": r'\d{4}-\d{2}-\d{2}',
    "Hex colors": r'#[0-9a-fA-F]{6}\b',
    "IPv4": r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
}
for name, pattern in patterns.items():
    matches = re.findall(pattern, mixed_text)
    print(f"  {name}: {matches}")
