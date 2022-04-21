"""Create Aliens for Ellen."""


class Alien:
    """An alien."""

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Initialize."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def is_alive(self) -> bool:
        """Return if the Alien is alive."""
        return self.health > 0

    def hit(self) -> None:
        """Reduce Alien health."""
        # With bounds checks:
        # self.health = max(0, self.health - 1)
        self.health -= 1

    def teleport(self, x_coordinate: int, y_coordinate: int) -> None:
        """Change the Alien position."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other: object) -> None:
        """Detect collision."""


def new_aliens_collection(positions: list[tuple[int, int]]) -> list[Alien]:
    """Return a list of Aliens for a given list of positions."""
    return [Alien(*coordinate) for coordinate in positions]
