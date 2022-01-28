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
import dataclasses
import itertools
import functools


NATIONALITIES = {"Englishman", "Spaniard", "Japanese", "Ukrainian", "Norwegian"}
PETS = {"dog", "fox", "snails", "horse", "zebra"}
COLORS = {"red", "ivory", "green", "blue", "yellow"}
DRINKS = {"tea", "coffee", "orange juice", "milk", "water"}
SMOKES = {"Old Gold", "Kools", "Lucky Strike", "Parliaments", "Chesterfields"}
VALUES = [NATIONALITIES, PETS, COLORS, DRINKS, SMOKES]


@dataclasses.dataclass
class House:
    nationality: str
    pet: str
    color: str
    drink: str
    smoke: str


FAST_CHECKS = [
    # 9. Milk is drunk in the middle house.
    lambda h: h[2].drink == "milk",
    # 10. The Norwegian lives in the first house.
    lambda h: h[0].nationality == "Norwegian",
    # 15. The Norwegian lives next to the blue house.
    lambda h: h[1].color == "blue",
]

WHOLE_CHECKS = [
    # 6. The green house is immediately to the right of the ivory house.
    lambda h: any(l.color == "ivory" and r.color == "green" for l, r in itertools.pairwise(h)),
    # 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
    lambda h: any(
        abs(i - j) == 1 for i, one in enumerate(h) for j, other in enumerate(h)
        if i != j and one.smoke == "Chesterfields" and other.pet == "fox"
    ),
    # 12. Kools are smoked in the house next to the house where the horse is kept.
    lambda h: any(
        abs(i - j) == 1 for i, one in enumerate(h) for j, other in enumerate(h)
        if i != j and one.smoke == "Kools" and other.pet == "horse"
    ),
]

ANY_CONSTRAINTS = [
    # 2. The Englishman lives in the red house.
    (lambda h: h.nationality == "Englishman" and h.color == "red"),
    # 3. The Spaniard owns the dog.
    (lambda h: h.nationality == "Spaniard" and h.pet == "dog"),
    # 4. Coffee is drunk in the green house.
    (lambda h: h.drink == "coffee" and h.color == "green"),
    # 5. The Ukrainian drinks tea.
    (lambda h: h.nationality == "Ukrainian" and h.drink == "tea"),
    # 7. The Old Gold smoker owns snails.
    (lambda h: h.smoke == "Old Gold" and h.pet == "snails"),
    # 8. Kools are smoked in the yellow house.
    (lambda h: h.smoke == "Kools" and h.color == "yellow"),
    # 13. The Lucky Strike smoker drinks orange juice.
    (lambda h: h.smoke == "Lucky" and h.drink == "orange juice"),
    # 14. The Japanese smokes Parliaments.
    (lambda h: h.nationality == "Japanese" and h.smoke == "Parliaments"),
]


@functools.cache
def build_houses():
    inputs = [itertools.permutations(data) for data in VALUES]
    count = 0

    for orders in itertools.product(*inputs):
        houses = [House(*vals) for vals in zip(*orders)]
        count += 1
        if count % 500011 == 0:
            print(count, str(houses))
        if not all(check(houses) for check in FAST_CHECKS):
            continue
        if not all(check(houses) for check in WHOLE_CHECKS):
            continue
        if not all(any(check(h) for h in houses) for check in ANY_CONSTRAINTS):
            continue
        return houses
    

def drinks_water():
    h = build_houses()
    print(h)


def owns_zebra():
    pass


build_houses()
