"""Compute points for a game of darts."""
import math

BANDS = [(1, 10), (5, 5), (10, 1), (math.inf, 0)]

def score(x: int, y: int) -> int:
    """Return the score for a throw."""
    distance = math.sqrt(x * x + y * y)
    for band, points in BANDS:
        if distance <= band:
            return points
    raise RuntimeError
