"""Recite a proverb."""


def proverb(*words, qualifier: None | str = None) -> list[str]:
    """Return proverb verses."""
    out = [
        f"For want of a {a} the {b} was lost."
        for a, b in zip(words[:-1], words[1:])
    ]
    if words:
        if qualifier:
            qualifier += " "
        out.append(f"And all for the want of a {qualifier or ''}{words[0]}.")
    return out
