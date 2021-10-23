"""Poker hand ranking."""

from __future__ import annotations

import collections
import enum


# Face cards. Used to make Jack, Queen, King, Ace to a value.
FACE = {"J": 11, "Q": 12, "K": 13, "A": 14}


class Suit(enum.Enum):
    """Card suit. This validates the suit value."""

    H = enum.auto()
    S = enum.auto()
    C = enum.auto()
    D = enum.auto()


class Category(enum.Enum):
    """Hand category."""

    STRAIGHT_FLUSH = enum.auto()
    FOUR_KIND = enum.auto()
    FULL_HOUSE = enum.auto()
    FLUSH = enum.auto()
    STRAIGHT = enum.auto()
    THREE_KIND = enum.auto()
    TWO_PAIR = enum.auto()
    ONE_PAIR = enum.auto()
    NONE = enum.auto()

    def __lt__(self, other):
        """Return if this category beats other. Allows sorting."""
        return self.value < other.value


class Outcome(enum.Enum):
    """Outcome when comparing hands."""

    WIN = enum.auto()
    LOSE = enum.auto()
    TIE = enum.auto()


class Card:
    """One card."""

    def __init__(self, val: str):
        """Initialize."""
        self.suit = Suit[val[-1]]
        pips = val[:-1]
        if pips in FACE:
            self.pips = FACE[pips]
        else:
            self.pips = int(pips)

    def __lt__(self, other):
        """Return if self < other. Allows sorting."""
        return self.pips < other.pips


class Hand:
    """A poker hand."""

    def __init__(self, val: str):
        """Initialize a Hand."""
        self.cards = [Card(i) for i in val.split()]
        assert len(self.cards) == 5, "A hand must contain 5 cards."

        self.pips = sorted(c.pips for c in self.cards)
        assert min(self.pips) > 1, "Cards cannot have a value below 2."
        assert max(self.pips) <= FACE["A"], "Cards cannot have a value greater than Ace."

        # Group pip values by count, e.g. [3, 3, 4, 4, 9] => {2: [3, 4], 1: [9]}
        self.counts = collections.defaultdict(list)
        for pips, count in collections.Counter(self.pips).items():
            self.counts[count].append(pips)

    @property
    def flush(self) -> bool:
        """Return if this hand is a flush, i.e. only one suit."""
        return len(set(c.suit for c in self.cards)) == 1

    @property
    def _straight(self) -> bool:
        """Return if this hand is a regular straight."""
        paired = zip(self.pips, self.pips[1:])
        return all(b - a == 1 for a, b in paired)

    @property
    def _straight_low_ace(self) -> bool:
        """Return if this hand is a straight using Ace as 1."""
        if FACE["A"] not in self.pips:
            return False
        pips = [1] + self.pips[:-1]
        paired = zip(pips, pips[1:])
        return all(b - a == 1 for a, b in paired)

    @property
    def straight(self) -> bool:
        """Return if this hand is a straight."""
        return self._straight or self._straight_low_ace

    @property
    def category(self) -> Category:
        """Return the hand category."""
        if self.flush and self.straight:
            return Category.STRAIGHT_FLUSH
        if 4 in self.counts:
            return Category.FOUR_KIND
        if 3 in self.counts and 2 in self.counts:
            return Category.FULL_HOUSE
        if self.flush:
            return Category.FLUSH
        if self.straight:
            return Category.STRAIGHT
        if 3 in self.counts:
            return Category.THREE_KIND
        if len(self.counts.get(2, [])) == 2:
            return Category.TWO_PAIR
        if len(self.counts.get(2, [])) == 1:
            return Category.ONE_PAIR
        return Category.NONE

    @staticmethod
    def _pips_cmp(self: list[int], other: list[int]) -> Outcome:
        """Compare a list of pips and determine if one beats the other."""
        for a, b in zip(sorted(self, reverse=True), sorted(other, reverse=True)):
            if a > b:
                return Outcome.WIN
            if a < b:
                return Outcome.LOSE
        return Outcome.TIE

    def __cmp__(self, other: Hand) -> Outcome:
        """Compare hands for an outcome."""
        # If the categories differ, order by category.
        s_cat, o_cat = self.category, other.category
        if s_cat != o_cat:
            return Outcome.WIN if s_cat < o_cat else Outcome.LOSE

        # Edge case: A2345 loses to 23456.
        if self.straight and self._straight != other._straight:
            return Outcome.LOSE if self._straight_low_ace else Outcome.WIN

        # For the same category, compare pips for a tie breaker, in priority of N-of-a-kind.
        for count in sorted(self.counts, reverse=True):
            # Ternary state. Pips can indicate win, lose or tie. Tie continues on.
            cmp = self._pips_cmp(self.counts[count], other.counts[count])
            if cmp != Outcome.TIE:
                return cmp
        return Outcome.TIE

    def __lt__(self, other: Hand) -> bool:
        """Return if self beats other. Useful for sorting."""
        return self.__cmp__(other) == Outcome.WIN


def best_hands(hands: list[str]) -> list[str]:
    """Return the best poker hands."""
    # Map the input strings to the Hand so the inputs can be reused for returns.
    the_hands = {i: Hand(i) for i in hands}
    # Find the best hand. Hands sort from best to worst.
    best = min(the_hands.values())
    # Return all hands that would tie the best hand.
    return [k for k, v in the_hands.items() if v.__cmp__(best) == Outcome.TIE]
