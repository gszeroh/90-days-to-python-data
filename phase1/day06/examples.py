"""
Day 06: Control Flow — Loops — Examples
"""

# === Basic for Loop ===

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char, end=" ")
print()  # newline

# === range() Function ===

# range(stop) — 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("range(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("range(0, 20, 4):")
for i in range(0, 20, 4):
    print(i, end=" ")
print()

# Counting backwards
print("range(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")
print()

# === while Loop ===

count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# Countdown
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print("Liftoff!")

# === break Statement ===

print("\nbreak example:")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(i, end=" ")
print()

# break in while loop
total = 0
while True:
    total += 1
    if total >= 5:
        break
print(f"Total after break: {total}")

# === continue Statement ===

print("\ncontinue example — odd numbers only:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# Skip negative values
values = [10, -3, 5, -7, 8, -1, 3]
positive_sum = 0
for v in values:
    if v < 0:
        continue
    positive_sum += v
print(f"Sum of positives: {positive_sum}")

# === pass Statement ===

print("\npass example:")
for i in range(5):
    if i == 3:
        pass  # placeholder for future logic
    print(i, end=" ")
print()

# === enumerate() ===

colors = ["red", "green", "blue", "yellow"]

print("\nenumerate (default start=0):")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

print("enumerate (start=1):")
for index, color in enumerate(colors, start=1):
    print(f"  {index}. {color}")

# === zip() ===

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

print("\nzip — two iterables:")
for name, score in zip(names, scores):
    print(f"  {name} scored {score}")

print("zip — three iterables:")
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score} ({grade})")

# zip stops at shortest
short = [1, 2]
long = ["a", "b", "c", "d"]
print("zip stops at shortest:")
for pair in zip(short, long):
    print(f"  {pair}")

# === Nested Loops ===

print("\nNested loop — coordinate pairs:")
for x in range(3):
    for y in range(3):
        print(f"({x},{y})", end=" ")
    print()

# Multiplication table (1-5)
print("Multiplication table:")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:4d}", end="")
    print()

# === Loop-else Clause ===

print("\nfor-else — prime checker:")
for n in range(2, 20):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            break
    else:
        print(f"  {n} is prime")

# while-else
print("\nwhile-else — search:")
items = [4, 7, 2, 9, 1]
target = 9
index = 0
while index < len(items):
    if items[index] == target:
        print(f"  Found {target} at index {index}")
        break
    index += 1
else:
    print(f"  {target} not found")

# === Accumulator Pattern ===

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"\nSum of {numbers}: {total}")

# === Counting Pattern ===

text = "mississippi"
count = 0
for char in text:
    if char == "s":
        count += 1
print(f"Letter 's' appears {count} times in '{text}'")

# === Building a New List ===

squares = []
for n in range(1, 11):
    squares.append(n ** 2)
print(f"Squares 1-10: {squares}")

# === Combining enumerate and zip ===

subjects = ["Math", "Science", "English"]
teachers = ["Dr. Smith", "Prof. Lee", "Ms. Chen"]

print("\nenumerate + zip:")
for i, (subject, teacher) in enumerate(zip(subjects, teachers), start=1):
    print(f"  {i}. {subject} — {teacher}")

# === Reverse Iteration ===

print("\nReverse iteration:")
for item in reversed(["first", "second", "third"]):
    print(f"  {item}")

# Using range to iterate in reverse
print("Countdown with range:")
for i in range(5, 0, -1):
    print(f"  {i}")
print("  Go!")
