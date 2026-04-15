"""
Day 16: OOP — Advanced (Exercises)
Complete each exercise by replacing `pass` with your implementation.
"""

from dataclasses import dataclass, field


# === Exercise 1: Money Class with Operator Overloading ===
# Create a Money class that supports:
# - Addition of two Money objects (same currency only, raise ValueError otherwise)
# - Subtraction of two Money objects (same currency only)
# - Multiplication by a scalar (int or float)
# - Comparison operators: ==, <, <=
# - String representation: "$10.50" for USD
# - Hashing (so Money can be used in sets/dicts)

class Money:
    def __init__(self, amount, currency="USD"):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, scalar):
        pass

    def __rmul__(self, scalar):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __hash__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


# === Exercise 2: Temperature with Properties ===
# Create a Temperature class with:
# - Internal storage in Celsius
# - Properties for celsius, fahrenheit, kelvin (all with getters and setters)
# - Validation: temperature cannot go below absolute zero (-273.15°C)
# - __repr__ showing all three scales
# Conversion formulas:
#   F = C * 9/5 + 32
#   K = C + 273.15

class TemperatureConverter:
    def __init__(self, celsius=0):
        pass

    @property
    def celsius(self):
        pass

    @celsius.setter
    def celsius(self, value):
        pass

    @property
    def fahrenheit(self):
        pass

    @fahrenheit.setter
    def fahrenheit(self, value):
        pass

    @property
    def kelvin(self):
        pass

    @kelvin.setter
    def kelvin(self, value):
        pass

    def __repr__(self):
        pass


# === Exercise 3: Playlist as a Dataclass ===
# Create a Song dataclass with: title (str), artist (str), duration_seconds (int)
# Create a Playlist dataclass with: name (str), songs (list of Song, default empty)
# Playlist should support:
# - add_song(song): add a song to the playlist
# - total_duration: property returning total seconds
# - __len__: return number of songs
# - __getitem__: access songs by index
# - __contains__: check if a song is in the playlist

@dataclass
class Song:
    pass


@dataclass
class Playlist:
    pass

    def add_song(self, song):
        pass

    @property
    def total_duration(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass

    def __contains__(self, song):
        pass


# === Exercise 4: Custom Container — SortedList ===
# Create a SortedList that always keeps its elements in sorted order.
# Support:
# - add(value): insert value in the correct sorted position
# - __len__: return the number of elements
# - __getitem__: access by index
# - __contains__: membership test
# - __repr__: e.g., "SortedList([1, 3, 5, 7])"
# - __iter__: iteration support
# - __add__: merge two SortedLists into a new SortedList

class SortedList:
    def __init__(self, initial=None):
        pass

    def add(self, value):
        pass

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass

    def __contains__(self, value):
        pass

    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def __add__(self, other):
        pass


# === Exercise 5: Composition — DataPipeline ===
# Build a DataPipeline using composition (not inheritance).
# Create simple transformer classes, each with a transform(data) method:
#   - UpperTransformer: converts strings in data to uppercase
#   - FilterTransformer: filters elements by a predicate function
#   - MapTransformer: applies a function to each element
# Create DataPipeline that:
#   - Takes a list of transformer objects
#   - Has a process(data) method that runs data through each transformer in order
#   - Has an add_transformer(transformer) method

class UpperTransformer:
    def transform(self, data):
        pass


class FilterTransformer:
    def __init__(self, predicate):
        pass

    def transform(self, data):
        pass


class MapTransformer:
    def __init__(self, func):
        pass

    def transform(self, data):
        pass


class DataPipeline:
    def __init__(self, transformers=None):
        pass

    def add_transformer(self, transformer):
        pass

    def process(self, data):
        pass
