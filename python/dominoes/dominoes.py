"""Build a chain of dominoes."""
from typing import Generator, Optional

Domino = tuple[int, int]


def build_line(dominoes: list[Domino], prior: Optional[int]) -> Generator[list[Domino], None, None]:
    """Return all possible lines of a set of dominoes."""
    if not dominoes:
        yield []
        return

    # Collapse repeat pieces since it doesn't matter which we start with.
    for start in set(dominoes):
        rest = dominoes.copy()
        rest.remove(start)
        # Try using the piece in both orientations.
        for domino in (start, (start[1], start[0])):
            # Check if this piece is valid here on the line.
            if prior is not None and domino[0] != prior:
                continue
            # Check if the rest of the dominos form a line with this piece.
            for candidate in build_line(rest, domino[1]):
                if candidate is not None:
                    yield [domino] + candidate


def can_chain(dominoes: list[Domino]) -> Optional[list[Domino]]:
    """Return a circular chain of linked dominos."""
    # Special case the empty list.
    if not dominoes:
        return dominoes
    # Check every line and return the first that loops around.
    for chain in build_line(dominoes, None):
        if chain[0][0] == chain[-1][-1]:
            return chain
    return None
