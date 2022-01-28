"""Transpose a block of text."""

def transpose(lines: str) -> str:
    """Transpose a string."""
    if not lines:
        return ""

    # Pad lines with spaces so that upper lines are as long as any following lines.
    # Convert:
    #   "A"
    #   "BBB"
    # into:
    #   "A  "
    #   "BBB"
    width = 0
    space_padded = []
    for row in reversed(lines.splitlines()):
        width = max(len(row), width)
        space_padded.append(row.ljust(width))
    space_padded.reverse()

    # Empty-pad rows so all rows have the same number of elements.
    # Convert:
    #   "AAA"
    #   "B"
    # into:
    #   ["A", "A", "A"]
    #   ["B",  "",  ""]
    padded = []
    for row in space_padded:
        padded.append(list(row) + [""] * (width - len(row)))

    # Transpose the data which now has the same number of elements on every line.
    return "\n".join(
        "".join(padded[y][x] for y in range(len(padded)))
        for x in range(width)
    )
