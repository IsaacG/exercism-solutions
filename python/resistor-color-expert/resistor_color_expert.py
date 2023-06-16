"""Parse resistor colors."""

COLORS = "black brown red orange yellow green blue violet grey white".split()
TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}
UNITS = ["ohms", "kiloohms", "megaohms"]


def resistor_label(colors: list[str]) -> str:
    """Return the value of a resistor color."""
    # Unpack or set up variables.
    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors, COLORS[0], None

    # Add the bands, apply the multiplier.
    val = 0.0
    for value in values:
        val = val * 10 + COLORS.index(value)
    val *= 10 ** COLORS.index(multiplier)

    # Shift numbers over to get the proper prefix.
    power = 0
    while val > 1000:
        val /= 1000
        power += 1

    # Add a tolerance, if one is supplied.
    result = f"{val:n} {UNITS[power]}"
    if tolerance:
        result += f" ±{TOLERANCES[tolerance]}%"

    return result
