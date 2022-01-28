"""Fill a NxN board with numbers 1..N^2 in a spiral pattern."""

def spiral_matrix(size: int) -> list[list[int]]:
    """Return a spiral-filled board.

    Implementation:
    * Use complex numbers as coordinates.
    * The next cell can be computed as current + direction where direction
      is one of [1, -1, 1j, -1j].
    * The direction is "rotated" 90 degrees using `direction *= 1j`.
    * The direction needs to change when either (1) the board edge is encountered
      or (2) we reach a cell which is already filled.
    """
    # Initialize
    board: dict[complex, int] = {}
    coord = 0 + 0j
    direction = 1 + 0j
    edges = {-1, size}
    # Iterate through all values needed.
    for val in range(1, size ** 2 + 1):
        board[coord] = val
        # Check if we need to change directions.
        next_coord = coord + direction
        if next_coord in board or {next_coord.real, next_coord.imag} & edges:
            direction *= 1j
        coord += direction

    # Convert the dict[complex, int] to a list[list[int]]
    return [[board[x + y * 1j] for x in range(size)] for y in range(size)]
