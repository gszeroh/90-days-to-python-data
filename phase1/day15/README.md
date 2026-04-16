# Day 15: OOP — Inheritance & Polymorphism

## Overview
Inheritance lets you build new classes on top of existing ones, reusing code
and establishing "is-a" relationships. Combined with **polymorphism** — the
ability for different types to respond to the same interface — inheritance
enables flexible, extensible designs. Python also supports **multiple
inheritance**, **abstract base classes**, and **mixins**, giving you a rich
toolkit for class hierarchies.

---

## 1. Single Inheritance

A child class inherits all attributes and methods from its parent.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):                  # Override parent method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

d = Dog("Rex")
print(d.speak())    # "Rex says Woof!"
print(d.name)       # "Rex" — inherited from Animal
```

---

## 2. The `super()` Function

`super()` calls a method from the parent class. It's essential for extending
(not replacing) parent behavior.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Canine")
        self.breed = breed          # Additional attribute

d = Dog("Rex", "Labrador")
print(d.name)       # "Rex"       — set by Animal.__init__
print(d.species)    # "Canine"    — set by Animal.__init__
print(d.breed)      # "Labrador"  — set by Dog.__init__
```

---

## 3. Method Overriding

A child class can **override** any parent method by defining a method with the
same name.

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                   # Overrides Shape.area
        import math
        return math.pi * self.radius ** 2
```

---

## 4. `isinstance()` and `issubclass()`

```python
d = Dog("Rex", "Lab")

isinstance(d, Dog)       # True
isinstance(d, Animal)    # True  — Dog IS an Animal
isinstance(d, Cat)       # False

issubclass(Dog, Animal)  # True
issubclass(Dog, object)  # True  — everything inherits from object
issubclass(Animal, Dog)  # False
```

---

## 5. Multiple Inheritance

A class can inherit from multiple parents.

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says Quack!"

donald = Duck("Donald")
print(donald.speak())    # "Donald says Quack!"
print(donald.fly())      # "Donald is flying"
print(donald.swim())     # "Donald is swimming"
```

---

## 6. Method Resolution Order (MRO)

When multiple parents define the same method, Python uses the **C3
linearization** algorithm to determine the order.

```python
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B"

class C(A):
    def greet(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.greet())         # "B"  — B comes before C in MRO

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

---

## 7. Abstract Base Classes (ABC)

ABCs define **interfaces** — they declare methods that subclasses **must**
implement.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass

    def describe(self):
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

# Cannot instantiate an ABC:
# shape = Shape()  # TypeError!

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(4, 5)
print(r.describe())   # "Area: 20.00, Perimeter: 18.00"
```

> 💡 ABCs enforce that subclasses provide required methods at **instantiation
> time**, not at call time. This catches errors early.

---

## 8. Polymorphism

Polymorphism means different types respond to the **same interface**.

```python
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

for shape in shapes:
    print(f"{type(shape).__name__}: area = {shape.area():.2f}")
```

No `if/elif` chain needed — each shape knows how to compute its own area.

---

## 9. Mixins

A **mixin** is a class designed to add functionality to other classes through
multiple inheritance. Mixins typically don't stand alone.

```python
class JSONMixin:
    """Add JSON serialization to any class."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__, default=str)

class LogMixin:
    """Add logging to any class."""
    def log(self, message):
        print(f"[{type(self).__name__}] {message}")

class User(JSONMixin, LogMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

u = User("Alice", "alice@example.com")
print(u.to_json())    # {"name": "Alice", "email": "alice@example.com"}
u.log("Logged in")    # [User] Logged in
```

---

## 10. Best Practices

| Guideline | Reason |
|-----------|--------|
| Prefer composition over inheritance | Reduces coupling |
| Keep hierarchies shallow | Deep trees are hard to follow |
| Use ABCs to define interfaces | Forces implementation of required methods |
| Favour single inheritance + mixins | Avoids diamond-problem complexity |
| Call `super()` consistently | Ensures all parents are initialized |

---

## Key Takeaways
- Inheritance creates "is-a" relationships; child classes reuse parent code.
- Use `super()` to extend (not replace) parent initialization and methods.
- `isinstance()` checks the full inheritance chain.
- Python's MRO (C3 linearization) determines method lookup order.
- Abstract base classes enforce interfaces — unimplemented methods cause errors.
- Polymorphism lets you write code that works with any object supporting the interface.
- Mixins add capabilities without deep hierarchies.

---

## Further Reading
- [Python Docs — Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Python Docs — abc module](https://docs.python.org/3/library/abc.html)
- [Real Python — Inheritance & Composition](https://realpython.com/inheritance-composition-python/)
- [Real Python — Abstract Classes](https://realpython.com/python-interface/)
- [Python MRO (Method Resolution Order)](https://docs.python.org/3/howto/mro.html)
