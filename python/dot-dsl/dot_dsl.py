"""Parse DOT DSL data."""

import dataclasses


NODE, EDGE, ATTR = range(3)


@dataclasses.dataclass
class Node:
    """Dot node."""
    name: str
    attrs: dict


@dataclasses.dataclass
class Edge:
    """Dot edge."""
    src: str
    dst: str
    attrs: dict


def check_types(name: str, data: list, types: list):
    """Check the data matches the wanted types."""
    if len(data) != len(types):
        raise ValueError(f"{name} is malformed")
    for val, want in zip(data, types):
        if not isinstance(val, want):
            raise ValueError(f"{name} is malformed")


class Graph:
    """Parse a graph."""

    def __init__(self, data=None):
        """Initialize."""
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is None:
            data = []

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")
        if any(len(entry) < 2 for entry in data):
            raise TypeError("Graph item incomplete")

        for entry_type, *rest in data:
            if entry_type == NODE:
                check_types("Node", rest, (str, dict))
                self.nodes.append(Node(*rest))
            elif entry_type == EDGE:
                check_types("Edge", rest, (str, str, dict))
                self.edges.append(Edge(*rest))
            elif entry_type == ATTR:
                check_types("Attribute", rest, (str, str))
                self.attrs[rest[0]] = rest[1]
            else:
                raise ValueError("Unknown item")
