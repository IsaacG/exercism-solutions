"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

from typing import Union


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    return int(card)


def values(cards: tuple[str, ...]) -> list[int]:
    """Return multiple card values."""
    return [value_of_card(card) for card in cards]


def higher_card(*cards: str) -> Union[str, tuple[str, ...]]:
    """Determine which card has a higher value in the hand.

    J, Q, K = 10, 'A' = 1, all others are numerical value.

    :param card_one, card_two: str - cards dealt.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    for i in range(2):
        if value_of_card(cards[i]) > value_of_card(cards[1 - i]):
            return cards[i]
    return cards


def value_of_ace(*cards: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card (J, Q, K == 10, numerical value otherwise)
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    vals = values(cards)
    if 1 in vals or sum(vals) > 10:
        return 1
    return 11


def is_blackjack(*cards: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    J, Q, K = 10, 'A' = 11, all others are numerical value.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    return set(values(cards)) == {1, 10}


def can_split_pairs(*cards: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(cards[0]) == value_of_card(cards[1])


def can_double_down(*cards: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    return 9 <= sum(values(cards)) <= 11
