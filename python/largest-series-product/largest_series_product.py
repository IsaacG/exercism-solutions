"""Largest Series Product."""
import math


def largest_product(series: str, size: int) -> int:
    """Return the largest series product."""
    if size == 0:
        return 1
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if size < 0:
        raise ValueError("span must not be negative")

    numbers = [int(number) for number in series]
    return max(
        math.prod(numbers[start:start + size])
        for start in range(len(series) - size + 1)
    )
