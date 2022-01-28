"""Solve an alphametics puzzle."""

import itertools
import string
from typing import Optional


def solve(puzzle: str) -> Optional[dict[str, int]]:
    """Return a puzzle solution."""
    left, right = puzzle.split(" == ")
    parts = [p.strip() for p in left.split("+")]
    letters = {l for l in puzzle if l.isalpha()}
    # Try all permutations of digits for the letters.
    for vals in itertools.permutations(string.digits, r=len(letters)):
        mapping = dict(zip(letters, vals))
        trans = str.maketrans(mapping)
        t_parts = [p.translate(trans) for p in parts]
        t_right = right.translate(trans)
        # All numbers cannot start with a 0.
        if any(p[0].startswith("0") for p in t_parts):
            continue
        if t_right.startswith("0"):
            continue
        if sum(int(p) for p in t_parts) == int(t_right):
            return {k: int(v) for k, v in mapping.items()}
    return None
