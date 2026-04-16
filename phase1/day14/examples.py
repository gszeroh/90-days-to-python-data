"""
Day 14: OOP Basics — Examples
"""

import datetime
import math

# === Creating a Basic Class ===

print("--- Basic Class ---")

class Dog:
    """A simple Dog class."""

    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, breed, age):
        self.name = name          # Instance attributes
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def description(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"

fido = Dog("Fido", "Labrador", 3)
rex = Dog("Rex", "German Shepherd", 5)

print(f"fido: {fido.description()}")
print(f"rex: {rex.description()}")
print(f"fido.bark(): {fido.bark()}")
print(f"species: {fido.species}")
print(f"Same species object: {fido.species is rex.species}")

# === Instance vs Class Attributes ===

print("\n--- Instance vs Class Attributes ---")

class Counter:
    """Demonstrates class vs instance attributes."""

    total_count = 0  # Class attribute — shared

    def __init__(self, name):
        self.name = name
        self.count = 0  # Instance attribute — per object

    def increment(self):
        self.count += 1
        Counter.total_count += 1

a = Counter("A")
b = Counter("B")

a.increment()
a.increment()
b.increment()

print(f"a.count = {a.count}")          # 2
print(f"b.count = {b.count}")          # 1
print(f"Counter.total_count = {Counter.total_count}")  # 3

# === __str__ and __repr__ ===

print("\n--- __str__ and __repr__ ---")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"

p = Point(3, 4)
print(f"str(p):  {p}")           # (3, 4)
print(f"repr(p): {repr(p)}")     # Point(x=3, y=4)
print(f"f-string: {p}")          # Uses __str__
print(f"In a list: {[p]}")       # Uses __repr__

# === Class Methods ===

print("\n--- @classmethod ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor using birth year."""
        age = datetime.date.today().year - birth_year
        return cls(name, age)

    @classmethod
    def from_dict(cls, data):
        """Alternative constructor from a dictionary."""
        return cls(data["name"], data["age"])

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

alice = Person("Alice", 30)
bob = Person.from_birth_year("Bob", 1995)
charlie = Person.from_dict({"name": "Charlie", "age": 28})

print(f"alice:   {alice}")
print(f"bob:     {bob}")
print(f"charlie: {charlie}")

# === Static Methods ===

print("\n--- @staticmethod ---")

class MathUtils:
    """A collection of math utility functions."""

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("n must be non-negative")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(f"is_even(4): {MathUtils.is_even(4)}")
print(f"is_prime(17): {MathUtils.is_prime(17)}")
print(f"factorial(5): {MathUtils.factorial(5)}")

# Can also call on an instance (less common)
utils = MathUtils()
print(f"Instance call: {utils.is_prime(7)}")

# === Properties ===

print("\n--- @property ---")

class Circle:
    def __init__(self, radius):
        self._radius = radius  # "Private" by convention

    @property
    def radius(self):
        """Get the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self._radius

    def __repr__(self):
        return f"Circle(radius={self._radius})"

c = Circle(5)
print(f"Circle: {c}")
print(f"  radius: {c.radius}")
print(f"  diameter: {c.diameter}")
print(f"  area: {c.area:.2f}")
print(f"  circumference: {c.circumference:.2f}")

c.radius = 10
print(f"\nAfter c.radius = 10:")
print(f"  area: {c.area:.2f}")

try:
    c.radius = -1
except ValueError as e:
    print(f"  Error: {e}")

# === Putting It All Together ===

print("\n--- Complete Example: BankAccount ---")

class BankAccount:
    """A simple bank account."""

    bank_name = "Python Bank"
    _total_accounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._transactions = []
        BankAccount._total_accounts += 1
        self._account_number = BankAccount._total_accounts

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(("withdraw", amount))
        return self._balance

    @classmethod
    def get_total_accounts(cls):
        return cls._total_accounts

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def __str__(self):
        return f"{self.owner}'s account (#{self._account_number}): ${self._balance:.2f}"

    def __repr__(self):
        return (f"BankAccount(owner={self.owner!r}, "
                f"balance={self._balance!r})")

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

print(acc1)
print(acc2)

acc1.deposit(250)
acc1.withdraw(100)
print(f"\nAfter transactions: {acc1}")
print(f"Balance: ${acc1.balance:.2f}")

print(f"\nTotal accounts: {BankAccount.get_total_accounts()}")
print(f"Valid amount 50: {BankAccount.validate_amount(50)}")
print(f"Valid amount -5: {BankAccount.validate_amount(-5)}")
