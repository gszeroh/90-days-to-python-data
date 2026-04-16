"""
Day 15: OOP — Inheritance & Polymorphism — Solutions
"""

from abc import ABC, abstractmethod
import math


# === Exercise 1: Shape Hierarchy ===

class Shape(ABC):
    """Abstract base class for all shapes.

    Abstract Methods:
        area() -> float
        perimeter() -> float

    Concrete Method:
        describe() -> str:
            Return "{ClassName}: area={area:.2f}, perimeter={perimeter:.2f}"
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return (f"{type(self).__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


class Circle(Shape):
    """A circle defined by its radius.

    Args:
        radius (float): Must be positive.

    Examples:
        c = Circle(5)
        c.area()       -> 78.53981633974483
        c.perimeter()  -> 31.41592653589793
        c.describe()   -> "Circle: area=78.54, perimeter=31.42"
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class RectangleShape(Shape):
    """A rectangle defined by width and height.

    Args:
        width (float): Must be positive.
        height (float): Must be positive.

    Examples:
        r = RectangleShape(4, 6)
        r.area()       -> 24
        r.perimeter()  -> 20
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class TriangleShape(Shape):
    """A triangle defined by three side lengths.

    Uses Heron's formula for area.

    Args:
        a, b, c (float): Side lengths (must be positive and form a valid triangle).

    Examples:
        t = TriangleShape(3, 4, 5)
        t.area()       -> 6.0
        t.perimeter()  -> 12
    """

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Side lengths must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Side lengths do not form a valid triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# === Exercise 2: Animal Hierarchy ===

class Animal:
    """Base class for animals.

    Args:
        name (str): The animal's name.
        sound (str): The sound the animal makes (default "...").

    Methods:
        speak() -> str: Return "{name} says {sound}!"
        __str__() -> str: Return "{ClassName}({name})"
    """

    def __init__(self, name, sound="..."):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"{type(self).__name__}({self.name})"


class Pet(Animal):
    """A domesticated animal with an owner.

    Additional Args:
        owner (str): The pet owner's name.

    Additional Method:
        info() -> str:
            Return "{name} is owned by {owner}"
    """

    def __init__(self, name, owner, sound="..."):
        super().__init__(name, sound)
        self.owner = owner

    def info(self):
        return f"{self.name} is owned by {self.owner}"


class DogAnimal(Pet):
    """A dog — always sounds "Woof".

    Args:
        name (str): Dog's name.
        owner (str): Owner's name.
        breed (str): Dog breed (default "Mixed").

    Overrides:
        speak() -> str: Return "{name} says Woof! (tail wagging)"
    """

    def __init__(self, name, owner, breed="Mixed"):
        super().__init__(name, owner, sound="Woof")
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof! (tail wagging)"


class CatAnimal(Pet):
    """A cat — always sounds "Meow".

    Args:
        name (str): Cat's name.
        owner (str): Owner's name.
        indoor (bool): Whether the cat is indoor-only (default True).

    Overrides:
        speak() -> str: Return "{name} says Meow! (purring)"
    """

    def __init__(self, name, owner, indoor=True):
        super().__init__(name, owner, sound="Meow")
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says Meow! (purring)"


# === Exercise 3: Employee Types ===

class Employee:
    """Base class for employees.

    Args:
        name (str): Employee name.
        employee_id (str): Unique identifier.

    Abstract-like method (implement in subclasses):
        calculate_pay() -> float: Return pay for a period.

    Method:
        __str__() -> str: "{name} (ID: {employee_id})"
    """

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay()")

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"


class SalariedEmployee(Employee):
    """An employee paid a fixed annual salary.

    Additional Args:
        annual_salary (float): Yearly salary.

    Methods:
        calculate_pay() -> float:
            Return monthly pay (annual_salary / 12).
    """

    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12


class HourlyEmployee(Employee):
    """An employee paid by the hour.

    Additional Args:
        hourly_rate (float): Pay per hour.
        hours_worked (float): Hours worked this period (default 0).

    Methods:
        log_hours(hours) -> None: Add hours to hours_worked.
        calculate_pay() -> float:
            Regular pay for first 40 hours, 1.5x for overtime.
    """

    def __init__(self, name, employee_id, hourly_rate, hours_worked=0):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def log_hours(self, hours):
        self.hours_worked += hours

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        regular = self.hourly_rate * 40
        overtime = self.hourly_rate * 1.5 * (self.hours_worked - 40)
        return regular + overtime


class CommissionEmployee(SalariedEmployee):
    """A salaried employee who also earns commission.

    Additional Args:
        commission_rate (float): Percentage as decimal (e.g. 0.05 = 5%).
        sales (float): Total sales this period (default 0).

    Methods:
        add_sales(amount) -> None: Add to sales.
        calculate_pay() -> float:
            Monthly salary + (sales * commission_rate).
    """

    def __init__(self, name, employee_id, annual_salary, commission_rate, sales=0):
        super().__init__(name, employee_id, annual_salary)
        self.commission_rate = commission_rate
        self.sales = sales

    def add_sales(self, amount):
        self.sales += amount

    def calculate_pay(self):
        base = super().calculate_pay()
        return base + (self.sales * self.commission_rate)


# === Exercise 4: Vehicle Hierarchy with Mixin ===

class FuelMixin:
    """Mixin that adds fuel tracking.

    Attributes:
        fuel_level (float): Current fuel (starts at max_fuel).
        max_fuel (float): Tank capacity.

    Methods:
        refuel(amount=None) -> float:
            Add fuel (default fills to max). Return new level.
            Do not exceed max_fuel.
        use_fuel(amount) -> float:
            Subtract fuel. Raise ValueError if insufficient.
            Return remaining fuel.
    """

    def init_fuel(self, max_fuel):
        self.max_fuel = max_fuel
        self.fuel_level = max_fuel

    def refuel(self, amount=None):
        if amount is None:
            self.fuel_level = self.max_fuel
        else:
            self.fuel_level = min(self.fuel_level + amount, self.max_fuel)
        return self.fuel_level

    def use_fuel(self, amount):
        if amount > self.fuel_level:
            raise ValueError(
                f"Insufficient fuel: need {amount}, have {self.fuel_level}"
            )
        self.fuel_level -= amount
        return self.fuel_level


class Vehicle(ABC):
    """Abstract base class for vehicles.

    Args:
        make (str): Manufacturer.
        model (str): Model name.
        year (int): Year of manufacture.

    Abstract Method:
        max_speed() -> int: Return the top speed in km/h.

    Method:
        description() -> str:
            "{year} {make} {model} (max {max_speed()} km/h)"
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def max_speed(self):
        pass

    def description(self):
        return f"{self.year} {self.make} {self.model} (max {self.max_speed()} km/h)"


