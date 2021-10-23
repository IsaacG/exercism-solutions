"""Solve the jug filling problem."""

class Bucket:
    """A bucket with a capacity, volume and move counter."""

    def __init__(self, capacity: int, name: str):
        """Initialize."""
        self.volume = 0
        self.capacity = capacity
        self.moves = 0
        self.name = name

    def fill_if_empty(self):
        """Fill the bucket if it is empty."""
        if self.volume == 0:
            self.volume = self.capacity
            self.moves += 1

    def empty_if_full(self):
        """Empty the bucket if it is full."""
        if self.volume == self.capacity:
            self.volume = 0
            self.moves += 1

    def transfer_to(self, other):
        """Pour water from self into another bucket."""
        amount = min(self.volume, other.capacity - other.volume)
        if amount == 0:
            return
        self.volume -= amount
        other.volume += amount
        self.moves += 1

    def __str__(self) -> str:
        return f"[{self.volume}/{self.capacity}]"


def measure(one: int, two: int, goal: int, start: str) -> tuple[int, str, int]:
    """Pour from source to dest bucket until we have the goal volume."""
    # Create and name the two buckets.
    source = Bucket(one, "one")
    dest = Bucket(two, "two")
    # If starting with bucket two, swap pour direction.
    if start == "two":
        source, dest = dest, source

    # The first move must always be filling the source.
    source.fill_if_empty()

    # Edge case: if goal == dest bucket size, fill the dest.
    if goal == dest.capacity:
        dest.fill_if_empty()

    # Start the pouring! Stop when goal is hit.
    while goal not in (source.volume, dest.volume):
        # In order to transfer, the source needs water and the dest needs space.
        source.fill_if_empty()
        dest.empty_if_full()
        source.transfer_to(dest)

    # Figure out which bucket has what. One is at the "target" volume.
    if source.volume == goal:
        target, other = source, dest
    else:
        target, other = dest, source
    moves = source.moves + dest.moves
    return (moves, target.name, other.volume)
