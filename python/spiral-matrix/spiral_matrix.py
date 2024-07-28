"""Fill a NxN board with numbers 1..N^2 in a spiral pattern."""

def spiral_matrix(size: int) -> list[list[int]]:
    """Return a spiral-filled board.

    Start from the middle and spiral outwards, counting from size**2 to 1.
    At every step:
    - set the value of a cell to the current count
    - rotate right if the location to the right is not yet set
    - always advance one cell forward.
    """
    if not size:
        return []
    # Initialize
    board: dict[complex, int] = {}
    coord = 0 + 0j
    # Even vs odd spirals end in opposite directions.
    direction = -1j if size % 2 else 1j
    rotate = -1j
    # Fill the board.
    for val in range(size ** 2, 0, -1):
        board[coord] = val
        if coord + direction * rotate not in board:
            direction *= rotate
        coord += direction

    # Compute the boundaries.
    x_max = y_max = (size - 1) // 2
    x_min = y_min = -x_max
    if size % 2 == 0:
        x_max += 1
        y_min -= 1

    # Convert the dict[complex, int] to a list[list[int]]
    return [
        [board[x + y * 1j] for x in range(int(x_min), int(x_max) + 1)]
        for y in range(int(y_min), int(y_max) + 1)
    ]
