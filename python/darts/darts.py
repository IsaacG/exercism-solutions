import math

SCORES = {1: 10, 5: 5, 10: 1}


def score(x: int, y: int) -> int:
    diag = math.sqrt(x*x + y*y)
    return next(
        (
            score for distance, score in SCORES.items()
            if diag <= distance
        ),
        0,
    )
