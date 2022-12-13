"""Solve a cage for Killer Sudoku."""
import itertools


def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    """Return possible combinations for a cage."""
    candidates = [i for i in range(1, min(target, 9) + 1) if i not in exclude]
    return [
        list(combo)
        for combo in itertools.combinations(candidates, size)
        if sum(combo) == target
    ]
