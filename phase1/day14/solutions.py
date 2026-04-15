"""
Day 14: OOP Basics — Solutions
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
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"

    def __repr__(self):
        return self.__str__()


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
        self.name = name
        self.grades = list(grades) if grades else []

    def add_grade(self, grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def highest(self):
        if not self.grades:
            return 0.0
        return max(self.grades)

    def is_passing(self, threshold=60):
        return self.average() >= threshold

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("grades", []))

    def __repr__(self):
        return f"Student(name={self.name!r}, grades={self.grades!r})"


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
        self.width = width    # Uses the setter for validation
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    @property
    def is_square(self):
        return self._width == self._height

    @staticmethod
    def from_square(side):
        return Rectangle(side, side)

    def __str__(self):
        return f"Rectangle({self._width} x {self._height})"

    def __repr__(self):
        return f"Rectangle(width={self._width}, height={self._height})"


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
        self.name = name
        self._count = 0
        self.max_count = max_count

    @property
    def count(self):
        return self._count

    def click(self, times=1):
        actual = min(times, self.max_count - self._count)
        if actual > 0:
            self._count += actual
            ClickCounter.total_clicks += actual
        return self._count

    def reset(self):
        self._count = 0

    def __repr__(self):
        return f"ClickCounter(name={self.name!r}, count={self._count}, max={self.max_count})"


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
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def check_out(self):
        if not self.available:
            raise RuntimeError(f"{self.title} is already checked out")
        self.available = False
        return f"{self.title} checked out."

    def return_book(self):
        if self.available:
            raise RuntimeError(f"{self.title} is already available")
        self.available = True
        return f"{self.title} returned."

    @classmethod
    def from_string(cls, book_str):
        parts = [part.strip() for part in book_str.split("|")]
        return cls(title=parts[0], author=parts[1], isbn=parts[2])

    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"
