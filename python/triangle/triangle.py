def is_valid(sides: list[float]) -> bool:
    """Return if a triangle is valid."""
    return max(sides) * 2 < sum(sides) and all(sides)


def equilateral(sides: list[float]) -> bool:
    """Return if a triangle is an equilateral triangle."""
    return is_valid(sides) and len(set(sides)) == 1


def isosceles(sides: list[float]) -> bool:
    """Return if a triangle is an isosceles triangle."""
    return is_valid(sides) and len(set(sides)) < 3


def scalene(sides: list[float]) -> bool:
    """Return if a triangle is a scalene triangle."""
    return is_valid(sides) and len(set(sides)) == 3
