"""Connect where players try to connect from one edge to the other on a hex board."""


# Six neighboring directions on a hex axial grid.
OFFSETS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1)]


class ConnectGame:
    """Connect logic."""

    def __init__(self, board: str):
        """Initialize a board."""
        board = board.replace(" ", "")
        lines = board.splitlines()
        # Set of player's pieces, encoded using hex axial coordinates.
        self.pieces = {
            player: {
                (q, r)
                for r, line in enumerate(lines)
                for q, piece in enumerate(line)
                if piece == player
            }
            for player in "XO"
        }
        # Far edge location.
        self.max = (len(lines[0]) - 1, len(lines) - 1)

    @staticmethod
    def neighbors(piece: tuple[int, int]) -> list[tuple[int, int]]:
        """Return all possible neighbor coordinates for a piece."""
        p_q, p_r = piece
        return [(p_q + dq, p_r + dr) for dq, dr in OFFSETS]

    def get_winner(self) -> str:
        """Return the winner for the current board, if any."""
        # X plays along the horizonal q-axis and ) plays the r-axis.
        for player, axis in [("O", 1), ("X", 0)]:
            pieces = self.pieces[player]
            # Start with any piece on the near edge.
            start = next((p for p in pieces if p[axis] == 0), None)
            if start is None:
                continue
            # Use Dijkstra's to follow pieces across the board.
            todo = {start}
            done = set()
            while todo:
                cur = todo.pop()
                done.add(cur)
                # If a piece reaches the far edge, the player wins.
                if cur[axis] == self.max[axis]:
                    return player
                for coord in self.neighbors(cur):
                    if coord not in pieces:
                        continue
                    if coord in done:
                        continue
                    todo.add(coord)
        return ""
