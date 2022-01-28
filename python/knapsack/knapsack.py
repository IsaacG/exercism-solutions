"""Brute force the knapsack problem."""
import functools


@functools.cache
def maximum(cap: int, items: tuple[tuple[int, int]]) -> int:
    """Solve for the maximum backpack value."""
    options = []
    for i, (weight, val) in enumerate(items):
        if weight > cap:
            continue
        n_items = items[:i] + items[i + 1:]
        options.append(val + maximum(cap - weight, n_items))
    return max(options) if options else 0


def maximum_value(maximum_weight: int, items: list[dict[str, int]]) -> int:
    """Return the maximum backpack value."""
    item_tuple = tuple((i["weight"], i["value"]) for i in items)
    return maximum(maximum_weight, item_tuple)
