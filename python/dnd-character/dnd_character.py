"""D&D Character Generator."""

import random

TRAITS = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')


def modifier(stat: int) -> int:
    """Return the modifier value based on a skill stat."""
    return (stat - 10) // 2


class Character:
    """D&D character generator."""

    # For pylint
    constitution: int

    def __init__(self):
        """Initialize the character."""
        for trait in TRAITS:
            setattr(self, trait, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """Roll an ability stat: 4d6 and discard the lowest die."""
        dice = sorted(random.randint(1, 6) for _ in range(4))
        return sum(dice[1:])
