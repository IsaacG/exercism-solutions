"""Word Search Puzzle."""

import dataclasses
from typing import Optional

@dataclasses.dataclass
class Point:
    """Cartesian coordinate."""
    x: int
    y: int


DIRECTIONS = (
    (0, 1),  # Horizontal
    (1, 0),  # Vertical
    (1, 1),  # Diagonal, down right
    (-1, 1)  # Diagonal, down left
)


class WordSearch:
    """Word Search Puzzle."""

    def __init__(self, puzzle: list[str]):
        """Initialize."""
        self.board = puzzle.copy()
        self.height = len(puzzle)
        self.width = len(puzzle[0])

    def search(self, word: str) -> Optional[tuple[Point, Point]]:
        """Search for a word in the puzzle."""
        # Check every point as a potential match. Return the first match.
        for y in range(self.height):
            for x in range(self.width):
                if points := self.test(x, y, word):
                    start, end = points
                    return (Point(*start), Point(*end))
        return None

    def test(self, x: int, y: int, word: str) -> Optional[tuple[tuple[int, int], tuple[int, int]]]:
        """Test to see if a word starts/ends at a given point."""
        wlen = len(word) - 1
        # Check in all four directions.
        for x_mod, y_mod in DIRECTIONS:
            # Compute the end from this given point.
            end_x, end_y = x + x_mod * wlen, y + y_mod * wlen
            # Check if the end point is on the board.
            if not (0 <= end_x < self.width and 0 <= end_y < self.height):
                continue
            # Build the string between this start and end point.
            block = "".join(self.board[y + y_mod * i][x + x_mod * i] for i in range(len(word)))
            # Check in both directions.
            if word == block:
                return ((x, y), (end_x, end_y))
            if word == "".join(reversed(block)):
                return ((end_x, end_y), (x, y))
        return None
