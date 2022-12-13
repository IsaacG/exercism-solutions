"""Parse an SGF tree."""
from __future__ import annotations

import collections
import dataclasses


@dataclasses.dataclass
class SgfTree:
    """SGF Node."""

    properties: dict[str, str] = dataclasses.field(default_factory=dict)
    children: list[SgfTree] = dataclasses.field(default_factory=list)


def parse_node(sgf: str) -> SgfTree:
    """Parse and return a Node."""
    if not sgf.startswith(";"):
        raise ValueError("node must start with ';'")

    idx = 1
    prop_key_start = idx

    properties = collections.defaultdict(list)
    children = []

    while idx < len(sgf):
        match sgf[idx]:
            case "[":
                # Parse property values.
                if idx == prop_key_start:
                    raise ValueError("propery key is empty")
                prop_key = sgf[prop_key_start:idx]
                if not prop_key.isupper():
                    raise ValueError('property must be in uppercase')

                while idx < len(sgf):
                    if sgf[idx] != "[":
                        break

                    # Start of the value.
                    idx += 1
                    prop_val_start = idx
                    while sgf[idx] != "]":
                        idx += 1
                    # End of the value.
                    prop_val = sgf[prop_val_start:idx]
                    prop_val = prop_val.replace("\n", "n").replace("\t", "t")
                    prop_val = prop_val.replace("\\t", " ")
                    properties[prop_key].append(prop_val)

                    idx += 1

                # New property.
                prop_key_start = idx
            case ";":
                # Single child.
                child = parse_node(sgf[idx:])
                children.append(child)
                break
            case "(":
                # Multiple children.
                children = []
                while idx < len(sgf):
                    if sgf[idx] != "(":
                        break
                    # Child start.
                    idx += 1
                    child_start = idx
                    while sgf[idx] != ")":
                        idx += 1
                    # Child end.
                    child = parse_node(sgf[child_start:idx])
                    children.append(child)
                    idx += 1
            case _:
                idx += 1

    if idx > prop_key_start and not properties:
        raise ValueError('properties without delimiter')
    return SgfTree(children=children, properties=dict(properties))


def parse(sgf: str) -> SgfTree:
    """Parse an SGF tree."""
    if not sgf.startswith("(") and not sgf.endswith(")"):
        raise ValueError('tree missing')
    if not sgf.startswith("(;"):
        raise ValueError('tree with no nodes')
    return parse_node(sgf.removeprefix("(").removesuffix(")"))
