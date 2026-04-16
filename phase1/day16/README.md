# Day 16: OOP — Advanced

## Overview

Building on the OOP fundamentals from Day 15, today we explore Python's advanced
object-oriented features: magic methods that let your classes integrate seamlessly
with Python's built-in syntax, properties for controlled attribute access,
dataclasses for reducing boilerplate, `__slots__` for memory optimization, and
composition as an alternative to inheritance.

---

## 1. Dunder / Magic Methods

Magic methods (also called "dunder" methods for their **d**ouble **under**score
naming) let you define how objects behave with built-in operations and syntax.

### Arithmetic Operators

| Method         | Operator | Example          |
|----------------|----------|------------------|
| `__add__`      | `+`      | `a + b`          |
| `__sub__`      | `-`      | `a - b`          |
| `__mul__`      | `*`      | `a * b`          |
| `__truediv__`  | `/`      | `a / b`          |
| `__floordiv__` | `//`     | `a // b`         |
| `__mod__`      | `%`      | `a % b`          |
| `__pow__`      | `**`     | `a ** b`         |

### Comparison Operators

| Method    | Operator | Example    |
|-----------|----------|------------|
| `__eq__`  | `==`     | `a == b`   |
| `__ne__`  | `!=`     | `a != b`   |
| `__lt__`  | `<`      | `a < b`    |
| `__le__`  | `<=`     | `a <= b`   |
| `__gt__`  | `>`      | `a > b`    |
| `__ge__`  | `>=`     | `a >= b`   |

### Container Protocol

| Method          | Syntax          | Purpose                  |
|-----------------|-----------------|--------------------------|
| `__len__`       | `len(obj)`      | Return length            |
| `__getitem__`   | `obj[key]`      | Access by index/key      |
| `__setitem__`   | `obj[key] = v`  | Set by index/key         |
| `__delitem__`   | `del obj[key]`  | Delete by index/key      |
| `__contains__`  | `x in obj`      | Membership test          |
| `__iter__`      | `for x in obj`  | Iteration support        |

### Other Useful Magic Methods

| Method       | Syntax        | Purpose                        |
|--------------|---------------|--------------------------------|
| `__call__`   | `obj()`       | Make object callable           |
| `__hash__`   | `hash(obj)`   | Hashability (sets, dict keys)  |
| `__repr__`   | `repr(obj)`   | Developer-friendly string      |
| `__str__`    | `str(obj)`    | User-friendly string           |
| `__bool__`   | `bool(obj)`   | Truthiness                     |

### `__repr__` vs `__str__`

- `__repr__` is for developers — should ideally be an expression that recreates
  the object. Used in the REPL and debuggers.
- `__str__` is for end users — a readable, friendly representation.
- If only one is defined, `__repr__` is the better choice since Python falls back
  to it when `__str__` is missing.

### `__hash__` and `__eq__`

If you define `__eq__`, Python sets `__hash__` to `None` by default (making the
object unhashable). If you want objects usable as dictionary keys or set members,
you must also define `__hash__`. The rule: **objects that compare equal must have
the same hash**.

---

## 2. The `@property` Decorator

The `@property` decorator lets you define methods that behave like attributes,
providing controlled access without changing the public API.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter — accessed as circle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter — assigned as circle.radius = 5"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Read-only computed property."""
        import math
        return math.pi * self._radius ** 2
```

### When to Use Properties

- **Validation**: Enforce constraints on attribute values.
- **Computed values**: Derive a value from other attributes.
- **Backward compatibility**: Replace a public attribute with logic without
  breaking existing code.
- **Lazy loading**: Compute expensive values only when accessed.

---

## 3. Dataclasses

The `dataclasses` module (Python 3.7+) auto-generates `__init__`, `__repr__`,
`__eq__`, and more from class annotations.

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"
```

### Dataclass Parameters

| Parameter      | Default | Purpose                               |
|----------------|---------|---------------------------------------|
| `init`         | `True`  | Generate `__init__`                   |
| `repr`         | `True`  | Generate `__repr__`                   |
| `eq`           | `True`  | Generate `__eq__` (and `__ne__`)      |
| `order`        | `False` | Generate `__lt__`, `__le__`, etc.     |
| `frozen`       | `False` | Make instances immutable              |
| `slots`        | `False` | Generate `__slots__` (Python 3.10+)  |

### Mutable Default Fields

Use `field(default_factory=...)` for mutable defaults:

```python
@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)
```

### Frozen Dataclasses

```python
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int
```

Frozen dataclasses are immutable and automatically hashable.

---

## 4. `__slots__`

By default, Python stores instance attributes in a per-instance `__dict__`
dictionary. `__slots__` replaces this with a fixed structure, providing:

- **Less memory** per instance (no `__dict__`).
- **Faster attribute access**.
- **Prevents accidental attribute creation**.

```python
class SlottedPoint:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### Trade-offs

| Feature                     | `__dict__` | `__slots__` |
|-----------------------------|------------|-------------|
| Memory per instance         | Higher     | Lower       |
| Attribute access speed      | Slower     | Faster      |
| Dynamic attribute addition  | Yes        | No          |
| Supports `__weakref__`      | Yes        | Only if listed |
| Inheritance complexity      | Simple     | Requires care |

---

## 5. Composition vs Inheritance

**Inheritance** models an "is-a" relationship. **Composition** models a "has-a"
relationship by embedding objects inside other objects.

```python
# Inheritance: Dog IS an Animal
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Composition: Car HAS an Engine
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

### When to Prefer Composition

- When the relationship is "has-a" rather than "is-a".
- When you need to combine behaviors from multiple sources.
- When you want to swap components at runtime.
- When deep inheritance hierarchies become hard to follow.

### Composition Pattern: Delegation

```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class Service:
    def __init__(self, logger=None):
        self.logger = logger or Logger()

    def process(self, data):
        self.logger.log(f"Processing {data}")
        return data.upper()
```

---

## Key Takeaways

1. Magic methods let your classes integrate with Python's syntax and built-ins.
2. `@property` provides controlled attribute access without changing the API.
3. Dataclasses eliminate boilerplate for data-holding classes.
4. `__slots__` optimize memory when you have many instances with fixed attributes.
5. Favor composition over inheritance when modeling "has-a" relationships.

---

## Further Reading

- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [dataclasses module](https://docs.python.org/3/library/dataclasses.html)
- [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)
