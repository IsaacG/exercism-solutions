"""The Old Woman."""

REACTIONS = {
    "fly": "I don't know why she swallowed the fly. Perhaps she'll die.",
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird!",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I don't know how she swallowed a cow!",
    "horse": "She's dead, of course!",
}
# Map verse "numbers" to specific animals.
ANIMALS = dict(enumerate(REACTIONS, start=1))
# Map each animal to it's food/subject, i.e. what it eats.
SUBJECTS = dict(zip(list(REACTIONS)[1:], list(REACTIONS)))
# Unlike all other animals, the bird does not simply eat a "spider". It is more detailed.
SUBJECTS["bird"] = "spider that wriggled and jiggled and tickled inside her"


def verse(num: int) -> list[str]:
    """Return one verse."""
    out = [f"I know an old lady who swallowed a {ANIMALS[num]}."]
    if num > 1:
        out.append(REACTIONS[ANIMALS[num]])
    if num < 8:
        for i in range(num, 1, -1):
            out.append(f"She swallowed the {ANIMALS[i]} to catch the {SUBJECTS[ANIMALS[i]]}.")
        out.append(REACTIONS[ANIMALS[1]])
    return out


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return a set of verses."""
    out = []
    for i in range(start_verse, end_verse + 1):
        out.extend(verse(i))
        if i != end_verse:
            out.append("")
    return out
