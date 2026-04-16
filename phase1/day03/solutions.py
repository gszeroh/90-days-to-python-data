"""
Day 03: Strings Deep Dive — Solutions
"""


# === Exercise 1: Reverse String ===

def reverse_string(s):
    """Return the reverse of string `s` using slicing.

    Examples:
        reverse_string("hello")  -> "olleh"
        reverse_string("Python") -> "nohtyP"
        reverse_string("")       -> ""
    """
    return s[::-1]


# === Exercise 2: Count Vowels ===

def count_vowels(s):
    """Return the number of vowels (a, e, i, o, u) in `s`.

    The count should be case-insensitive.

    Examples:
        count_vowels("hello")     -> 2
        count_vowels("AEIOU")     -> 5
        count_vowels("rhythm")    -> 0
    """
    return sum(1 for char in s.lower() if char in "aeiou")


# === Exercise 3: Title Case ===

def title_case(s):
    """Convert a string to title case where each word starts with an uppercase
    letter and the remaining letters are lowercase.

    Use the built-in string method.

    Examples:
        title_case("hello world")      -> "Hello World"
        title_case("PYTHON IS FUN")    -> "Python Is Fun"
        title_case("a tale of two cities") -> "A Tale Of Two Cities"
    """
    return s.title()


# === Exercise 4: Initials ===

def extract_initials(full_name):
    """Extract uppercase initials from a full name, separated by dots.

    Examples:
        extract_initials("Alice Bob Carter")  -> "A.B.C"
        extract_initials("John Doe")          -> "J.D"
        extract_initials("Madonna")           -> "M"
    """
    parts = full_name.split()
    return ".".join(part[0].upper() for part in parts)


# === Exercise 5: Mask Email ===

def mask_email(email):
    """Mask an email address by replacing all but the first and last
    characters of the username with asterisks.

    The domain should remain unchanged.

    Examples:
        mask_email("alice@example.com")   -> "a***e@example.com"
        mask_email("bob@test.org")        -> "b*b@test.org"
        mask_email("jo@mail.com")         -> "jo@mail.com"
    """
    username, domain = email.split("@")
    if len(username) <= 2:
        masked = username
    else:
        masked = username[0] + "*" * (len(username) - 2) + username[-1]
    return f"{masked}@{domain}"
