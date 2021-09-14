"""Convert a string matrix to an object with row- and column-wise access."""


class Matrix:
    """A matrix of integers."""

    def __init__(self, data: str):
        """Initialize the matrix."""
        self.rows = [[int(element) for element in row.split()] for row in data.splitlines()]

    def row(self, index: int) -> list[int]:
        """Return one matrix row."""
        return self.rows[index - 1].copy()

    def column(self, index: int) -> list[int]:
        """Return one matrix column."""
        return [row[index - 1] for row in self.rows]
