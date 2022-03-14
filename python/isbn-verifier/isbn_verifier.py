"""ISBN validation."""


def is_valid(isbn: str) -> bool:
    """Return if an ISBN is valid."""
    # Ignore dashes.
    values = [value for value in isbn if value != "-"]

    if len(values) != 10:
        return False

    # The last character (and only the last one) may be "X". Map "X" => 10
    if values[-1] == "X":
        values[-1] = "10"

    if any(not value.isdigit() for value in values):
        return False

    total = sum(int(value) * (10 - position) for position, value in enumerate(values))
    return total % 11 == 0
