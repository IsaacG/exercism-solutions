"""
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
import itertools
import functools
import operator


ENGLISHMAN = 1 << 0
SPANIARD = 1 << 1
JAPANESE = 1 << 2
UKRAINIAN = 1 << 3
NORWEGIAN = 1 << 4

NAMES = {
    ENGLISHMAN: "Englishman",
    SPANIARD: "Spaniard",
    JAPANESE: "Japanese",
    UKRAINIAN: "Ukrainian",
    NORWEGIAN: "Norwegian",
}

DOG = 1 << 5
FOX = 1 << 6
SNAILS = 1 << 7
HORSE = 1 << 8
ZEBRA = 1 << 9

RED = 1 << 10
IVORY = 1 << 11
GREEN = 1 << 12
BLUE = 1 << 13
YELLOW = 1 << 14

TEA = 1 << 15
COFFEE = 1 << 16
ORANGE_JUICE = 1 << 17
MILK = 1 << 18
WATER = 1 << 19

OLD_GOLD = 1 << 20
KOOLS = 1 << 21
LUCKY_STRIKE = 1 << 22
PARLIAMENTS = 1 << 23
CHESTERFIELDS = 1 << 24
ALL_BITS = (1 << 25) - 1

NATIONALITIES = {ENGLISHMAN, SPANIARD, JAPANESE, UKRAINIAN, NORWEGIAN}
PETS = {DOG, FOX, SNAILS, HORSE, ZEBRA}
COLORS = {RED, IVORY, GREEN, BLUE, YELLOW}
DRINKS = {TEA, COFFEE, ORANGE_JUICE, MILK, WATER}
SMOKES = {OLD_GOLD, KOOLS, LUCKY_STRIKE, PARLIAMENTS, CHESTERFIELDS}

House = tuple[int, int, int, int, int]
Street = tuple[House, House, House, House, House]
IDX_NAT, IDX_PET, IDX_COLOR, IDX_DRINK, IDX_SMOKE = list(range(5))


@functools.cache
def solve_puzzle() -> Street:
    options = {
        nationality: [
            (nationality, pet, color, drink, smokes)
            for pet in PETS
            for color in COLORS
            for drink in DRINKS
            for smokes in SMOKES
            if (
                # The Englishman lives in the red house.
                (nationality == ENGLISHMAN) == (color == RED)
                # The Spaniard owns the dog.
                and (nationality == SPANIARD) == (pet == DOG)
                # Coffee is drunk in the green house.
                and (drink == COFFEE) == (color == GREEN)
                # The Ukrainian drinks tea.
                and (nationality == UKRAINIAN) == (drink == TEA)
                # The Old Gold smoker owns snails.
                and (smokes == OLD_GOLD) == (pet == SNAILS)
                # Kools are smoked in the yellow house.
                and (smokes == KOOLS) == (color == YELLOW)
                # The Lucky Strike smoker drinks orange juice.
                and (smokes == LUCKY_STRIKE) == (drink == ORANGE_JUICE)
                # The Japanese smokes Parliaments.
                and (smokes == PARLIAMENTS) == (nationality == JAPANESE)
            )
        ]
        for nationality in NATIONALITIES
    }
    # Options found (counts):
    # ENGLISHMAN: 11
    # SPANIARD: 9
    # JAPANESE: 15
    # UKRAINIAN: 11
    # NORWEGIAN: 32

    # Find (unordered) house combinations where all values are present.
    house_combos = [
        houses
        # Combinations: 11*9*15*11*32 = 522720
        for houses in itertools.product(*options.values())
        if functools.reduce(operator.or_, (v for house in houses for v in house)) == ALL_BITS
    ]
    # 456 combinations of possible (unordered) house collections.

    found = []
    # For each valid combination of houses, they can be laid out in many (5! = 120) orders.
    # 456 combinations with 5! orderings = 54720 possibilities.
    for houses in house_combos:
        for street in itertools.permutations(houses):
            # Milk is drunk in the middle house. 54720 to 10944.
            if street[2][IDX_DRINK] != MILK:
                continue
            # The Norwegian lives in the first house. 10944 to 2016.
            if street[0][IDX_NAT] != NORWEGIAN:
                continue
            # The green house is immediately to the right of the ivory house. 2016 to 336.
            idx = next(i for i, house in enumerate(street) if house[IDX_COLOR] == IVORY)
            if idx == 4 or street[idx + 1][IDX_COLOR] != GREEN:
                continue
            # The man who smokes Chesterfields lives in the house next to the man with the fox. 336 to 120.
            idx = next(i for i, house in enumerate(street) if house[IDX_SMOKE] == CHESTERFIELDS)
            if (idx == 0 or street[idx - 1][IDX_PET] != FOX) and (idx == 4 or street[idx + 1][IDX_PET] != FOX):
                continue
            # Kools are smoked in the house next to the house where the horse is kept. 120 to 32.
            idx = next(i for i, house in enumerate(street) if house[IDX_SMOKE] == KOOLS)
            if (idx == 0 or street[idx - 1][IDX_PET] != HORSE) and (idx == 4 or street[idx + 1][IDX_PET] != HORSE):
                continue
            # The Norwegian lives next to the blue house. 32 to 1.
            idx = next(i for i, house in enumerate(street) if house[IDX_NAT] == NORWEGIAN)
            if (idx == 0 or street[idx - 1][IDX_COLOR] != BLUE) and (idx == 4 or street[idx + 1][IDX_COLOR] != BLUE):
                continue
            found.append(street)

    assert len(found) == 1, len(found)
    return found[0]


def drinks_water():
    street = solve_puzzle()
    house = next(house for house in street if house[IDX_DRINK] == WATER)
    return NAMES[house[IDX_NAT]]


def owns_zebra():
    street = solve_puzzle()
    house = next(house for house in street if house[IDX_PET] == ZEBRA)
    return NAMES[house[IDX_NAT]]
