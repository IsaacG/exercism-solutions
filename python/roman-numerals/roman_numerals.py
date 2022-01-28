"""Convert an int to a Roman numeral."""


# The 10's, 5's and 1's position chars for 1, 10, 100, 1000.
DIGIT_CHARS = ["XVI", "CLX", "MDC", "??M"]


def roman(number: int) -> str:
    """Return the Roman numeral for a number."""
    # Generate a mapping from numeric value to Roman numeral.
    mapping = []
    for position in range(len(DIGIT_CHARS) - 1, -1, -1):
        # Values: 1000, 100, 10, 1
        scale = 10 ** position
        chars = DIGIT_CHARS[position]
        # This might be: (9, IX) or (90, XC)
        mapping.append((9 * scale, chars[2] + chars[0]))
        # This might be: (5, V) or (50, D)
        mapping.append((5 * scale, chars[1]))
        # This might be: (4, IV) or (40, XD)
        mapping.append((4 * scale, chars[2] + chars[1]))
        mapping.append((1 * scale, chars[2]))

    out = ""
    for num, numerals in mapping:
        while number >= num:
            out += numerals
            number -= num
    return out
