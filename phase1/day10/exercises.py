"""
Day 10: Dictionaries & Sets — Exercises

Complete each function below according to its docstring.
Replace `pass` with your implementation.
"""


# === Exercise 1: Word Frequency Counter ===

def word_frequency(text):
    """Return a dictionary mapping each word to its frequency.

    Convert text to lowercase and split on whitespace.
    Do not worry about punctuation.

    Examples:
        word_frequency("the cat and the dog")
            -> {"the": 2, "cat": 1, "and": 1, "dog": 1}

        word_frequency("hello hello hello")
            -> {"hello": 3}

        word_frequency("")
            -> {}
    """
    pass


# === Exercise 2: Merge Dictionaries ===

def merge_dicts(*dicts):
    """Merge multiple dictionaries into one.

    If a key appears in multiple dicts, the value from the last dict wins.

    Do NOT use the | operator (to support Python < 3.9).

    Examples:
        merge_dicts({"a": 1}, {"b": 2}, {"c": 3})
            -> {"a": 1, "b": 2, "c": 3}

        merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
            -> {"a": 1, "b": 3, "c": 4}

        merge_dicts()
            -> {}

        merge_dicts({"x": 10})
            -> {"x": 10}
    """
    pass


# === Exercise 3: Set Operations ===

def analyze_groups(group_a, group_b):
    """Analyze two groups of members using set operations.

    Given two lists of member names, return a dictionary with:
        "only_a":    sorted list of members only in group_a
        "only_b":    sorted list of members only in group_b
        "both":      sorted list of members in both groups
        "either":    sorted list of members in either group
        "total":     total number of unique members

    Examples:
        analyze_groups(
            ["Alice", "Bob", "Charlie"],
            ["Bob", "David", "Charlie"]
        ) -> {
            "only_a": ["Alice"],
            "only_b": ["David"],
            "both": ["Bob", "Charlie"],
            "either": ["Alice", "Bob", "Charlie", "David"],
            "total": 4
        }
    """
    pass


# === Exercise 4: Group By ===

def group_by_key(items, key_func):
    """Group a list of items by the result of key_func.

    Return a dictionary where each key is the result of key_func(item)
    and each value is a list of items that produced that key.

    Maintain the original order of items within each group.

    Examples:
        group_by_key([1, 2, 3, 4, 5, 6], lambda x: "even" if x % 2 == 0 else "odd")
            -> {"odd": [1, 3, 5], "even": [2, 4, 6]}

        group_by_key(["apple", "ant", "banana", "avocado"], lambda s: s[0])
            -> {"a": ["apple", "ant", "avocado"], "b": ["banana"]}

        group_by_key([], lambda x: x)
            -> {}
    """
    pass


# === Exercise 5: Inventory Manager ===

def manage_inventory(operations):
    """Process a list of inventory operations and return the final state.

    Each operation is a tuple of (action, item, quantity):
        - ("add", item, qty)    — add qty to item's count
        - ("remove", item, qty) — subtract qty (minimum count is 0)
        - ("delete", item, 0)   — remove item entirely

    Return a dict of {item: quantity} for items with quantity > 0,
    sorted by item name.

    Examples:
        manage_inventory([
            ("add", "apple", 10),
            ("add", "banana", 5),
            ("remove", "apple", 3),
            ("add", "apple", 2),
            ("remove", "banana", 10),
            ("delete", "banana", 0),
        ])
        -> {"apple": 9}

        manage_inventory([
            ("add", "pen", 100),
            ("add", "pencil", 50),
            ("remove", "pen", 20),
        ])
        -> {"pen": 80, "pencil": 50}

        manage_inventory([])
        -> {}
    """
    pass
