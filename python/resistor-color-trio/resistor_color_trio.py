"""Parse resistor colors."""

COLORS = "black brown red orange yellow green blue violet grey white".split()


def label(colors: list[str]) -> str:
    """Return the value of a resistor color."""
    val = 0
    for color in colors[:2]:
        val = val * 10 + COLORS.index(color)
    val *= 10 ** COLORS.index(colors[2])
    if val % 1000 == 0:
        return f"{val // 1000} kiloohms"
    return f"{val} ohms"
