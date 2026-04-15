"""
Day 09: Lists & Tuples — Solutions
"""


# === Exercise 1: Flatten a Nested List ===

def flatten(nested):
    """Flatten a list of lists into a single list.

    Only flatten one level deep (not recursively).

    Examples:
        flatten([[1, 2], [3, 4], [5, 6]])       -> [1, 2, 3, 4, 5, 6]
        flatten([["a", "b"], ["c"]])             -> ["a", "b", "c"]
        flatten([[1], [], [2, 3]])               -> [1, 2, 3]
        flatten([])                              -> []
    """
    return [item for sublist in nested for item in sublist]


# === Exercise 2: List Comprehension Filter ===

def filter_and_transform(numbers):
    """Return a list of squared values for positive even numbers only.

    Use a single list comprehension.

    Steps:
        1. Keep only positive, even numbers
        2. Square each remaining number

    Examples:
        filter_and_transform([1, 2, 3, 4, 5, 6])      -> [4, 16, 36]
        filter_and_transform([-2, -1, 0, 1, 2, 3])     -> [4]
        filter_and_transform([1, 3, 5])                 -> []
        filter_and_transform([-4, -2, 0])               -> []
    """
    return [x ** 2 for x in numbers if x > 0 and x % 2 == 0]


# === Exercise 3: Matrix Transpose ===

def transpose(matrix):
    """Return the transpose of a matrix (list of lists).

    The transpose flips a matrix over its diagonal: rows become columns.

    Assume the matrix is rectangular (all rows have the same length).
    Return an empty list if the matrix is empty.

    Examples:
        transpose([[1, 2, 3],
                   [4, 5, 6]])
            -> [[1, 4], [2, 5], [3, 6]]

        transpose([[1, 2],
                   [3, 4],
                   [5, 6]])
            -> [[1, 3, 5], [2, 4, 6]]

        transpose([[1]])
            -> [[1]]

        transpose([])
            -> []
    """
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


# === Exercise 4: Chunk a List ===

def chunk(items, size):
    """Split a list into chunks of the given size.

    The last chunk may be smaller than size if the list isn't evenly divisible.
    If size is <= 0, return an empty list.

    Examples:
        chunk([1, 2, 3, 4, 5], 2)  -> [[1, 2], [3, 4], [5]]
        chunk([1, 2, 3, 4], 2)     -> [[1, 2], [3, 4]]
        chunk([1, 2, 3], 5)        -> [[1, 2, 3]]
        chunk([], 3)               -> []
        chunk([1, 2], 0)           -> []
    """
    if size <= 0:
        return []
    return [items[i:i + size] for i in range(0, len(items), size)]


# === Exercise 5: Tuple Records ===

def student_summary(records):
    """Process a list of student tuples and return a summary.

    Each record is a tuple of (name, score1, score2, score3).

    Return a list of tuples: (name, average_score) sorted by average
    score in descending order. Round the average to 1 decimal place.

    Examples:
        student_summary([
            ("Alice", 90, 85, 92),
            ("Bob", 78, 82, 80),
            ("Charlie", 95, 88, 91),
        ])
        -> [("Charlie", 91.3), ("Alice", 89.0), ("Bob", 80.0)]

        student_summary([("Zoe", 100, 100, 100)])
        -> [("Zoe", 100.0)]

        student_summary([])
        -> []
    """
    summaries = []
    for record in records:
        name = record[0]
        scores = record[1:]
        avg = round(sum(scores) / len(scores), 1)
        summaries.append((name, avg))
    summaries.sort(key=lambda s: s[1], reverse=True)
    return summaries
