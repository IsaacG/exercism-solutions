"""Build a chain of dominoes."""
from __future__ import annotations
from typing import Generator, Optional


class Domino(tuple):
    """Domino tile."""

    def orientations(self) -> list[Domino]:
        """Return all possible Domino orientations."""
        return [self, Domino(reversed(self))]

    def can_connect(self, prior: Optional[int]) -> bool:
        """Return if this Domino can connect to prior."""
        return prior is None or prior == self[0]


def select(dominoes: list[Domino]) -> Generator[tuple[Domino, list[Domino]], None, None]:
    """Generate tuples of a start Domino and the rest."""
    for one in set(dominoes):
        rest = dominoes.copy()
        rest.remove(one)
        yield one, rest


def build_line(dominoes: list[Domino], prior: Optional[int]) -> Generator[list[Domino], None, None]:
    """Return all possible lines of a set of dominoes."""
    if not dominoes:
        yield []
        return

    # Collapse repeat pieces since it doesn't matter which we start with.
    for start, rest in select(dominoes):
        # Try using the piece in both orientations.
        for domino in start.orientations():
            if not domino.can_connect(prior):
                continue
            # Check if the rest of the dominos form a line with this piece.
            for candidate in build_line(rest, prior=domino[1]):
                if candidate is not None:
                    yield [domino] + candidate


def can_chain(dominoes: list[Domino]) -> Optional[list[Domino]]:
    """Return a circular chain of linked dominos."""
    # Special case the empty list.
    if not dominoes:
        return dominoes
    # Check every line and return the first that loops around.
    for chain in build_line([Domino(d) for d in dominoes], None):
        if chain[0][0] == chain[-1][-1]:
            return chain
    return None
