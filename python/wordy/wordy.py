"""Solve word equations."""

import operator
import re

from typing import Callable, Generator


# Match a number.
NUM_RE = re.compile(r"(-?[0-9]+)[ \?]")
# Binary (two operands) operations.
OPS = [
    (operator.mul, "multiplied by"),
    (operator.truediv, "divided by"),
    (operator.add, "plus"),
    (operator.sub, "minus"),
    (operator.mod, "modulus"),
    (operator.gt, "is greater than"),
    (operator.lt, "is less than"),
    (operator.lt, "is less than"),
]


def tokenize(question: str) -> Generator[tuple[Callable[[int, int], int], int], None, None]:
    """Generator operator, number pairs for a given question.

    Parse a question and yield tuple[operator, int] pairs for the input.
    The expectation is that we start with a value of 0 and the first operation is a "0 + int".
    """
    # Pointer to the start of the next token.
    position = 0
    # The end of the question, when we stop parsing.
    end = len(question)

    def read_int():
        """Return an int, parsed from the current position."""
        nonlocal position
        if match := NUM_RE.match(question[position:]):
            position += match.end()
            return int(match.group(1))
        raise ValueError("syntax error")

    def read_op():
        """Return an operator, parsed from the current position."""
        nonlocal position
        for oper, text in OPS:
            if question[position:].startswith(text):
                position += len(text) + 1
                return oper
        if NUM_RE.match(question[position:]):
            raise ValueError("syntax error")
        raise ValueError("unknown operation")

    # Parse the first two works, "What is ..."
    if not question[position:].startswith("What "):
        raise ValueError("unknown operation")
    position += len("What ")
    if not question[position:].startswith("is "):
        raise ValueError("syntax error")
    position += len("is ")

    # The first operator is an implicit "add".
    yield operator.add, read_int()
    # While there is more question, parse operator, int pairs.
    while position < end:
        yield read_op(), read_int()


def answer(question: str) -> int:
    """Answer a word problem."""
    value = 0
    for oper, num in tokenize(question):
        value = oper(value, num)
    return value
