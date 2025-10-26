"""
Algorithm
---------

"Guided search" or "mutating search" based on kahgoh's Elixir solution
as described by Jeremy and Erik.

This algorithm starts with a random street as the search space.
It checks that all the rules match.
If a rule does not match, it modifies the house(s) that violates the rules
so that the rule would pass and adds the new street to the search space.
Repeat until a valid street is found.

For example, consider "The Englishman lives in the red house."
Find the house where the Englishman lives and find the red house.
If they are the same house, the rule passes and we check the next rule.
If they are different, try either swapping the nationalities between those house
or swapping the colors.
After either of those two swaps, this rule should now pass.

Representation
--------------
A street/combo is a tuple of five houses.
A house is a collection of five attributes.
An attribute is an integer [0..5).
A house combines attributes via bit shifting, allocating 3 bits per attribute.

Rules
-----

1. There are five houses.
2. The Englishman lives in the red house.
3. The Spaniard owns the dog.
4. Coffee is drunk in the green house.
5. The Ukrainian drinks tea.
6. The green house is immediately to the right of the ivory house.
7. The Old Gold smoker owns snails.
8. Kools are smoked in the yellow house.
9. Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments.
15. The Norwegian lives next to the blue house.

Each of the five houses is painted a different color, and their
inhabitants are of different national extractions, own different pets,
drink different beverages and smoke different brands of cigarettes.
"""

import random

# How far to bit shift each attribute, number of bits.
NATIONALITY, PET, COLOR, DRINK, SMOKE = [i * 3 for i in range(5)]
NATIONALITIES = ENGLISHMAN, SPANIARD, JAPANESE, UKRAINIAN, NORWEGIAN = [i << NATIONALITY for i in range(5)]
PETS = DOG, FOX, SNAILS, HORSE, ZEBRA = [i << PET for i in range(5)]
COLORS = RED, IVORY, GREEN, BLUE, YELLOW = [i << COLOR for i in range(5)]
DRINKS = TEA, COFFEE, ORANGE_JUICE, MILK, WATER = [i << DRINK for i in range(5)]
SMOKES = OLD_GOLD, KOOLS, LUCKY_STRIKE, PARLIAMENTS, CHESTERFIELDS = [i << SMOKE for i in range(5)]

RuleResult = tuple[bool, list[tuple[int, ...]]]


def matches(house: int, attribute: int, value: int) -> bool:
    """Return if a house has a specific attribute, eg NATIONALITY == NORWEGIAN."""
    return house & (0b111 << attribute) == value


def find_house(combo: tuple[int, ...], attribute: int, value: int) -> int:
    """Return the index of a house having a specific value for an attribute."""
    mask = 0b111 << attribute
    return next(idx for idx, house in enumerate(combo) if (house & mask) == value)


def swap(combo: tuple[int, ...], a, b, attribute) -> tuple[int, ...]:
    """Swap attributes between two houses, eg swap the NATIONALITY of houses 1 and 2."""
    # mask is used to get a specific attribute. rev_mask is used to zero out the attribute.
    mask = 0b111 << attribute
    rev_mask  = (2 << 16) - 1 - mask
    # Update the houses.
    houses = list(combo)
    c = houses[a]
    # a becomes a with one attribute taken from b.
    # b becomes b with one attribute taken from c.
    houses[a] = (houses[a] & rev_mask) | houses[b] & mask
    houses[b] = (houses[b] & rev_mask) | c & mask
    return tuple(houses)


def house_rule(combo: tuple[int, ...], attribute_a: int, val_a: int, attribute_b: int, val_b: int,) -> RuleResult:
    """Check a single house has two specific attributes."""
    a = find_house(combo, attribute_a, val_a)
    b = find_house(combo, attribute_b, val_b)
    if a == b:
        return True, []
    return False, [swap(combo, a, b, attribute_a), swap(combo, a, b, attribute_b)]


def adjacent_rule(combo: tuple[int, ...], attribute_a: int, val_a: int, attribute_b: int, val_b: int) -> RuleResult:
    """Check adjacent houses have specific attributes."""
    a = find_house(combo, attribute_a, val_a)
    b = find_house(combo, attribute_b, val_b)
    # Adjacent
    if abs(a - b) == 1:
        return True, []
    alternatives = []
    # Swap attributes with adjacent houses. Two to four possibilities.
    if a > 0:
        alternatives.append(swap(combo, a - 1, b, attribute_b))
    if a < 4:
        alternatives.append(swap(combo, a + 1, b, attribute_b))
    if b > 0:
        alternatives.append(swap(combo, b - 1, b, attribute_a))
    if b < 4:
        alternatives.append(swap(combo, b + 1, b, attribute_a))
    return False, alternatives


