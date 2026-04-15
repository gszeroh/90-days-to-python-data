# Day 06: Control Flow — Loops

## Overview
Loops let you execute a block of code repeatedly. Python provides two loop
constructs — `for` and `while` — along with powerful tools like `range()`,
`enumerate()`, and `zip()` to make iteration concise and expressive.

---

## 1. The `for` Loop

Iterate over any **iterable** (list, string, tuple, range, dict, etc.).

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Iterating Over Strings
```python
for char in "Python":
    print(char, end=" ")
# P y t h o n
```

---

## 2. The `range()` Function

Generate a sequence of numbers without creating a full list in memory.

```python
range(stop)             # 0, 1, ..., stop-1
range(start, stop)      # start, start+1, ..., stop-1
range(start, stop, step)  # start, start+step, ..., up to (not including) stop
```

```python
for i in range(5):
    print(i)            # 0 1 2 3 4

for i in range(2, 8):
    print(i)            # 2 3 4 5 6 7

for i in range(0, 10, 3):
    print(i)            # 0 3 6 9

for i in range(10, 0, -2):
    print(i)            # 10 8 6 4 2
```

---

## 3. The `while` Loop

Execute a block **as long as** a condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

> ⚠️ **Warning:** Always ensure the condition will eventually become `False`,
> or you'll create an **infinite loop**.

### Common Pattern: Input Validation
```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
```

---

## 4. `break`, `continue`, and `pass`

### `break` — Exit the Loop Immediately
```python
for n in range(10):
    if n == 5:
        break
    print(n)
# Prints 0 1 2 3 4
```

### `continue` — Skip to the Next Iteration
```python
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)
# Prints 1 3 5
```

### `pass` — Do Nothing (Placeholder)
```python
for n in range(5):
    if n == 3:
        pass  # TODO: handle this case later
    print(n)
```

---

## 5. `enumerate()` — Index + Value

Get both the **index** and the **value** while iterating.

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Start counting from 1
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")
```

---

## 6. `zip()` — Iterate in Parallel

Combine two or more iterables element-by-element.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

`zip()` stops at the **shortest** iterable. Use `itertools.zip_longest()` to
pad missing values.

```python
from itertools import zip_longest

a = [1, 2, 3]
b = ["x", "y"]

for pair in zip_longest(a, b, fillvalue="-"):
    print(pair)
# (1, 'x'), (2, 'y'), (3, '-')
```

---

## 7. Nested Loops

A loop inside another loop — the inner loop runs completely for each iteration
of the outer loop.

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
```

### Multiplication Table
```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:4d}", end="")
    print()
```

---

## 8. The `loop-else` Clause

Python's `for` and `while` loops support an optional `else` block that runs
**only if the loop completed without hitting `break`**.

```python
for n in range(2, 10):
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        # No break was hit → n is prime
        print(f"{n} is prime")
```

### `while-else`
```python
attempts = 0
while attempts < 3:
    guess = "wrong"
    if guess == "secret":
        print("Correct!")
        break
    attempts += 1
else:
    print("Out of attempts!")
```

---

## 9. Common Loop Patterns

### Accumulator Pattern
```python
total = 0
for n in [10, 20, 30, 40]:
    total += n
print(total)  # 100
```

### Counting Pattern
```python
count = 0
for char in "hello world":
    if char == "l":
        count += 1
print(count)  # 3
```

### Search Pattern
```python
items = [4, 7, 2, 9, 1]
target = 9

for item in items:
    if item == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found.")
```

### Building a New List
```python
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

---

## Key Takeaways
- `for` loops iterate over any iterable; `while` loops run as long as a
  condition is true.
- `range()` generates number sequences efficiently.
- `break` exits a loop; `continue` skips to the next iteration; `pass` does
  nothing.
- `enumerate()` gives index + value; `zip()` combines iterables in parallel.
- The `else` clause on a loop runs only when no `break` was hit.
- Avoid infinite loops — always ensure `while` conditions will eventually be
  `False`.

---

## Further Reading
- [Python Docs — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Docs — range()](https://docs.python.org/3/library/stdtypes.html#range)
- [Real Python — Python for Loops](https://realpython.com/python-for-loop/)
- [Real Python — Python while Loops](https://realpython.com/python-while-loop/)
