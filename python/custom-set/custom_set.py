"""Reimplement the set class."""

from __future__ import annotations


class CustomSet:
    """Custom set class using a list."""

    def __init__(self, elements=None):
        """Initialize the set."""
        self._data = list(elements or [])

    def isempty(self) -> bool:
        """Return if the set is empty."""
        return not self._data

    def __contains__(self, element) -> bool:
        """Return if an element is in this set."""
        return element in self._data

    def issubset(self, other) -> bool:
        """Return if this set is a subset of other."""
        return all(element in other for element in self)

    def isdisjoint(self, other) -> bool:
        """Return if this set is a disjoint with other."""
        return not any(element in self for element in other)

    def __eq__(self, other) -> bool:
        """Return if this set has the same elements as other."""
        return self.issubset(other) and other.issubset(self)

    def add(self, element) -> None:
        """Add an element to this set."""
        if element not in self._data:
            self._data.append(element)

    def intersection(self, other) -> CustomSet:
        """Return a CustomSet with elements in both this set and other."""
        return CustomSet(element for element in other if element in self)

    def __sub__(self, other) -> CustomSet:
        """Return a CustomSet with elements in this set but not in other."""
        return CustomSet(element for element in self if element not in other)

    def __add__(self, other) -> CustomSet:
        """Return a CustomSet with elements in either this set or other."""
        result = CustomSet(self)
        for element in other:
            result.add(element)
        return result

    def __iter__(self):
        """Return an element generator."""
        return iter(self._data)
