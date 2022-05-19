"""Forth interpretter."""
import operator
import re


NUM_RE = re.compile(r"^-?\d+$")


class StackUnderflowError(Exception):
    """Raised when the stack does not contain sufficient items for an operation."""


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
}
# Minimum stack size for these operators.
# Anything smaller triggers a StackUnderflowError.
MIN_STACK = {
    "+": 2,
    "-": 2,
    "*": 2,
    "/": 2,
    "dup": 1,
    "drop": 1,
    "swap": 2,
    "over": 2,
    ":": 0,
}


class Forth:
    """Forth interpretter."""

    def __init__(self):
        """Initialize."""
        self.stack: list[int] = []
        self.defs: dict[str, list[str]] = {}

    def eval(self, data: list[str]) -> list[int]:
        """Evaluate a program, returning the stack."""
        for line in data:
            self.eval_chunk(line.lower().split())
        return self.stack

    def eval_chunk(self, words: list[str]) -> None:
        """Evaluate a chunk of instructions."""
        instructions = iter(words)
        while (word := next(instructions, None)) is not None:
            # Push numbers to the stack.
            if NUM_RE.match(word):
                self.stack.append(int(word))
                continue

            # Evaluate custom definitions.
            if word in self.defs:
                self.eval_chunk(self.defs[word])
                continue

            # Evaluate built-in operators.
            # Check the operator and stack size.
            if word not in MIN_STACK:
                raise ValueError("undefined operation")
            if len(self.stack) < MIN_STACK[word]:
                raise StackUnderflowError("Insufficient number of items in stack")

            if word in "+-*/":
                self.alu_check(word)
                # Perform the operation using the last two values on the stack.
                self.stack.append(OPS[word](self.stack.pop(-2), self.stack.pop(-1)))
            elif word == "dup":
                self.stack.append(self.stack[-1])
            elif word == "drop":
                self.stack.pop()
            elif word == "swap":
                self.stack.insert(-1, self.stack.pop())
            elif word == "over":
                self.stack.append(self.stack[-2])
            elif word == ":":
                self.parse_definition(instructions)

    def alu_check(self, word):
        """Perform any arithmetic checks needed."""
        if word == "/" and self.stack[-1] == 0:
            raise ZeroDivisionError("divide by zero")

    def parse_definition(self, instructions):
        """Parse and set user defined values."""
        # Read definition name.
        name = next(instructions)
        # Check if the name is an int. Integers cannot be redefined.
        if NUM_RE.match(name):
            raise ValueError("illegal operation")
        # Read instructions until a ";" is found.
        vals = []
        while (cmd := next(instructions)) != ";":
            # Dereference custom definitions.
            if cmd in self.defs:
                vals.extend(self.defs[cmd])
            else:
                vals.append(cmd)
        self.defs[name] = vals


def evaluate(input_data: list[str]) -> list[int]:
    """Evaluate a Forth program."""
    return Forth().eval(input_data)
