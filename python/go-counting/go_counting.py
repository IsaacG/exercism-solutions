"""Count territories on a Go board."""

BLACK = "B"
WHITE = "W"
NONE = " "
DIRECTONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}

Spots = set[tuple[int, int]]

class Board:
    """Count territories of each player in a Go game.

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: list[str]):
        pieces = {}
        for y, line in enumerate(board):
            for x, val in enumerate(line):
                pieces[(x, y)] = val
        self.board = pieces

    def neighbors(self, x: int, y: int) -> Spots:
        """Return the set of neighboring positions around a given spot."""
        return {
                (x + i, y + j) for (i, j) in DIRECTONS
                if (x + i, y + j) in self.board
        }

    def territory(self, x: int, y: int) -> tuple[str, Spots]:
        """Find the owner and the territories given a coordinate on the board."

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.    One of "W", "B", "".    The
                        second being a set of coordinates, representing
                        the owner"s territories.
        """
        if (x, y) not in self.board:
            raise ValueError("Invalid coordinate")

        if self.board[(x, y)] != NONE:
            return NONE, set()

        # Dijkstra's algorithm.
        to_check = {(x, y)}
        checked = set()
        territory = set()

        # Owner is not yet known.
        owner = None

        while to_check:
            # Pick a random square.
            (x, y) = to_check.pop()
            if (x, y) in checked:
                continue
            checked.add((x, y))

            if self.board[(x, y)] == NONE:
                # Add new unchecked squares.
                territory.add((x, y))
                to_check.update(self.neighbors(x, y))
            else: # ie self.get(x, y) in STONES
                # Set the owner, either to a color or to NONE as needed.
                if not owner:
                    owner = self.board[(x, y)]
                elif owner != self.board[(x, y)]:
                    owner = NONE

        return owner or NONE, territory

    def territories(self) -> dict[str, Spots]:
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".    The value being a set
                        of coordinates owned by the owner.
        """
        empties = {position for position, owner in self.board.items() if owner == NONE}
        terrritories: dict[str, Spots] = {BLACK: set(), WHITE: set(), NONE: set()}
        while empties:
            x, y = empties.pop()
            # Find the owner and territory of that square.
            owner, territory = self.territory(x, y)
            empties -= territory
            terrritories[owner].update(territory)
        return terrritories
