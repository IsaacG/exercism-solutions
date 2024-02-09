"""Poker hand ranking."""

from __future__ import annotations

import collections
import itertools


# Face cards. Used to make Jack, Queen, King, Ace to a value.
FACE = {"J": 11, "Q": 12, "K": 13, "A": 14} | {str(i): i for i in range(2, 11)}


class Card:
    """One card."""

    def __init__(self, val: str):
        """Initialize."""
        self.suit = val[-1]
        self.pips = FACE[val[:-1]]


class Hand:
    """A poker hand."""

    def __init__(self, cards: str):
        """Initialize a Hand."""
        self.original_repr = cards
        self.cards = [Card(i) for i in cards.split()]
        self.pips = sorted(c.pips for c in self.cards)

        # Group pip values by count, e.g. [3, 3, 4, 4, 9] => {2: [3, 4], 1: [9]}
        self.counts = collections.defaultdict(list)
        for pips, count in collections.Counter(self.pips).items():
            self.counts[count].append(pips)
        for counts in self.counts.values():
            counts.sort(reverse=True)

        self.flush = len(set(c.suit for c in self.cards)) == 1
        self.low_straight = FACE["A"] in self.pips and self.values_are_straight([1] + self.pips[:-1])
        self.regular_straight = self.values_are_straight(self.pips)
        self.straight = self.regular_straight or self.low_straight

    @staticmethod
    def values_are_straight(pips: list[int]) -> bool:
        return all(b - a == 1 for a, b in zip(pips[:-1], pips[1:]))

    @property
    def category(self) -> int:
        """Return the hand category."""
        if self.flush and self.straight:
            return 8  # STRAIGHT_FLUSH
        if self.counts[4]:
            return 7  # FOUR_KIND
        if self.counts[3] and self.counts[2]:
            return 6  # FULL_HOUSE
        if self.flush:
            return 5  # FLUSH
        if self.straight:
            return 4  # STRAIGHT
        if self.counts[3]:
            return 3  # THREE_KIND
        if len(self.counts[2]) == 2:
            return 2  # TWO_PAIR
        if len(self.counts[2]) == 1:
            return 1  # ONE_PAIR
        return 0  # NONE

    def __lt__(self, other: Hand) -> bool:
        """Return if self is lower poitns than other. Useful for sorting."""
        # If the categories differ, order by category.
        if self.category != other.category:
            return self.category < other.category

        # Edge case: A2345 loses to 23456.
        if self.straight and self.regular_straight != other.regular_straight:
            return self.low_straight

        # For the same category, compare pips for a tie breaker, in priority of N-of-a-kind.
        for count in sorted(set(self.counts) | set(other.counts), reverse=True):
            for a, b in itertools.zip_longest(self.counts[count], other.counts[count], fillvalue=0):
                if a != b:
                    return a < b
        return False

    def __str__(self) -> str:
        return self.original_repr


def best_hands(hands: list[str]) -> list[str]:
    """Return the best poker hands."""
    # Map the input strings to the Hand so the inputs can be reused for returns.
    the_hands = [Hand(hand) for hand in hands]
    # Find the best hand. Hands sort from best to worst.
    best = max(the_hands)
    # Return all hands that would tie the best hand.
    return [str(v) for v in the_hands if not v < best]
