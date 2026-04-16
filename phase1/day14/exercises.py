"""
Day 14: OOP Basics — Exercises

Complete each class below according to its docstring.
Replace `pass` with your implementation.
"""


# === Exercise 1: BankAccount ===

class BankAccount:
    """A bank account with deposit, withdraw, and transfer.

    Attributes:
        owner (str): Account holder's name.
        balance (float): Current balance (read-only property).

    Class Attributes:
        bank_name (str): "PyBank" for all accounts.

    Methods:
        deposit(amount) -> float:
            Add amount to balance. Raise ValueError if amount <= 0.
            Return new balance.

        withdraw(amount) -> float:
            Subtract amount from balance. Raise ValueError if amount <= 0
            or amount > balance.  Return new balance.

        transfer(other, amount) -> None:
            Withdraw amount from self and deposit into other account.

    Special Methods:
        __str__: "BankAccount(owner='Alice', balance=1000.00)"
        __repr__: same as __str__

    Examples:
        acc = BankAccount("Alice", 1000)
        acc.deposit(500)         -> 1500
        acc.withdraw(200)        -> 1300
        acc.balance              -> 1300
        str(acc)                 -> "BankAccount(owner='Alice', balance=1300.00)"
    """

    bank_name = "PyBank"

    def __init__(self, owner, balance=0):
        pass

    @property
    def balance(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, other, amount):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


# === Exercise 2: Student ===

class Student:
    """A student with grades.

    Attributes:
        name (str): Student's name.
        grades (list): List of numeric grades.

    Methods:
        add_grade(grade) -> None:
            Add a grade (0-100). Raise ValueError if out of range.

        average() -> float:
            Return the average grade. Return 0.0 if no grades.

        highest() -> float:
            Return the highest grade. Return 0.0 if no grades.

        is_passing(threshold=60) -> bool:
            Return True if average >= threshold.

    Class Method:
        from_dict(data) -> Student:
            Create a Student from {"name": str, "grades": list}.

    Examples:
        s = Student("Alice")
        s.add_grade(90)
        s.add_grade(85)
        s.average()       -> 87.5
        s.is_passing()    -> True
    """

    def __init__(self, name, grades=None):
        pass

    def add_grade(self, grade):
        pass

    def average(self):
        pass

    def highest(self):
        pass

    def is_passing(self, threshold=60):
        pass

    @classmethod
    def from_dict(cls, data):
        pass

    def __repr__(self):
        pass


# === Exercise 3: Rectangle ===

class Rectangle:
    """A rectangle with width and height.

    Properties (with validation — must be > 0):
        width (float): The width.
        height (float): The height.

    Read-only properties:
        area (float): width * height
        perimeter (float): 2 * (width + height)
        is_square (bool): True if width == height

    Static Method:
        from_square(side) -> Rectangle:
            Create a square (width == height == side).

    Special Methods:
        __str__: "Rectangle(4 x 5)"
        __repr__: "Rectangle(width=4, height=5)"

    Examples:
        r = Rectangle(4, 5)
        r.area        -> 20
        r.perimeter   -> 18
        r.is_square   -> False
        Rectangle.from_square(5).is_square  -> True
    """

    def __init__(self, width, height):
        pass

    @property
    def width(self):
        pass

    @width.setter
    def width(self, value):
        pass

    @property
    def height(self):
        pass

    @height.setter
    def height(self, value):
        pass

    @property
    def area(self):
        pass

    @property
    def perimeter(self):
        pass

    @property
    def is_square(self):
        pass

    @staticmethod
    def from_square(side):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


# === Exercise 4: Counter ===

class ClickCounter:
    """A counter that tracks clicks with a maximum value.

    Attributes:
        name (str): Counter name.
        count (int): Current count (read-only property, starts at 0).
        max_count (int): Maximum allowed count.

    Class Attribute:
        total_clicks (int): Total clicks across ALL counters.

    Methods:
        click(times=1) -> int:
            Increment count by `times`. If it would exceed max_count,
            set count to max_count instead. Update total_clicks.
            Return new count.

        reset() -> None:
            Reset count to 0 (do NOT adjust total_clicks).

    Examples:
        c = ClickCounter("btn", max_count=10)
        c.click()       -> 1
        c.click(5)      -> 6
        c.click(100)    -> 10  (capped at max_count)
        c.reset()
        c.count         -> 0
    """

    total_clicks = 0

    def __init__(self, name, max_count=100):
        pass

    @property
    def count(self):
        pass

    def click(self, times=1):
        pass

    def reset(self):
        pass

    def __repr__(self):
        pass


# === Exercise 5: Book ===

class Book:
    """A book in a library system.

    Attributes:
        title (str): Book title.
        author (str): Author name.
        isbn (str): ISBN identifier.
        available (bool): Whether the book is available.

    Methods:
        check_out() -> str:
            Mark as unavailable. Return "{title} checked out."
            Raise RuntimeError if already checked out.

        return_book() -> str:
            Mark as available. Return "{title} returned."
            Raise RuntimeError if already available.

    Class Method:
        from_string(book_str) -> Book:
            Parse "Title | Author | ISBN" format.

    Static Method:
        is_valid_isbn(isbn) -> bool:
            Return True if isbn is a string of exactly 13 digits.

    Special Methods:
        __str__: "'{title}' by {author}"
        __repr__: "Book(title='{title}', author='{author}', isbn='{isbn}')"

    Examples:
        b = Book("Python 101", "Guido", "1234567890123")
        str(b)          -> "'Python 101' by Guido"
        b.check_out()   -> "Python 101 checked out."
        b.available     -> False
        b.return_book() -> "Python 101 returned."
    """

    def __init__(self, title, author, isbn, available=True):
        pass

    def check_out(self):
        pass

    def return_book(self):
        pass

    @classmethod
    def from_string(cls, book_str):
        pass

    @staticmethod
    def is_valid_isbn(isbn):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
