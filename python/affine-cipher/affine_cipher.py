"""Affine Cipher encoding and decoding."""

import math
import string
import textwrap

from typing import Callable

LOWER = string.ascii_lowercase
ORD_A = ord(LOWER[0])
LEN = len(LOWER)


def char_op(char: str, operation: Callable[[int], int]) -> str:
    """Perform an operation() on a character as an offset."""
    assert char.isalnum()
    if char.isnumeric():
        return char
    # Convert to an offset.
    offset = ord(char) - ORD_A
    # Call operation() and convert back to a chr().
    return chr((operation(offset) + LEN) % LEN + ORD_A)


def encode(plain_text: str, a: int, b: int) -> str:
    """Encode a string using an affine cipher."""
    # Check for shared factors.
    if math.gcd(a, LEN) != 1:
        raise ValueError(f"a ({a}) and m ({len(LOWER)}) must be coprime")

    encoded = "".join(
        char_op(char, lambda c: a * c + b)
        for char in plain_text.lower()
        if char.isalnum()
    )
    # Apply chunking.
    return " ".join(textwrap.wrap(encoded, width=5))


def mmi(num: int) -> int:
    """Compute the MMI for a number using brute force."""
    for i in range(1, LEN):
        if (num * i) % LEN == 1:
            return i
    raise ValueError(f"Could not find MMI for {num}")


def decode(ciphered_text, a, b):
    """Decode a string using an affine cipher."""
    # Check for shared factors.
    if math.gcd(a, LEN) != 1:
        raise ValueError(f"a ({a}) and m ({len(LOWER)}) must be coprime")

    m = mmi(a)

    return "".join(
        char_op(char, lambda c: m * (c - b))
        for char in ciphered_text.lower()
        if char.isalnum()
    )
