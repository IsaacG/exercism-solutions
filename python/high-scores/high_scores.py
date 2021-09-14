"""High score utilities."""

def personal_top_three(scores: list[int]) -> list[int]:
    """Return the top three."""
    return sorted(scores, reverse=True)[:3]

def personal_best(scores: list[int]) -> int:
    """Return the best score."""
    return max(scores)

def latest(scores: list[int]) -> int:
    """Return the last score."""
    return scores[-1]
