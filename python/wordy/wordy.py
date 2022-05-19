"""Solve word equations."""

import operator
import re


def raise_unknown() -> None:
    """Raise an unknown error."""
    raise ValueError("unknown operation")


# Word problem prefix/suffix.
PREFIX = "What is "
SUFFIX = "?"
# Match a number.
NUM_RE = re.compile(r"-?[0-9]+")
# Binary (two operands) operations.
OPS = [
    (int, re.compile(r"(-?\d+)")),
    (operator.pow, re.compile(r"(.*) raised to the (-?\d+)th power")),
    (operator.mul, re.compile(r"(.*) multiplied by (-?\d+)")),
    (operator.truediv, re.compile(r"(.*) divided by (-?\d+)")),
    (operator.add, re.compile(r"(.*) plus (-?\d+)")),
    (operator.sub, re.compile(r"(.*) minus (-?\d+)")),
    (operator.mod, re.compile(r"(.*) modulus (-?\d+)")),
    (operator.eq, re.compile(r"(.*) equals (-?\d+)")),
    (operator.gt, re.compile(r"(.*) is greater than (-?\d+)")),
    (operator.lt, re.compile(r"(.*) is less than (-?\d+)")),
    (operator.lt, re.compile(r"(.*) is less than (-?\d+)")),
    (raise_unknown, re.compile(r"-?\d+ cubed")),
]


def answer(question: str) -> int:
    """Answer a word problem."""
    if not question.endswith(SUFFIX):
        raise ValueError("syntax error")
    if " is " not in question:
        raise ValueError("syntax error")
    if not question.startswith(PREFIX):
        raise ValueError("unknown operation")
    question = question.removeprefix(PREFIX).removesuffix(SUFFIX)
    return solve(question)


def solve(question: str) -> int:
    """Solve a problem fragment."""
    for operation, pattern in OPS:
        if match := pattern.fullmatch(question):
            if " " in question:
                resolver = solve
            else:
                # Stop recursing when down to one token.
                resolver = lambda x: x
            operands = (resolver(part) for part in match.groups())
            return operation(*operands)
    raise ValueError("syntax error")
