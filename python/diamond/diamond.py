"""Generate a Diamond pattern."""

import string


def rows(letter: str) -> list[str]:
    """Return a diamond pattern for a letter."""
    count = string.ascii_uppercase.index(letter)
    line_width = count * 2 + 1
    lines = []
    for offset in range(0, count + 1):
        char = string.ascii_uppercase[offset]
        center = " " * (offset * 2 - 1)
        line = center.join(char * (2 if offset else 1))
        lines.append(f"{line:^{line_width}}")

    # Mirror the top half for the bottom.
    return lines + lines[-2::-1]
