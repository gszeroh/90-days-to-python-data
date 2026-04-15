"""
Day 15: OOP — Inheritance & Polymorphism — Examples
"""

import math
from abc import ABC, abstractmethod

# === Single Inheritance ===

print("--- Single Inheritance ---")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound"

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r})"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canine")
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Feline")
        self.color = color

    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers", "Orange")

print(f"{dog!r} → {dog.speak()}")
print(f"{cat!r} → {cat.speak()}")
print(f"Dog species: {dog.species}")
print(f"Dog breed: {dog.breed}")

# === super() in Action ===

print("\n--- super() ---")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r}, ${self.salary:,.0f})"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Initialize Employee part
        self.department = department

    def __repr__(self):
        base = super().__repr__()
        return f"{base} [dept={self.department}]"

mgr = Manager("Alice", 120000, "Engineering")
print(f"Manager: {mgr}")
print(f"Name: {mgr.name}, Salary: ${mgr.salary:,}")

# === isinstance() and issubclass() ===

print("\n--- isinstance / issubclass ---")

print(f"isinstance(dog, Dog):    {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"isinstance(dog, Cat):    {isinstance(dog, Cat)}")
print(f"isinstance(dog, object): {isinstance(dog, object)}")

print(f"\nissubclass(Dog, Animal):  {issubclass(Dog, Animal)}")
print(f"issubclass(Dog, object):  {issubclass(Dog, object)}")
print(f"issubclass(Animal, Dog):  {issubclass(Animal, Dog)}")

# === Method Overriding ===

print("\n--- Method Overriding ---")

class Vehicle:
    def start(self):
        return "Vehicle starting..."

    def fuel_type(self):
        return "Unknown"

class ElectricCar(Vehicle):
    def start(self):
        return "Electric motor humming..."

    def fuel_type(self):
        return "Electricity"

class GasCar(Vehicle):
    def start(self):
        return "Engine rumbling..."

    def fuel_type(self):
        return "Gasoline"

for v in [Vehicle(), ElectricCar(), GasCar()]:
    print(f"  {type(v).__name__}: {v.start()} (fuel: {v.fuel_type()})")

# === Multiple Inheritance ===

print("\n--- Multiple Inheritance ---")

class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, species="Bird")

    def speak(self):
        return f"{self.name} says Quack!"

donald = Duck("Donald")
print(f"{donald.speak()}")
print(f"{donald.fly()}")
print(f"{donald.swim()}")

# === Method Resolution Order (MRO) ===

print("\n--- MRO ---")

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(f"D().greet() = {d.greet()}")  # "Hello from B"

print("\nD.__mro__:")
for cls in D.__mro__:
    print(f"  {cls.__name__}")

# === Abstract Base Classes ===

print("\n--- Abstract Base Classes ---")

class Shape(ABC):
    """Abstract base class for shapes."""

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
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Cannot instantiate Shape directly
try:
    s = Shape()
except TypeError as e:
    print(f"Cannot instantiate ABC: {e}")

# But concrete subclasses work fine
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"  {shape.describe()}")

# === Polymorphism in Action ===

print("\n--- Polymorphism ---")

def print_areas(shapes):
    """Works with ANY object that has an area() method."""
    for shape in shapes:
        print(f"  {type(shape).__name__}: area = {shape.area():.2f}")

print_areas(shapes)

# === Mixins ===

print("\n--- Mixins ---")

import json

class JSONMixin:
    """Add JSON serialization capability."""
    def to_json(self):
        return json.dumps(self.__dict__, default=str, indent=2)

class LogMixin:
    """Add simple logging capability."""
    def log(self, message):
        print(f"  [{type(self).__name__}] {message}")

class User(JSONMixin, LogMixin):
    def __init__(self, name, email, role="user"):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        return f"User({self.name!r}, {self.email!r})"

user = User("Alice", "alice@example.com", role="admin")
print(f"User: {user}")
print(f"JSON:\n{user.to_json()}")
user.log("Created account")
user.log("Updated profile")

# === Inheritance Chain with super() ===

print("\n--- Cooperative super() ---")

class Base:
    def __init__(self, **kwargs):
        pass  # End of the chain

class Named(Base):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

class Aged(Base):
    def __init__(self, age, **kwargs):
        super().__init__(**kwargs)
        self.age = age

class Person(Named, Aged):
    def __init__(self, name, age, **kwargs):
        super().__init__(name=name, age=age, **kwargs)

    def __repr__(self):
        return f"Person({self.name!r}, age={self.age})"

p = Person("Bob", 30)
print(f"Person: {p}")
print(f"MRO: {[c.__name__ for c in Person.__mro__]}")
