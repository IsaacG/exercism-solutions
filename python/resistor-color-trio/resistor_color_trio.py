"""Parse resistor colors."""

COLORS = "black brown red orange yellow green blue violet grey white".split()
UNITS = ["ohms", "kiloohms", "megaohms", "gigaohms"]


def label(colors: list[str]) -> str:
    """Return the value of a resistor color."""
    val = 0
    for color in colors[:2]:
        val = val * 10 + COLORS.index(color)
    val *= 10 ** COLORS.index(colors[2])

    power = 0
    while val > 1000 and not val % 1000:
        val //= 1000
        power += 1
    return f"{val} {UNITS[power]}"
