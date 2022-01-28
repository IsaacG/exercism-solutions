"""Base conversion."""

def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a number between bases."""
    for val, name in [(input_base, "input"), (output_base, "output")]:
        if val < 2:
            raise ValueError(f"{name} base must be >= 2")

    # Parse the input.
    val = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        val *= input_base
        val += digit

    # Generate the output.
    out = []
    while val:
        out.append(val % output_base)
        val //= output_base

    return list(reversed(out)) or [0]
