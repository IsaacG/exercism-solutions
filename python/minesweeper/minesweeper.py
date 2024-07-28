"""Minesweeper."""

ADJACENT = [complex(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y]


def annotate(minefield: list[str]) -> list[str]:
    """Annotate a minefield."""
    height = len(minefield)
    width = len(minefield[0]) if minefield else 0

    if not all(len(row) == width for row in minefield):
        raise ValueError("The board is invalid with current input.")

    mines = set()
    for y, line in enumerate(minefield):
        for x, val in enumerate(line):
            if val == "*":
                mines.add(complex(x, y))
            elif val != " ":
                raise ValueError("The board is invalid with current input.")

    def cell_value(point: complex) -> str:
        """Return the value for one square."""
        if point in mines:
            return "*"
        count = sum(point + offset in mines for offset in ADJACENT)
        return str(count) if count else " "

    return [
        "".join(cell_value(complex(x, y)) for x in range(width))
        for y in range(height)
    ]
