"""Generate a Diamond pattern."""

import string


def rows(letter):
    """Return a diamond pattern for a letter."""
    count = string.ascii_uppercase.index(letter)
    # Special case the first row.
    out = [" " * count + "A" + " " * count]
    for offset in range(1, count + 1):
        char = string.ascii_uppercase[offset]
        pad = count - offset
        gap = offset * 2 - 1
        # Each line has pad, char, gap, char, pad.
        line = char.join([" " * pad, " " * gap, " " * pad])
        out.append(line)

    # Mirror the top half for the bottom.
    return out + list(reversed(out[:-1]))
