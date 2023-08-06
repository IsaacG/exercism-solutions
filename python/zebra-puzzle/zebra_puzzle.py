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
import enum
import itertools
import functools
import operator


class Nationality(enum.Enum):
    ENGLISHMAN = enum.auto()
    SPANIARD = enum.auto()
    JAPANESE = enum.auto()
    UKRAINIAN = enum.auto()
    NORWEGIAN = enum.auto()

NAMES = {
    Nationality.ENGLISHMAN: "Englishman",
    Nationality.SPANIARD: "Spaniard",
    Nationality.JAPANESE: "Japanese",
    Nationality.UKRAINIAN: "Ukrainian",
    Nationality.NORWEGIAN: "Norwegian",
}

class Pets(enum.Enum):
    DOG = enum.auto()
    FOX = enum.auto()
    SNAILS = enum.auto()
    HORSE = enum.auto()
    ZEBRA = enum.auto()


class Colors(enum.Enum):
    RED = enum.auto()
    IVORY = enum.auto()
    GREEN = enum.auto()
    BLUE = enum.auto()
    YELLOW = enum.auto()


class Drinks(enum.Enum):
    TEA = enum.auto()
    COFFEE = enum.auto()
    ORANGE_JUICE = enum.auto()
    MILK = enum.auto()
    WATER = enum.auto()


class Smokes(enum.Enum):
    OLD_GOLD = enum.auto()
    KOOLS = enum.auto()
    LUCKY_STRIKE = enum.auto()
    PARLIAMENTS = enum.auto()
    CHESTERFIELDS = enum.auto()


ALL_VALUES = [set(Nationality), set(Pets), set(Colors), set(Drinks), set(Smokes)]

House = tuple[int, int, int, int, int]
Street = tuple[House, House, House, House, House]
IDX_NAT, IDX_PET, IDX_COLOR, IDX_DRINK, IDX_SMOKE = list(range(5))

def valid_house(nationality, pet, color, drink, smokes) -> bool:
    return (
        # The Englishman lives in the red house.
        (nationality == Nationality.ENGLISHMAN) == (color == Colors.RED)
        # The Spaniard owns the dog.
        and (nationality == Nationality.SPANIARD) == (pet == Pets.DOG)
        # Coffee is drunk in the green house.
        and (drink == Drinks.COFFEE) == (color == Colors.GREEN)
        # The Ukrainian drinks tea.
        and (nationality == Nationality.UKRAINIAN) == (drink == Drinks.TEA)
        # The Old Gold smoker owns snails.
        and (smokes == Smokes.OLD_GOLD) == (pet == Pets.SNAILS)
        # Kools are smoked in the yellow house.
        and (smokes == Smokes.KOOLS) == (color == Colors.YELLOW)
        # The Lucky Strike smoker drinks orange juice.
        and (smokes == Smokes.LUCKY_STRIKE) == (drink == Drinks.ORANGE_JUICE)
        # The Japanese smokes Parliaments.
        and (smokes == Smokes.PARLIAMENTS) == (nationality == Nationality.JAPANESE)
    )


def valid_street(street):
    # Milk is drunk in the middle house. 54720 to 10944.
    if street[2][IDX_DRINK] != Drinks.MILK:
        return False
    # The Norwegian lives in the first house. 10944 to 2016.
    if street[0][IDX_NAT] != Nationality.NORWEGIAN:
        return False
    # The green house is immediately to the right of the ivory house. 2016 to 336.
    idx = next(i for i, house in enumerate(street) if house[IDX_COLOR] == Colors.IVORY)
    if idx == 4 or street[idx + 1][IDX_COLOR] != Colors.GREEN:
        return False
    # The man who smokes Chesterfields lives in the house next to the man with the fox. 336 to 120.
    idx = next(i for i, house in enumerate(street) if house[IDX_SMOKE] == Smokes.CHESTERFIELDS)
    if (idx == 0 or street[idx - 1][IDX_PET] != Pets.FOX) and (idx == 4 or street[idx + 1][IDX_PET] != Pets.FOX):
        return False
    # Kools are smoked in the house next to the house where the horse is kept. 120 to 32.
    idx = next(i for i, house in enumerate(street) if house[IDX_SMOKE] == Smokes.KOOLS)
    if (idx == 0 or street[idx - 1][IDX_PET] != Pets.HORSE) and (idx == 4 or street[idx + 1][IDX_PET] != Pets.HORSE):
        return False
    # The Norwegian lives next to the blue house. 32 to 1.
    idx = next(i for i, house in enumerate(street) if house[IDX_NAT] == Nationality.NORWEGIAN)
    if (idx == 0 or street[idx - 1][IDX_COLOR] != Colors.BLUE) and (idx == 4 or street[idx + 1][IDX_COLOR] != Colors.BLUE):
        return False
    return True


@functools.cache
def solve_puzzle() -> Street:
    options = {
        nationality: [
            (nationality, pet, color, drink, smokes)
            for pet in Pets
            for color in Colors
            for drink in Drinks
            for smokes in Smokes
            if valid_house(nationality, pet, color, drink, smokes)
        ]
        for nationality in Nationality
    }
    # Options found (counts):
    # ENGLISHMAN: 11
    # SPANIARD: 9
    # JAPANESE: 15
    # UKRAINIAN: 11
    # NORWEGIAN: 32
    # Combinations: 11*9*15*11*32 = 522720

    # Find (unordered) house combinations where all values are present.
    house_combos = (
        houses
        for houses in itertools.product(*options.values())
        if [set(v) for v in zip(*houses)] == ALL_VALUES
    )
    # 456 combinations of possible (unordered) house collections.

    # For each valid combination of houses, they can be laid out in many (5! = 120) orders.
    # 456 combinations with 5! orderings = 54720 possibilities.
    found = [
        street
        for houses in house_combos
        for street in itertools.permutations(houses)
        if valid_street(street)
    ]

    assert len(found) == 1, len(found)
    return found[0]


def drinks_water():
    street = solve_puzzle()
    house = next(house for house in street if house[IDX_DRINK] == Drinks.WATER)
    return NAMES[house[IDX_NAT]]


def owns_zebra():
    street = solve_puzzle()
    house = next(house for house in street if house[IDX_PET] == Pets.ZEBRA)
    return NAMES[house[IDX_NAT]]
