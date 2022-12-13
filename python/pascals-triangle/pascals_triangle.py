"""Solve Pascal's Triangle."""


def rows(row_count: int) -> list[list[int]]:
    """Return Pascal's Triangle using recursion (slow)."""
    if row_count < 0:
        raise ValueError("count must be a counting number")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    prior = rows(row_count - 1)
    return prior + [[1] + [a + b for a, b in zip(prior[-1][:-1], prior[-1][1:])] + [1]]


def fast_rows(row_count: int) -> list[list[int]]:
    """Return Pascal's Triangle efficiently."""
    out = [[1]]
    for _ in range(row_count - 1):
        out.append([1] + [a + b for a, b in zip(out[-1][:-1], out[-1][1:])] + [1])
    return out[:row_count]
