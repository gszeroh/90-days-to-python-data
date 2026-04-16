"""
Day 16: OOP — Advanced (Examples)
Topics: Magic methods, @property, dataclasses, __slots__, composition
"""

import math
from dataclasses import dataclass, field
import sys


# === Magic Methods: Vector Class ===

class Vector:
    """A 2D vector demonstrating common magic methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representations
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Arithmetic
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.magnitude < other.magnitude

    # Hashing (required if __eq__ is defined and you want set/dict support)
    def __hash__(self):
        return hash((self.x, self.y))

    # Unary
    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return self.magnitude

    # Boolean
    def __bool__(self):
        return self.x != 0 or self.y != 0

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


print("=== Vector Magic Methods ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"repr: {repr(v1)}")
print(f"str:  {v1}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3  = {v1 * 3}")
print(f"3 * v1  = {3 * v1}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
print(f"v1 < v2: {v1 < v2}")
print(f"-v1 = {-v1}")
print(f"abs(v1) = {abs(v1)}")
print(f"bool(Vector(0, 0)): {bool(Vector(0, 0))}")
print(f"hash(v1): {hash(v1)}")
print(f"v1 in {{v1, v2}}: {v1 in {v1, v2}}")


# === Container Protocol: Custom Collection ===

class Deck:
    """A deck of cards demonstrating container magic methods."""

    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
             "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [f"{r}{s}" for s in self.SUITS for r in self.RANKS]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __contains__(self, card):
        return card in self.cards

    def __repr__(self):
        return f"Deck({len(self)} cards)"


print("\n=== Container Protocol: Deck ===")
deck = Deck()
print(f"len(deck): {len(deck)}")
print(f"deck[0]: {deck[0]}")
print(f"deck[-1]: {deck[-1]}")
print(f"deck[:3]: {deck[:3]}")
print(f"'A♠' in deck: {'A♠' in deck}")
print(f"'Joker' in deck: {'Joker' in deck}")
# Iteration works because __getitem__ is defined
print(f"First 5 cards: {[card for card in deck[:5]]}")


# === Callable Objects ===

class Multiplier:
    """A callable object that multiplies by a fixed factor."""

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

    def __repr__(self):
        return f"Multiplier({self.factor})"


print("\n=== Callable Objects ===")
double = Multiplier(2)
triple = Multiplier(3)
print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")
print(f"callable(double): {callable(double)}")
# Use as a function in map
print(f"map(double, [1,2,3]): {list(map(double, [1, 2, 3]))}")


# === @property Decorator ===

class Temperature:
    """Temperature with property-based conversion."""

    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    def __repr__(self):
        return f"Temperature({self._celsius}°C)"


print("\n=== @property Decorator ===")
temp = Temperature(100)
print(f"Celsius:    {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin:     {temp.kelvin}K")
temp.fahrenheit = 32
print(f"After setting 32°F -> {temp.celsius}°C")
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Validation error: {e}")


# === Dataclasses ===

@dataclass
class Point:
    x: float
    y: float
    label: str = "unnamed"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


@dataclass(order=True)
class Student:
    """Ordered dataclass — sorts by fields in declaration order."""
    gpa: float
    name: str = field(compare=False)
    courses: list = field(default_factory=list, compare=False, repr=False)


@dataclass(frozen=True)
class Color:
    """Immutable dataclass — automatically hashable."""
    r: int
    g: int
    b: int

    @property
    def hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"


print("\n=== Dataclasses ===")
p1 = Point(0, 0, "origin")
p2 = Point(3, 4)
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 == Point(0, 0, 'origin'): {p1 == Point(0, 0, 'origin')}")
print(f"Distance: {p1.distance_to(p2)}")

s1 = Student(3.8, "Alice", ["Math", "CS"])
s2 = Student(3.9, "Bob")
print(f"\ns1: {s1}")
print(f"s1 < s2 (by GPA): {s1 < s2}")

red = Color(255, 0, 0)
print(f"\nred: {red}")
print(f"red.hex: {red.hex}")
print(f"hash(red): {hash(red)}")
print(f"red in {{red}}: {red in {red}}")
try:
    red.r = 128
except AttributeError as e:
    print(f"Frozen error: {e}")


# === __slots__ for Memory Optimization ===

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SlottedPoint:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


print("\n=== __slots__ Memory Comparison ===")
regular = RegularPoint(1, 2)
slotted = SlottedPoint(1, 2)
print(f"RegularPoint has __dict__: {hasattr(regular, '__dict__')}")
print(f"SlottedPoint has __dict__: {hasattr(slotted, '__dict__')}")
print(f"RegularPoint size: {sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)} bytes")
print(f"SlottedPoint size: {sys.getsizeof(slotted)} bytes")

try:
    slotted.z = 3
except AttributeError as e:
    print(f"Cannot add attribute: {e}")


# === Composition vs Inheritance ===

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True
        return f"Engine ({self.horsepower}hp) started"

    def stop(self):
        self.running = False
        return "Engine stopped"


class GPS:
    def navigate(self, destination):
        return f"Navigating to {destination}"


class Car:
    """Car uses composition — it HAS an engine and a GPS."""

    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)
        self.gps = GPS()

    def start(self):
        return f"{self.model}: {self.engine.start()}"

    def drive_to(self, destination):
        if not self.engine.running:
            self.engine.start()
        return f"{self.model}: {self.gps.navigate(destination)}"

    def __repr__(self):
        return f"Car('{self.model}', {self.engine.horsepower}hp)"


print("\n=== Composition ===")
car = Car("Tesla Model 3", 283)
print(car)
print(car.start())
print(car.drive_to("San Francisco"))


# === Composition: Strategy Pattern ===

class CSVExporter:
    def export(self, data):
        return ",".join(str(v) for v in data)


class JSONExporter:
    def export(self, data):
        import json
        return json.dumps(data)


class Report:
    """Report delegates export to a composable exporter strategy."""

    def __init__(self, title, data, exporter=None):
        self.title = title
        self.data = data
        self.exporter = exporter or CSVExporter()

    def generate(self):
        return f"{self.title}: {self.exporter.export(self.data)}"


print("\n=== Composition: Strategy Pattern ===")
data = [1, 2, 3, 4, 5]
csv_report = Report("Sales", data, CSVExporter())
json_report = Report("Sales", data, JSONExporter())
print(csv_report.generate())
print(json_report.generate())
