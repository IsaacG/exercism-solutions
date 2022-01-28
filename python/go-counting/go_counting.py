BLACK = 'B'
WHITE = 'W'
NONE = ' '
DIRECTONS =  {(0, 1), (0, -1), (1, 0), (-1, 0)}
STONES = {BLACK, WHITE}
OWNERS = {BLACK, WHITE, NONE}

class Board:
  """Count territories of each player in a Go game

  Args:
    board (list[str]): A two-dimensional Go board
  """

  def __init__(self, board):
    self.board = board

  @property
  def x(self):
    return len(self.board[0])

  @property
  def y(self):
    return len(self.board)

  def neighbors(self, x, y):
    return set((x + i, y + j) for (i, j) in DIRECTONS
            if self.is_valid(x + i, y + j))

  def is_valid(self, x, y):
    return 0 <= y < self.y and 0 <= x < self.x

  def get(self, x, y):
    return self.board[y][x]

  def territory(self, x, y):
    """Find the owner and the territories given a coordinate on
       the board

    Args:
      x (int): Column on the board
      y (int): Row on the board

    Returns:
      (str, set): A tuple, the first element being the owner
            of that area.  One of "W", "B", "".  The
            second being a set of coordinates, representing
            the owner's territories.
    """
    if not self.is_valid(x, y):
      raise ValueError('Invalid coordinate')

    # Return early when pointing to a stone.
    if self.get(x, y) in STONES:
      return NONE, set()

    # Owner is not yet known.
    owner = None
    # We handle the first square prior to the loop.
    checked = set([(x, y)])
    terr = set([(x, y)])
    # Seed with the neighboring squares to check.
    to_check = set()
    to_check.update(self.neighbors(x, y))

    while to_check:
      # Pick a random square.
      (x, y) = to_check.pop()
      checked.add((x, y))

      if self.get(x, y) == NONE:
        # Add new unchecked squares.
        terr.add((x, y))
        to_check.update(self.neighbors(x, y) - checked)
      else: # ie self.get(x, y) in STONES
        # Set the owner, either to a color or to NONE as needed.
        if not owner:
          owner = self.get(x, y)
        elif owner != self.get(x, y):
          owner = NONE

    return owner or NONE, terr

  def territories(self):
    """Find the owners and the territories of the whole board

    Args:
      none

    Returns:
      dict(str, set): A dictionary whose key being the owner
            , i.e. "W", "B", "".  The value being a set
            of coordinates owned by the owner.
    """
    # Cover every empty square.
    empties = set((x, y) for x in range(self.x) for y in range(self.y)
                  if self.get(x, y) == NONE)
    all_t = {BLACK: set(), WHITE: set(), NONE: set()}
    while empties:
      x, y = empties.pop()
      # Find the owner and territory of that square.
      c, t = self.territory(x, y)
      empties.difference_update(t)
      all_t[c].update(t)
    return all_t


# vim:ts=2:sw=2:expandtab
