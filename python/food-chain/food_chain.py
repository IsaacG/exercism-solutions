"""The Old Woman."""

ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
SUBJECTS = ANIMALS.copy()
SUBJECTS[1] = "spider that wriggled and jiggled and tickled inside her"
REACTIONS = [
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!",
]


def verse(num: int) -> list[str]:
    """Return one verse."""
    out = [f"I know an old lady who swallowed a {ANIMALS[num - 1]}."]
    if num > 1:
        out.append(REACTIONS[num - 2])
    if num < 8:
        for i in range(num, 1, -1):
            out.append(f"She swallowed the {ANIMALS[i - 1]} to catch the {SUBJECTS[i - 2]}.")
        out.append("I don't know why she swallowed the fly. Perhaps she'll die.")
    return out


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return a set of verses."""
    out = []
    for i in range(start_verse, end_verse + 1):
        out.extend(verse(i))
        if i != end_verse:
            out.append("")
    return out
