"""Compute the hamming distance."""
from functools import reduce

def reduction(count: int, strings: tuple[str, str]) -> int:
    """Reduce a list of pairs by adding 1 on differing, otherwise count doesn't change."""
    first, second = strings
    return count if first == second else count + 1


def distance(strand_a: str, strand_b: str) -> int:
    """Return the hamming distance between two strings."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths differ")
    dist = reduce(reduction, zip(strand_a, strand_b), 0)
    alt = alt_distance(strand_a, strand_b)
    assert dist == alt, f"{dist} != {alt}"
    return dist

def alt_distance(strand_a: str, strand_b: str) -> int:
    """Return the hamming distance between two strings."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths differ")
    return sum(a != b for a, b in zip(strand_a, strand_b))
