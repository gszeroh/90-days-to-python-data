"""
Day 04: Operators & Expressions — Examples
"""

# === Arithmetic Operators ===

a, b = 17, 5

print(f"{a} + {b}  = {a + b}")     # 22
print(f"{a} - {b}  = {a - b}")     # 12
print(f"{a} * {b}  = {a * b}")     # 85
print(f"{a} / {b}  = {a / b}")     # 3.4
print(f"{a} // {b} = {a // b}")    # 3
print(f"{a} % {b}  = {a % b}")     # 2
print(f"{a} ** {b} = {a ** b}")    # 1419857

# Division always returns float
print(f"6 / 3 = {6 / 3}")         # 2.0

# Floor division rounds toward negative infinity
print(f"-7 // 2 = {-7 // 2}")     # -4

# Exponentiation precedence
print(f"-2 ** 2 = {-2 ** 2}")     # -4  (not 4!)

# === Comparison Operators ===

x, y = 10, 20

print(f"{x} == {y}: {x == y}")    # False
print(f"{x} != {y}: {x != y}")    # True
print(f"{x} <  {y}: {x < y}")     # True
print(f"{x} >  {y}: {x > y}")     # False
print(f"{x} <= {y}: {x <= y}")    # True
print(f"{x} >= {y}: {x >= y}")    # False

# Chained comparisons
score = 85
print(f"0 <= {score} <= 100: {0 <= score <= 100}")     # True
print(f"1 < 5 < 10:         {1 < 5 < 10}")             # True

# === Logical Operators ===

print(f"True and True:   {True and True}")     # True
print(f"True and False:  {True and False}")    # False
print(f"False or True:   {False or True}")     # True
print(f"False or False:  {False or False}")    # False
print(f"not True:        {not True}")          # False
print(f"not False:       {not False}")         # True

# Short-circuit evaluation
print(f"0 and 'hello':       {0 and 'hello'}")         # 0
print(f"'hi' and 'hello':    {'hi' and 'hello'}")      # hello
print(f"'' or 'default':     {'' or 'default'}")       # default
print(f"'value' or 'default':{' value' or 'default'}") # value

# Practical example: default values
user_name = ""
display_name = user_name or "Anonymous"
print(f"Display name: {display_name}")

# === Assignment Operators ===

x = 10
print(f"x = {x}")

x += 5
print(f"x += 5 → {x}")    # 15

x -= 3
print(f"x -= 3 → {x}")    # 12

x *= 2
print(f"x *= 2 → {x}")    # 24

x /= 4
print(f"x /= 4 → {x}")    # 6.0

x //= 2
print(f"x //= 2 → {x}")   # 3.0

x **= 3
print(f"x **= 3 → {x}")   # 27.0

x %= 5
print(f"x %= 5 → {x}")    # 2.0

# === Identity Operators ===

a = [1, 2, 3]
b = a              # b references the same object as a
c = [1, 2, 3]      # c is a different object with same content

print(f"a is b:     {a is b}")       # True
print(f"a is c:     {a is c}")       # False
print(f"a == c:     {a == c}")       # True
print(f"a is not c: {a is not c}")   # True

# None should always be compared with `is`
result = None
print(f"result is None: {result is None}")   # True

# === Membership Operators ===

fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits:     {'banana' in fruits}")         # True
print(f"'grape' not in fruits:  {'grape' not in fruits}")      # True
print(f"'a' in 'apple':         {'a' in 'apple'}")            # True

# === Bitwise Operators ===

x, y = 5, 3  # binary: 101, 011

print(f"{x} & {y}  = {x & y}")     # 1   (001)
print(f"{x} | {y}  = {x | y}")     # 7   (111)
print(f"{x} ^ {y}  = {x ^ y}")     # 6   (110)
print(f"~{x}       = {~x}")         # -6
print(f"{x} << 1   = {x << 1}")    # 10  (1010)
print(f"{x} >> 1   = {x >> 1}")    # 2   (10)

# Binary representation
print(f"bin(5) = {bin(5)}")   # 0b101
print(f"bin(3) = {bin(3)}")   # 0b11
print(f"bin(7) = {bin(7)}")   # 0b111

# === Operator Precedence ===

# Without parentheses — follows precedence rules
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")      # 14 (not 20)

# With parentheses — explicit control
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")    # 20

# Mixed precedence
result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}")    # 512 (right-associative: 2 ** 9)

# Logical precedence
result = True or False and False
print(f"True or False and False = {result}")   # True (and binds tighter)
