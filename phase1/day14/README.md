# Day 14: OOP — Basics

## Overview
Object-Oriented Programming (OOP) lets you model real-world entities as
**objects** that bundle data (attributes) and behavior (methods) together.
Python's class system is straightforward yet powerful — supporting instance
and class attributes, multiple method types, and special "dunder" methods that
integrate your objects seamlessly with the language.

---

## 1. Classes and Objects

A **class** is a blueprint; an **object** (instance) is a concrete entity
created from that blueprint.

```python
class Dog:
    pass

fido = Dog()          # Create an instance
print(type(fido))     # <class '__main__.Dog'>
print(isinstance(fido, Dog))  # True
```

---

## 2. The `__init__` Method and `self`

`__init__` is called automatically when you create an instance. `self` refers
to the instance being created.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name        # Instance attribute
        self.breed = breed
        self.age = age

fido = Dog("Fido", "Labrador", 3)
print(fido.name)    # "Fido"
```

---

## 3. Instance Attributes vs Class Attributes

```python
class Dog:
    species = "Canis familiaris"     # Class attribute — shared by all

    def __init__(self, name, age):
        self.name = name             # Instance attribute — unique to each
        self.age = age

a = Dog("Fido", 3)
b = Dog("Rex", 5)

print(a.species)     # "Canis familiaris"
print(b.species)     # "Canis familiaris"  — same object
print(a.name)        # "Fido"
print(b.name)        # "Rex"              — different objects
```

> ⚠️ Be careful with mutable class attributes (like lists). All instances
> share the same object, so mutations affect everyone.

---

## 4. Instance Methods

Regular methods take `self` as the first parameter and can access/modify
instance state.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}"
```

---

## 5. Class Methods (`@classmethod`)

Class methods receive the **class** as the first argument (`cls`), not an
instance. They are commonly used as **alternative constructors**.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        import datetime
        age = datetime.date.today().year - birth_year
        return cls(name, age)

puppy = Dog.from_birth_year("Buddy", 2021)
```

---

## 6. Static Methods (`@staticmethod`)

Static methods don't receive `self` or `cls`. They're utility functions that
logically belong to the class but don't need instance or class state.

```python
class Dog:
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0

Dog.is_valid_name("Fido")   # True
Dog.is_valid_name("")        # False
```

---

## 7. `__str__` and `__repr__`

These special methods control how your objects are displayed.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # User-friendly string (used by print, str())
        return f"{self.name}, age {self.age}"

    def __repr__(self):
        # Developer-friendly string (used in REPL, debugging)
        return f"Dog(name={self.name!r}, age={self.age!r})"

d = Dog("Fido", 3)
print(d)          # Fido, age 3         (__str__)
print(repr(d))    # Dog(name='Fido', age=3)  (__repr__)
```

| Method | Used by | Purpose |
|--------|---------|---------|
| `__str__` | `print()`, `str()`, f-strings | Human-readable |
| `__repr__` | `repr()`, REPL, debugger | Unambiguous, ideally eval-able |

> 💡 Always implement `__repr__`. If `__str__` is not defined, Python falls
> back to `__repr__`.

---

## 8. Properties

Properties let you define computed attributes with getter/setter syntax.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)    # 5
print(c.area)      # 78.539...
c.radius = 10      # Uses the setter
```

---

## 9. Naming Conventions

| Convention | Meaning |
|-----------|---------|
| `name` | Public attribute |
| `_name` | "Protected" — internal use (convention only) |
| `__name` | Name-mangled — harder to access from outside |
| `__name__` | "Dunder" — special Python methods |

---

## Key Takeaways
- A class defines a blueprint; instances are created by calling the class.
- `__init__` initializes instance attributes; `self` refers to the instance.
- Class attributes are shared; instance attributes are per-object.
- Use `@classmethod` for alternative constructors and `@staticmethod` for utilities.
- Implement `__repr__` (always) and `__str__` (for user-facing output).
- Use `@property` to create computed or validated attributes.

---

## Further Reading
- [Python Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Docs — Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Real Python — @property](https://realpython.com/python-property/)
