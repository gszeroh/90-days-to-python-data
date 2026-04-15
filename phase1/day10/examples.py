"""
Day 10: Dictionaries & Sets — Examples
"""

# === Creating Dictionaries ===

person = {"name": "Alice", "age": 30, "city": "NYC"}
print(f"person: {person}")

# dict() constructor
config = dict(debug=True, verbose=False, timeout=30)
print(f"config: {config}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(f"from pairs: {d}")

# === Accessing and Modifying ===

print(f"\nperson['name'] = {person['name']}")
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('email', 'N/A') = {person.get('email', 'N/A')}")

# Add / Update
person["email"] = "alice@example.com"
person["age"] = 31
print(f"After update: {person}")

# Delete
del person["email"]
removed = person.pop("city")
print(f"Removed city={removed}: {person}")

# pop with default
missing = person.pop("phone", "not found")
print(f"pop missing key: {missing}")

# === Dictionary Methods ===

print("\n--- Dict Methods ---")

d = {"a": 1, "b": 2, "c": 3, "d": 4}

print(f"keys:   {list(d.keys())}")
print(f"values: {list(d.values())}")
print(f"items:  {list(d.items())}")

# Iterating
print("\nIterating with items():")
for key, value in d.items():
    print(f"  {key} → {value}")

# update
d.update({"b": 20, "e": 5})
print(f"\nAfter update: {d}")

# setdefault
d.setdefault("f", 6)
d.setdefault("a", 999)  # Already exists, no change
print(f"After setdefault: {d}")

# Membership testing
print(f"\n'a' in d: {'a' in d}")
print(f"'z' in d: {'z' in d}")

# === Dictionary Comprehensions ===

print("\n--- Dict Comprehensions ---")

squares = {x: x ** 2 for x in range(6)}
print(f"Squares: {squares}")

even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Invert a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined: {combined}")

# Word lengths
words = ["hello", "world", "python", "is", "great"]
word_lens = {w: len(w) for w in words}
print(f"Word lengths: {word_lens}")

# === Merge Operators (Python 3.9+) ===

print("\n--- Merge Operators ---")

defaults = {"color": "blue", "size": "medium", "weight": "light"}
custom = {"size": "large", "weight": "heavy"}

merged = defaults | custom
print(f"defaults | custom: {merged}")

# |= update in place
copy = defaults.copy()
copy |= custom
print(f"defaults |= custom: {copy}")

# === defaultdict ===

print("\n--- defaultdict ---")

from collections import defaultdict

# Group words by length
word_groups = defaultdict(list)
for word in ["cat", "dog", "fish", "bird", "ant", "bee", "bear"]:
    word_groups[len(word)].append(word)

print("Words grouped by length:")
for length, group in sorted(word_groups.items()):
    print(f"  {length} letters: {group}")

# Count characters
char_count = defaultdict(int)
for char in "abracadabra":
    char_count[char] += 1
print(f"\nChar counts: {dict(char_count)}")

# Nested defaultdict
nested = defaultdict(lambda: defaultdict(int))
nested["fruits"]["apple"] += 3
nested["fruits"]["banana"] += 2
nested["veggies"]["carrot"] += 5
print(f"\nNested: {dict({k: dict(v) for k, v in nested.items()})}")

# === Counter ===

print("\n--- Counter ---")

from collections import Counter

# Count characters
c = Counter("mississippi")
print(f"Counter('mississippi'): {c}")
print(f"Most common 2: {c.most_common(2)}")

# Count words
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
word_counts = Counter(words)
print(f"\nWord counts: {word_counts}")
print(f"apple count: {word_counts['apple']}")
print(f"missing key: {word_counts['grape']}")  # Returns 0, no KeyError

# Counter arithmetic
c1 = Counter(a=3, b=1, c=2)
c2 = Counter(a=1, b=3, c=1)
print(f"\nc1 = {c1}")
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1 + c2}")
print(f"c1 - c2 = {c1 - c2}")  # Keeps only positive counts
print(f"c1 & c2 = {c1 & c2}")  # Minimum of each
print(f"c1 | c2 = {c1 | c2}")  # Maximum of each

# === Creating Sets ===

print("\n--- Sets ---")

fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
print(f"fruits: {fruits}")
print(f"numbers: {numbers}")

# From a list (removes duplicates)
unique = set([1, 2, 2, 3, 3, 3, 4])
print(f"Unique from list: {unique}")

# From a string
chars = set("hello")
print(f"Unique chars in 'hello': {chars}")

# Empty set
empty = set()
print(f"Empty set: {empty}, type: {type(empty)}")

# === Set Operations ===

print("\n--- Set Operations ---")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"a = {a}")
print(f"b = {b}")
print(f"a | b  (union):       {a | b}")
print(f"a & b  (intersection): {a & b}")
print(f"a - b  (difference):   {a - b}")
print(f"b - a  (difference):   {b - a}")
print(f"a ^ b  (symmetric):    {a ^ b}")

# Subset and superset
small = {1, 2}
print(f"\n{small} <= {a} (subset):   {small <= a}")
print(f"{a} >= {small} (superset): {a >= small}")
print(f"{a} <= {b} (subset):   {a <= b}")

# === Set Methods ===

print("\n--- Set Methods ---")

s = {1, 2, 3}
print(f"Original: {s}")

s.add(4)
print(f"add(4): {s}")

s.discard(2)
print(f"discard(2): {s}")

s.discard(99)  # No error
print(f"discard(99): {s}")

s.update([5, 6, 7])
print(f"update([5, 6, 7]): {s}")

# === frozenset ===

print("\n--- frozenset ---")

fs = frozenset([1, 2, 3, 4])
print(f"frozenset: {fs}")

# Can be used as dict key
cache = {frozenset(["a", "b"]): "result_1", frozenset(["c"]): "result_2"}
print(f"Dict with frozenset keys: {cache}")
print(f"Lookup: {cache[frozenset(['a', 'b'])]}")

# Can be element of a set
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {set_of_sets}")

# === Practical Patterns ===

print("\n--- Practical Patterns ---")

# Remove duplicates while preserving order
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
seen = set()
unique_ordered = []
for item in items:
    if item not in seen:
        seen.add(item)
        unique_ordered.append(item)
print(f"Unique (ordered): {unique_ordered}")

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Common elements: {common}")

# Set comprehension
even_set = {x for x in range(20) if x % 2 == 0}
print(f"Even set: {even_set}")
