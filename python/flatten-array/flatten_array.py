"""Flatten a nested list."""

def flatten_generator(val):
    """Generate values from a nested list."""
    if val is None:
        return

    if isinstance(val, list):
        for i in val:
            yield from flatten(i)
    else:
        yield val


def flatten(val):
    """Flatten into a list."""
    return list(flatten_generator(val))
