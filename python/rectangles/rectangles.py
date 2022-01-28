"""Rectangles Parsing."""

import itertools


def rectangles(strings: list[str]) -> int:
    """Count all rectangles in a diagram."""
    # Map coordinates to chars.
    elements = {
        (x, y): char
        for y, line in enumerate(strings) for x, char in enumerate(line)
        if char in "+-|"
    }
    # Build a set of corners, horizontal and vertical pieces.
    corners = {point for point, char in elements.items() if char == "+"}
    horiz = {point for point, char in elements.items() if char == "-"} | corners
    vert = {point for point, char in elements.items() if char == "|"} | corners

    count = 0
    # For every corner pair, see if it forms a rectangle.
    for (x0, y0), (x1, y1) in itertools.product(corners, repeat=2):
        # Only count pairs with (x0, y0) < (x1, y1)
        if x0 >= x1 or y0 >= y1:
            continue
        # Check the top right, bottom left corners.
        if (x0, y1) not in corners or (x1, y0) not in corners:
            continue
        # Check the top and bottom sides.
        if any((x, y0) not in horiz for x in range(x0, x1 + 1)):
            continue
        if any((x, y1) not in horiz for x in range(x0, x1 + 1)):
            continue
        # Check the left and right.
        if any((x0, y) not in vert for y in range(y0, y1 + 1)):
            continue
        if any((x1, y) not in vert for y in range(y0, y1 + 1)):
            continue
        count += 1
    return count
