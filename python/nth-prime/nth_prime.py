"""Compute primes."""

import math
from typing import Generator

def primes() -> Generator[int, None, None]:
    """Prime number generator."""
    # Yield the only even prime then only check odd values.
    yield 2
    found: list[int] = []
    cur = 1
    while True:
        # Test odd values: 3, 5, ...
        cur += 2
        is_prime = True
        # Limit prime checks to sqrt(value)
        limit = math.sqrt(cur)
        for factor in found:
            # If there are no factors <= sqrt(val) then val is prime.
            if factor > limit:
                break
            if cur % factor == 0:
                is_prime = False
                break
        if is_prime:
            found.append(cur)
            yield cur


def prime(number: int) -> int:
    """Return the n'th prime."""
    if number <= 0:
        raise ValueError("there_is_no_zeroth_prime")
    gen = primes()
    return [next(gen) for _ in range(number)][-1]
