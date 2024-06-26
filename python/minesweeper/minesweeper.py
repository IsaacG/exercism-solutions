"""Minesweeper."""

from typing import Generator


def neighbors(cell: complex) -> Generator[complex, None, None]:
    """Yield all eight neighboring cells."""
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if offset := x + y * 1j:
                yield cell + offset


class Minefield:
    """Minefield helper."""

    def __init__(self, data: list[str]):
        """Initialize."""
        self.height = len(data)
        self.width = len(data[0]) if data else 0

        if not all(len(row) == self.width for row in data):
            raise ValueError("The board is invalid with current input.")

        self.data = {}
        for y, line in enumerate(data):
            for x, val in enumerate(line):
                self.data[x + y * 1j] = val
        if not all(v in (" ", "*") for v in self.data.values()):
            raise ValueError("The board is invalid with current input.")

    def val(self, x: int, y: int) -> str:
        """Return the value for one square."""
        cur = x + y * 1j
        if self.data[cur] == "*":
            return "*"
        count = sum(self.data.get(neighbor, "") == "*" for neighbor in neighbors(cur))
        return str(count) if count else " "

    def convert(self) -> list[str]:
        """Convert the minefield."""
        return [
            "".join(self.val(x, y) for x in range(self.width))
            for y in range(self.height)
        ]


def annotate(minefield: list[str]) -> list[str]:
    """Annotate a minefield."""
    return Minefield(minefield).convert()
