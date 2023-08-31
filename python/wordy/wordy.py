"""Solve word equations.


Iteration 1: Recursive regex-based split and solve.
Iteration 2: Similar to #1 with more operators.
Iteration 3: Similar to #2 with numbers treated as an operation.
Iteration 4: Similar to #3.
Iteration 5: Replace recursion and regex matching with a stream parser/tokenizer/generator.
    This approach should be significantly more efficient as there is no recursion.
Iteration 6: Replace the generator with a single-pass regex.split().
    This approach is simpler as there is no need to maintain an index/pointer
    and all the splitting/tokenizing happens in a single call.
"""

import operator
import re

from typing import Callable


# Match a number.
NUM_RE = re.compile(r"(-?[0-9]+)")
# Binary (two operands) operations.
OPS = {
    "times": operator.mul,
    "multiplied by": operator.mul,
    "divided by": operator.truediv,
    "plus": operator.add,
    "minus": operator.sub,
    "modulus": operator.mod,
    "is greater than": operator.gt,
    "is less than": operator.lt,
}


def tokenize(question: str) -> list[tuple[Callable[[int, int], int], int]]:
    """Return pairs of operators and operands, parsed from the question.

    The expectation is that we start with a value of 0
    and the first operation is a "0 + int".
    """
    # Parse the first two words and suffix, "What is ...?"
    if not question.startswith("What "):
        raise ValueError("unknown operation")
    if not question.startswith("What is "):
        raise ValueError("syntax error")
    if not question.endswith("?"):
        raise ValueError("syntax error")
    question = question.removeprefix("What is ").removesuffix("?")

    # Split the question up into operations and numbers.
    pattern = r"|".join(OPS)
    parts = re.split(f"({pattern})", question)
    parts = [i.strip() for i in parts]

    numbers = parts[::2]
    operations = ["plus"] + parts[1::2]

    # Validation. The operators are known good since they were taken from
    # the operators dict. The part between the operators need validation.
    for number in numbers:
        if any(i.isalpha() for i in number.split()):
            raise ValueError("unknown operation")
        if not NUM_RE.fullmatch(number):
            raise ValueError("syntax error")

    # Map operators to callables and numbers to integers.
    # Pair them up and return.
    return list(zip((OPS[oper] for oper in operations), (int(i) for i in numbers)))


def answer(question: str) -> int:
    """Answer a word problem."""
    value = 0
    for oper, num in tokenize(question):
        value = oper(value, num)
    return value
