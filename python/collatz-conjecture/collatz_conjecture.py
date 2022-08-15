"""Test the Collatz Conjecture."""
import itertools


def steps(number: int) -> int:
    """Return the number of steps required to get a number to 1."""
    if number < 1:
        raise ValueError('Only positive integers are allowed')

    for step in itertools.count():
        if number == 1:
            return step
        if number % 2:
            number = number * 3 + 1
        else:
            number //= 2
    raise RuntimeError("count should not stop")
