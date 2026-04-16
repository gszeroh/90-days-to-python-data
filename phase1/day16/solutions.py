"""
Day 16: OOP — Advanced (Solutions)
"""

import bisect
from dataclasses import dataclass, field


# === Exercise 1: Money Class with Operator Overloading ===

class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def _check_currency(self, other):
        if not isinstance(other, Money):
            raise TypeError(f"Cannot operate with {type(other).__name__}")
        if self.currency != other.currency:
            raise ValueError(
                f"Currency mismatch: {self.currency} vs {other.currency}"
            )

    def __add__(self, other):
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Cannot multiply Money by {type(scalar).__name__}")
        return Money(self.amount * scalar, self.currency)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        self._check_currency(other)
        return self.amount < other.amount

    def __le__(self, other):
        self._check_currency(other)
        return self.amount <= other.amount

    def __hash__(self):
        return hash((self.amount, self.currency))

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    def __str__(self):
        symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
        symbol = symbols.get(self.currency, self.currency + " ")
        return f"{symbol}{self.amount:.2f}"


# === Exercise 2: Temperature with Properties ===

class TemperatureConverter:
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius=0):
        self.celsius = celsius  # uses the setter for validation

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < self.ABSOLUTE_ZERO:
            raise ValueError(
                f"Temperature {value}°C is below absolute zero ({self.ABSOLUTE_ZERO}°C)"
            )
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273.15

    def __repr__(self):
        return (
            f"TemperatureConverter("
            f"{self.celsius:.2f}°C / "
            f"{self.fahrenheit:.2f}°F / "
            f"{self.kelvin:.2f}K)"
        )


# === Exercise 3: Playlist as a Dataclass ===

@dataclass
class Song:
    title: str
    artist: str
    duration_seconds: int


@dataclass
class Playlist:
    name: str
    songs: list = field(default_factory=list)

    def add_song(self, song):
        self.songs.append(song)

    @property
    def total_duration(self):
        return sum(s.duration_seconds for s in self.songs)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs


# === Exercise 4: Custom Container — SortedList ===

class SortedList:
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []

    def add(self, value):
        bisect.insort(self._items, value)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __contains__(self, value):
        i = bisect.bisect_left(self._items, value)
        return i < len(self._items) and self._items[i] == value

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"SortedList({self._items})"

    def __add__(self, other):
        return SortedList(self._items + list(other))


# === Exercise 5: Composition — DataPipeline ===

class UpperTransformer:
    def transform(self, data):
        return [item.upper() if isinstance(item, str) else item for item in data]


class FilterTransformer:
    def __init__(self, predicate):
        self.predicate = predicate

    def transform(self, data):
        return [item for item in data if self.predicate(item)]


class MapTransformer:
    def __init__(self, func):
        self.func = func

    def transform(self, data):
        return [self.func(item) for item in data]


class DataPipeline:
    def __init__(self, transformers=None):
        self.transformers = list(transformers) if transformers else []

    def add_transformer(self, transformer):
        self.transformers.append(transformer)

    def process(self, data):
        result = data
        for transformer in self.transformers:
            result = transformer.transform(result)
        return result


# === Verification ===

if __name__ == "__main__":
    # Exercise 1
    print("=== Exercise 1: Money ===")
    m1 = Money(10.50)
    m2 = Money(5.25)
    print(f"m1 = {m1}")
    print(f"m2 = {m2}")
    print(f"m1 + m2 = {m1 + m2}")
    print(f"m1 - m2 = {m1 - m2}")
    print(f"m1 * 3 = {m1 * 3}")
    print(f"m1 == Money(10.50): {m1 == Money(10.50)}")
    print(f"m1 < m2: {m1 < m2}")
    print(f"m1 in set: {m1 in {m1, m2}}")
    try:
        m1 + Money(5, "EUR")
    except ValueError as e:
        print(f"Currency error: {e}")

    # Exercise 2
    print("\n=== Exercise 2: Temperature ===")
    t = TemperatureConverter(100)
    print(t)
    t.fahrenheit = 32
    print(f"After setting 32°F: {t}")
    t.kelvin = 0
    print(f"After setting 0K: {t}")
    try:
        t.celsius = -300
    except ValueError as e:
        print(f"Validation: {e}")

    # Exercise 3
    print("\n=== Exercise 3: Playlist ===")
    s1 = Song("Bohemian Rhapsody", "Queen", 354)
    s2 = Song("Stairway to Heaven", "Led Zeppelin", 482)
    s3 = Song("Hotel California", "Eagles", 391)
    pl = Playlist("Classic Rock")
    pl.add_song(s1)
    pl.add_song(s2)
    pl.add_song(s3)
    print(f"Playlist: {pl.name}, {len(pl)} songs")
    print(f"Total duration: {pl.total_duration}s")
    print(f"First song: {pl[0]}")
    print(f"s1 in playlist: {s1 in pl}")

    # Exercise 4
    print("\n=== Exercise 4: SortedList ===")
    sl = SortedList([5, 1, 3])
    sl.add(2)
    sl.add(4)
    print(f"SortedList: {sl}")
    print(f"len: {len(sl)}")
    print(f"sl[2]: {sl[2]}")
    print(f"3 in sl: {3 in sl}")
    sl2 = SortedList([6, 0])
    merged = sl + sl2
    print(f"Merged: {merged}")

    # Exercise 5
    print("\n=== Exercise 5: DataPipeline ===")
    pipeline = DataPipeline([
        FilterTransformer(lambda x: len(x) > 3),
        UpperTransformer(),
        MapTransformer(lambda x: x + "!"),
    ])
    result = pipeline.process(["hi", "hello", "hey", "world", "go"])
    print(f"Pipeline result: {result}")

    pipeline2 = DataPipeline()
    pipeline2.add_transformer(MapTransformer(lambda x: x * 2))
    pipeline2.add_transformer(FilterTransformer(lambda x: x > 5))
    print(f"Numeric pipeline: {pipeline2.process([1, 2, 3, 4, 5])}")