def green_ivory(combo: tuple[int, ...]) -> RuleResult:
    """6. The green house is immediately to the right of the ivory house."""
    a = find_house(combo, COLOR, GREEN)
    b = find_house(combo, COLOR, IVORY)
    if a == b + 1:
        return True, []
    alternatives = []
    if a > 0:
        alternatives.append(swap(combo, a - 1, b, COLOR))
    if b < 4:
        alternatives.append(swap(combo, b + 1, a, COLOR))
    return False, alternatives


def milk_middle(combo: tuple[int, ...]) -> RuleResult:
    """9. Milk is drunk in the middle house."""
    a = 2  # middle
    b = find_house(combo, DRINK, MILK)
    if a == b:
        return True, []
    return False, [swap(combo, a, b, DRINK)]


def norway_first(combo: tuple[int, ...]) -> RuleResult:
    """10. The Norwegian lives in the first house."""
    a = 0  # first
    b = find_house(combo, NATIONALITY, NORWEGIAN)
    if a == b:
        return True, []
    return False, [swap(combo, a, b, NATIONALITY)]


RULES = [
    # 2. The Englishman lives in the red house.
    lambda x: house_rule(x, NATIONALITY, ENGLISHMAN, COLOR, RED),
    # 3. The Spaniard owns the dog.
    lambda x: house_rule(x, NATIONALITY, SPANIARD, PET, DOG),
    # 4. Coffee is drunk in the green house.
    lambda x: house_rule(x, DRINK, COFFEE, COLOR, GREEN),
    # 5. The Ukrainian drinks tea.
    lambda x: house_rule(x, NATIONALITY, UKRAINIAN, DRINK, TEA),
    # 7. The Old Gold smoker owns snails.
    lambda x: house_rule(x, SMOKE, OLD_GOLD, PET, SNAILS),
    # 8. Kools are smoked in the yellow house.
    lambda x: house_rule(x, SMOKE, KOOLS, COLOR, YELLOW),
    # 13. The Lucky Strike smoker drinks orange juice.
    lambda x: house_rule(x, SMOKE, LUCKY_STRIKE, DRINK, ORANGE_JUICE),
    # 14. The Japanese smokes Parliaments.
    lambda x: house_rule(x, NATIONALITY, JAPANESE, SMOKE, PARLIAMENTS),
    # 6. The green house is immediately to the right of the ivory house.
    green_ivory,
    # 9. Milk is drunk in the middle house.
    milk_middle,
    # 10. The Norwegian lives in the first house.
    norway_first,
    # 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
    lambda x: adjacent_rule(x, SMOKE, CHESTERFIELDS, PET, FOX),
    # 12. Kools are smoked in the house next to the house where the horse is kept.
    lambda x: adjacent_rule(x, SMOKE, KOOLS, PET, HORSE),
    # 15. The Norwegian lives next to the blue house.
    lambda x: adjacent_rule(x, NATIONALITY, NORWEGIAN, COLOR, BLUE),
]


def solve_puzzle() -> tuple[int, ...]:
    """Solve the puzzle."""
    # Create a random street.
    attributes = [NATIONALITIES.copy(), PETS.copy(), COLORS.copy(), DRINKS.copy(), SMOKES.copy()]
    for attrib in attributes:
        random.shuffle(attrib)
    houses = [sum(attribs) for attribs in zip(*attributes)]

    # Depth first. If a street doesn't fulfill a role, try swapping in either direction to match the rule and queue both.
    combos = [tuple(houses)]
    seen = set(combos)
    while combos:
        combo = combos.pop()
        for rule in RULES:
            ok, alternatives = rule(combo)
            if not ok:
                for alternative in alternatives:
                    if alternative in seen:
                        continue
                    seen.add(alternative)
                    combos.append(alternative)
                break
        else:
            # All the rules pass.
            return combo
    raise RuntimeError("not solved")


def nationality(house: int) -> str:
    n = house & (0b111 << NATIONALITY)
    return {
        ENGLISHMAN: "Englishman",
        SPANIARD: "Spaniard",
        JAPANESE: "Japanese",
        UKRAINIAN: "Ukrainian",
        NORWEGIAN: "Norwegian",
    }[n]


def drinks_water() -> str:
    """Return the nationality of the water drinker."""
    street = solve_puzzle()
    return nationality(street[find_house(street, DRINK, WATER)])


def owns_zebra() -> str:
    """Return the nationality of the zebra owner."""
    street = solve_puzzle()
    return nationality(street[find_house(street, PET, ZEBRA)])