class Car(Vehicle, FuelMixin):
    """A car with fuel tracking.

    Additional Args:
        max_fuel (float): Tank capacity in liters (default 50).

    max_speed() -> int: Return 200.
    """

    def __init__(self, make, model, year, max_fuel=50):
        super().__init__(make, model, year)
        self.init_fuel(max_fuel)

    def max_speed(self):
        return 200


class Motorcycle(Vehicle, FuelMixin):
    """A motorcycle with fuel tracking.

    Additional Args:
        max_fuel (float): Tank capacity in liters (default 15).

    max_speed() -> int: Return 180.
    """

    def __init__(self, make, model, year, max_fuel=15):
        super().__init__(make, model, year)
        self.init_fuel(max_fuel)

    def max_speed(self):
        return 180


# === Exercise 5: Notification System ===

class Notification(ABC):
    """Abstract base class for notifications.

    Args:
        recipient (str): Who receives the notification.
        message (str): The notification content.

    Abstract Method:
        send() -> str: Send the notification and return a status string.

    Concrete Method:
        format_message() -> str:
            Return "To: {recipient} | {message}"
    """

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def format_message(self):
        return f"To: {self.recipient} | {self.message}"


class EmailNotification(Notification):
    """Send notification via email.

    Additional Args:
        subject (str): Email subject line.

    send() -> str:
        Return "Email sent to {recipient}: [{subject}] {message}"
    """

    def __init__(self, recipient, message, subject):
        super().__init__(recipient, message)
        self.subject = subject

    def send(self):
        return f"Email sent to {self.recipient}: [{self.subject}] {self.message}"


class SMSNotification(Notification):
    """Send notification via SMS.

    send() -> str:
        Truncate message to 160 characters if longer.
        Return "SMS sent to {recipient}: {truncated_message}"
    """

    def send(self):
        truncated = self.message[:160]
        return f"SMS sent to {self.recipient}: {truncated}"


class PushNotification(Notification):
    """Send notification via push notification.

    Additional Args:
        device_id (str): Target device identifier.

    send() -> str:
        Return "Push sent to {device_id} for {recipient}: {message}"
    """

    def __init__(self, recipient, message, device_id):
        super().__init__(recipient, message)
        self.device_id = device_id

    def send(self):
        return f"Push sent to {self.device_id} for {self.recipient}: {self.message}"
