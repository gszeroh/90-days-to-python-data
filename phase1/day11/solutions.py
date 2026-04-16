"""
Day 11: File I/O — Solutions
"""

import csv
import json
from pathlib import Path


# === Exercise 1: Count Words in a File ===

def count_words_in_file(filepath):
    """Read a text file and return the total number of words.

    Words are separated by whitespace.  Ignore leading/trailing whitespace
    on each line.

    Args:
        filepath: Path to the text file.

    Returns:
        int: Total word count.

    Examples:
        Given a file "story.txt" containing:
            Hello world
            Python is great

        count_words_in_file("story.txt") -> 5
    """
    count = 0
    with open(filepath, "r") as f:
        for line in f:
            count += len(line.split())
    return count


# === Exercise 2: Write List to File ===

def write_lines_to_file(filepath, lines):
    """Write a list of strings to a file, one per line.

    Each string should be followed by a newline character.
    Use a context manager.

    Args:
        filepath: Path to the output file.
        lines: List of strings to write.

    Returns:
        int: The number of lines written.

    Examples:
        write_lines_to_file("out.txt", ["alpha", "beta", "gamma"])
        -> 3
        # out.txt contains:
        # alpha
        # beta
        # gamma
    """
    with open(filepath, "w") as f:
        for line in lines:
            f.write(line + "\n")
    return len(lines)


# === Exercise 3: Parse CSV to Dictionaries ===

def parse_csv_to_dicts(filepath):
    """Read a CSV file and return a list of dictionaries.

    Use csv.DictReader so that each row is a dictionary whose keys are
    the column headers from the first row.

    Args:
        filepath: Path to the CSV file.

    Returns:
        list[dict]: A list of row dictionaries.

    Examples:
        Given "people.csv":
            name,age,city
            Alice,30,NYC
            Bob,25,LA

        parse_csv_to_dicts("people.csv")
        -> [
            {"name": "Alice", "age": "30", "city": "NYC"},
            {"name": "Bob", "age": "25", "city": "LA"},
        ]
    """
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


# === Exercise 4: Read and Write JSON ===

def merge_json_files(file_a, file_b, output_file):
    """Read two JSON files containing dictionaries and merge them.

    Keys from file_b overwrite keys from file_a when they overlap.
    Write the merged dictionary to output_file with indent=2.

    Args:
        file_a: Path to first JSON file.
        file_b: Path to second JSON file.
        output_file: Path to write the merged result.

    Returns:
        dict: The merged dictionary.

    Examples:
        file_a contains: {"a": 1, "b": 2}
        file_b contains: {"b": 3, "c": 4}

        merge_json_files("a.json", "b.json", "merged.json")
        -> {"a": 1, "b": 3, "c": 4}
        # merged.json is written with indent=2
    """
    with open(file_a, "r") as f:
        data_a = json.load(f)

    with open(file_b, "r") as f:
        data_b = json.load(f)

    merged = {**data_a, **data_b}

    with open(output_file, "w") as f:
        json.dump(merged, f, indent=2)

    return merged


# === Exercise 5: Find Files by Extension ===

def find_files_by_extension(directory, extension):
    """Find all files with the given extension in a directory tree.

    Search recursively through all subdirectories.
    Use pathlib for path operations.

    Args:
        directory: Root directory to search (string or Path).
        extension: File extension including the dot (e.g., ".py").

    Returns:
        list[str]: Sorted list of matching file paths as strings,
                   relative to the given directory.

    Examples:
        Given this directory tree:
            project/
              main.py
              utils.py
              data/
                input.csv
                config.json
              tests/
                test_main.py

        find_files_by_extension("project", ".py")
        -> ["main.py", "tests/test_main.py", "utils.py"]

        find_files_by_extension("project", ".csv")
        -> ["data/input.csv"]
    """
    root = Path(directory)
    pattern = f"**/*{extension}"
    matches = [
        str(p.relative_to(root))
        for p in root.glob(pattern)
        if p.is_file()
    ]
    return sorted(matches)
