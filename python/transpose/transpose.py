"""Transpose a block of text."""

def transpose(lines: str) -> str:
    """Transpose a string.

    First, lines need to be space padded such that every line is as long, or longer,
    than the following line. Input:
        "1"
        "333"
        "22"
    becomes:
        "1  "
        "333"
        "22"
    Next, convert each line into a list as long as the first line, padding with "",
    to aid in matrix transposing (to avoid any IndexErrors).
    """
    # Input with space padding so line length never increases.
    space_padded: list[str] = []
    width = 0
    for row in reversed(lines.splitlines()):
        width = max(len(row), width)
        space_padded.append(row.ljust(width))
    space_padded.reverse()

    # Build a "matrix" which is rectangular to aid in lookups.
    input_matrix: list[list[str]] = []
    for row in space_padded:
        input_matrix.append(list(row) + [""] * (width - len(row)))

    # Transpose the data which now has the same number of elements on every line.
    return "\n".join(
        "".join(input_matrix[y][x] for y in range(len(input_matrix)))
        for x in range(width)
    )
