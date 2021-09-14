"""Queen Attack."""
from __future__ import annotations

class Queen:
    """A cartesian coordinate."""

    def __init__(self, row: int, column: int):
        """Initialize."""
        if 0 <= row < 8 and 0 <= column < 8:
            self.position = (row, column)
        else:
            raise ValueError("Invalid coordinate.")

    def can_attack(self, other: Queen) -> bool:
        """Return if two queens can attack."""
        if self.position == other.position:
            raise ValueError("Two pieces cannot occupy the same position.")
        delta = {abs(self.position[i] - other.position[i]) for i in (0, 1)}
        # `0 in delta` indicates the queens are on the same row or column.
        # `len(delta) == 1` indicates the x and y delta are the same, ie on a diagonal.
        return 0 in delta or len(delta) == 1

    def print(self):
        """Print the coordinate."""
        print(self.position)
