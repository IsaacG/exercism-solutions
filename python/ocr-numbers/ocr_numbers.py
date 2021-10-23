"""OCR Numbers."""

# Numbers, as printed.
NUMBERS = """\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
                              
"""

# Map "display" value to int value.
DIGITS = {
    tuple(
        line[i * 3:(i + 1) * 3]
        for line in NUMBERS.splitlines()
    ): str(i)
    for i in range(10)
}


def convert(input_grid: list[str]) -> str:
    """Return the "string" value for "display grid"."""
    # Check dimensions are well formed.
    if len(input_grid) % 4 != 0:
        raise ValueError("Input must have 4n lines.")
    if any(len(line) % 3 != 0 for line in input_grid):
        raise ValueError("Input lines must have 3n chars.")

    output = []
    # Process grind one "line" of text at a time.
    for line_offset in range(0, len(input_grid), 4):
        line_len = len(input_grid[line_offset])
        # Break the "line" into 3x4 blocks.
        blocks = [
            tuple(
                line[i * 3:(i + 1) * 3]
                for line in input_grid[line_offset:line_offset + 4]
            )
            for i in range(line_len // 3)
        ]
        # Look up blocks in the mapping.
        vals = [DIGITS.get(block, "?") for block in blocks]
        output.append("".join(vals))
    return ",".join(output)


convert([" _ ", "| |", "|_|", "   "])
