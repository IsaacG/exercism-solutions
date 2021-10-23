"""Rotational cipher."""

import string

LEN_ALPHA = len(string.ascii_uppercase)
CHAR_RANGES = (
    (string.ascii_lowercase, ord(string.ascii_lowercase[0])),
    (string.ascii_uppercase, ord(string.ascii_uppercase[0])),
)


def rotate(text: str, key: int) -> str:
    """Rotate a string."""
    return ''.join(_add(t, key) for t in text)


def _add(char: str, key: int) -> str:
    """Rotate one character."""
    for chars, start in CHAR_RANGES:
        if char in chars:
            return chr((ord(char) + key - start) % LEN_ALPHA + start)
    else:
        # Non-alpha characters are unchanged.
        return char
