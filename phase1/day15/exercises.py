"""
Day 15: OOP — Inheritance & Polymorphism — Exercises

Complete each class hierarchy below according to its docstring.
Replace `pass` with your implementation.
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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


class Pet(Animal):
    """A domesticated animal with an owner.

    Additional Args:
        owner (str): The pet owner's name.

    Additional Method:
        info() -> str:
            Return "{name} is owned by {owner}"
    """
    pass


class DogAnimal(Pet):
    """A dog — always sounds "Woof".

    Args:
        name (str): Dog's name.
        owner (str): Owner's name.
        breed (str): Dog breed (default "Mixed").

    Overrides:
        speak() -> str: Return "{name} says Woof! (tail wagging)"
    """
    pass


class CatAnimal(Pet):
    """A cat — always sounds "Meow".

    Args:
        name (str): Cat's name.
        owner (str): Owner's name.
        indoor (bool): Whether the cat is indoor-only (default True).

    Overrides:
        speak() -> str: Return "{name} says Meow! (purring)"
    """
    pass


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
    pass


class SalariedEmployee(Employee):
    """An employee paid a fixed annual salary.

    Additional Args:
        annual_salary (float): Yearly salary.

    Methods:
        calculate_pay() -> float:
            Return monthly pay (annual_salary / 12).
    """
    pass


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
    pass


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
    pass


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
    pass


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
    pass


class Car(Vehicle, FuelMixin):
    """A car with fuel tracking.

    Additional Args:
        max_fuel (float): Tank capacity in liters (default 50).

    max_speed() -> int: Return 200.
    """
    pass


class Motorcycle(Vehicle, FuelMixin):
    """A motorcycle with fuel tracking.

    Additional Args:
        max_fuel (float): Tank capacity in liters (default 15).

    max_speed() -> int: Return 180.
    """
    pass


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
    pass


class EmailNotification(Notification):
    """Send notification via email.

    Additional Args:
        subject (str): Email subject line.

    send() -> str:
        Return "Email sent to {recipient}: [{subject}] {message}"
    """
    pass


class SMSNotification(Notification):
    """Send notification via SMS.

    send() -> str:
        Truncate message to 160 characters if longer.
        Return "SMS sent to {recipient}: {truncated_message}"
    """
    pass


class PushNotification(Notification):
    """Send notification via push notification.

    Additional Args:
        device_id (str): Target device identifier.

    send() -> str:
        Return "Push sent to {device_id} for {recipient}: {message}"
    """
    pass
