"""Solve word equations."""

import operator
import re

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
]


def answer(question: str) -> int:
    """Answer a word problem."""
    if not question.startswith(PREFIX) or not question.endswith(SUFFIX):
        raise ValueError("bad input")
    question = question.removeprefix(PREFIX).removesuffix(SUFFIX)
    return solve(question)


def solve(question: str) -> int:
    """Solve a problem fragment."""
    if NUM_RE.fullmatch(question):
        return int(question)
    for operation, pattern in OPS:
        if match := pattern.fullmatch(question):
            return operation(solve(match.group(1)), solve(match.group(2)))
    raise ValueError("bad input")
