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
    (operator.pow, re.compile(r"(.*) raised to the (.*)th power")),
    (operator.mul, re.compile(r"(.*) multiplied by (.*)")),
    (operator.truediv, re.compile(r"(.*) divided by (.*)")),
    (operator.add, re.compile(r"(.*) plus (.*)")),
    (operator.sub, re.compile(r"(.*) minus (.*)")),
    (operator.mod, re.compile(r"(.*) modulus (.*)")),
    (operator.eq, re.compile(r"(.*) equals (.*)")),
    (operator.gt, re.compile(r"(.*) is greater than (.*)")),
    (operator.lt, re.compile(r"(.*) is less than (.*)")),
    (operator.lt, re.compile(r"(.*) is less than (.*)")),
    (raise_unknown, re.compile(r"\d+ cubed")),
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
    if NUM_RE.fullmatch(question):
        return int(question)
    for operation, pattern in OPS:
        if match := pattern.fullmatch(question):
            operands = (solve(part) for part in match.groups())
            return operation(*operands)
    raise ValueError("syntax error")
