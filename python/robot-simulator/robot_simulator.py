"""Robot Simulator."""

# Directions, complex polar mappings.
EAST = 1
NORTH = 1j
WEST = -1
SOUTH = -1j


class Robot:
    """A robot."""

    def __init__(self, direction: complex, x: int, y: int):
        """Initialize, mapping inputs to complex numbers."""
        self.direction = direction
        self._coord = x + y * 1j

    @property
    def coordinates(self) -> tuple[int, int]:
        """Map complex coordinates to Cartesian."""
        return (int(self._coord.real), int(self._coord.imag))

    def move(self, instructions: str) -> None:
        """Move the robot Right|Left|Advance."""
        for instruction in instructions:
            if instruction not in "RLA":
                raise ValueError(f"invalid instruction {instruction}")
            if instruction == "A":
                # Advance.
                self._coord += self.direction
            elif instruction == "R":
                # Rotate -90 deg.
                self.direction *= -1j
            elif instruction == "L":
                # Rotate 90 deg.
                self.direction *= 1j
