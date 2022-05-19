"""Generate a Diamond pattern."""

import string


def rows(letter: str) -> list[str]:
    """Return a diamond pattern for a letter."""
    count = string.ascii_uppercase.index(letter)
    lines = []
    for offset in range(0, count + 1):
        char = string.ascii_uppercase[offset]
        # Populate a space-filled line.
        line = [" "] * (2 * count + 1)
        # Insert the char, offset from the center.
        line[count - offset] = char
        line[offset - count - 1] = char
        lines.append("".join(line))

    # Mirror the top half for the bottom.
    return lines + lines[-2::-1]
