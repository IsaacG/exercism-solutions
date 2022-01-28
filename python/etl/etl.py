"""Transform data format."""


def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Apply a dict transformation."""
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
