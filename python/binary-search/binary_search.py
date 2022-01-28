"""Binary search."""


def find(search_list: list[int], value: int) -> int:
    """Return the index of a value in a list, using binary search."""
    lower = 0
    upper = len(search_list)
    while lower != upper:
        # Take the center point as the pivot.
        pivot = (upper + lower) // 2
        if search_list[pivot] == value:
            return pivot
        # Reduce the search to the upper/lower half of the list.
        if search_list[pivot] > value:
            upper = pivot
        else:
            lower = pivot + 1
    raise ValueError("value not in array")
