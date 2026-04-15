"""
Day 17: Iterators & Generators (Solutions)
"""

import itertools
import math


# === Exercise 1: Fibonacci Generator ===

def fibonacci(max_count=None):
    a, b = 0, 1
    count = 0
    while max_count is None or count < max_count:
        yield a
        a, b = b, a + b
        count += 1


# === Exercise 2: Custom Range Iterator ===

class FloatRange:
    def __init__(self, start, stop, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self._current = start

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self._current >= self.stop) or \
           (self.step < 0 and self._current <= self.stop):
            raise StopIteration
        value = self._current
        self._current += self.step
        # Round to avoid floating-point drift
        self._current = round(self._current, 10)
        return round(value, 10)

    def __len__(self):
        if (self.step > 0 and self.start >= self.stop) or \
           (self.step < 0 and self.start <= self.stop):
            return 0
        return math.ceil((self.stop - self.start) / self.step)

    def __repr__(self):
        return f"FloatRange({self.start}, {self.stop}, {self.step})"


# === Exercise 3: Chunk Generator ===

def chunked(iterable, n):
    iterator = iter(iterable)
    while True:
        chunk = list(itertools.islice(iterator, n))
        if not chunk:
            break
        yield chunk


# === Exercise 4: itertools Combinations ===

def find_combinations(numbers, target, size=2):
    return [
        combo
        for combo in itertools.combinations(numbers, size)
        if sum(combo) == target
    ]


# === Exercise 5: Infinite Counter with Transformations ===

class InfiniteCounter:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self._current = start

    def __iter__(self):
        self._current = self.start
        return self

    def __next__(self):
        value = self._current
        self._current += self.step
        return value

    def apply_filter(self, predicate):
        def _filtered():
            for value in InfiniteCounter(self.start, self.step):
                if predicate(value):
                    yield value
        return _filtered()

    def apply_map(self, func):
        def _mapped():
            for value in InfiniteCounter(self.start, self.step):
                yield func(value)
        return _mapped()


# === Verification ===

if __name__ == "__main__":
    # Exercise 1
    print("=== Exercise 1: Fibonacci ===")
    print(f"First 10: {list(fibonacci(10))}")
    # Infinite — take first 15
    fib_inf = fibonacci()
    first_15 = [next(fib_inf) for _ in range(15)]
    print(f"First 15 (infinite): {first_15}")

    # Exercise 2
    print("\n=== Exercise 2: FloatRange ===")
    fr = FloatRange(0, 1, 0.2)
    print(f"FloatRange(0, 1, 0.2): {list(fr)}")
    print(f"len: {len(fr)}")
    print(f"Reusable: {list(fr)}")
    print(f"FloatRange(0, -1, -0.3): {list(FloatRange(0, -1, -0.3))}")
    print(f"FloatRange(5, 5, 1): {list(FloatRange(5, 5, 1))}")

    # Exercise 3
    print("\n=== Exercise 3: Chunked ===")
    print(f"chunked(range(10), 3): {list(chunked(range(10), 3))}")
    print(f"chunked('abcdefg', 2): {list(chunked('abcdefg', 2))}")
    print(f"chunked([], 5): {list(chunked([], 5))}")
    # Works with generators too
    gen = (x ** 2 for x in range(7))
    print(f"chunked(squares, 3): {list(chunked(gen, 3))}")

    # Exercise 4
    print("\n=== Exercise 4: Find Combinations ===")
    nums = [1, 2, 3, 4, 5]
    print(f"Sum to 6, size 2: {find_combinations(nums, target=6, size=2)}")
    print(f"Sum to 6, size 3: {find_combinations(nums, target=6, size=3)}")
    print(f"Sum to 10, size 3: {find_combinations(nums, target=10, size=3)}")
    print(f"Sum to 15, size 5: {find_combinations(nums, target=15, size=5)}")

    # Exercise 5
    print("\n=== Exercise 5: InfiniteCounter ===")
    counter = InfiniteCounter(1, 2)
    first_5 = [next(counter) for _ in range(5)]
    print(f"First 5 odd numbers: {first_5}")

    counter2 = InfiniteCounter(0, 3)
    doubled = counter2.apply_map(lambda x: x * 2)
    first_5_doubled = [next(doubled) for _ in range(5)]
    print(f"Multiples of 3, doubled: {first_5_doubled}")

    counter3 = InfiniteCounter(1, 1)
    evens = counter3.apply_filter(lambda x: x % 2 == 0)
    first_5_evens = [next(evens) for _ in range(5)]
    print(f"Even numbers: {first_5_evens}")
