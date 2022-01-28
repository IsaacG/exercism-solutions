"""Find products that are palindromes and fetch the largest/smallest."""

from typing import Callable, Optional

Result = tuple[Optional[int], set[tuple[int, int]]]

def is_palindrome(num: int) -> bool:
    """Return if a number is a palindrome."""
    return str(num) == str(num)[::-1]


def cmp_palindrome(max_factor: int, min_factor: int, cmp: Callable[[int, int], bool]) -> Result:
    """Return the $cmp where $cmp is a largest/smallest test."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    factors: set[tuple[int, int]] = set()
    product = None
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if product and cmp(i * j, product):
                continue
            if not is_palindrome(i * j):
                continue
            if i * j != product:
                factors.clear()
                product = i * j
            factors.add((i, j))

    if product is None:
        return product, set()
    return product, factors


def largest(max_factor: int, min_factor: int) -> Result:
    """Return the smallest palindrome product and its factors."""
    return cmp_palindrome(max_factor, min_factor, lambda x, y: x < y)


def smallest(max_factor: int, min_factor: int) -> Result:
    """Return the smallest palindrome product and its factors."""
    return cmp_palindrome(max_factor, min_factor, lambda x, y: x > y)
