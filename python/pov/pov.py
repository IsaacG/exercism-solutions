"""Tree POV."""


from __future__ import annotations
from typing import Generator, Optional


class Tree:
    """A Tree which can be reoriented."""

    def __init__(self, label: str, children: Optional[list[Tree]] = None):
        """Initialize a Tree Node."""
        self.label = label
        self.children = children or []
        self.parent = None
        for child in self.children:
            child.parent = self

    def __hash__(self) -> int:
        return hash(id(self))

    def __repr__(self) -> str:
        children = ", ".join(str(child) for child in self.children)
        return f"Tree({self.label!r}, children=[{children}])"

    def __lt__(self, other: Tree) -> bool:
        return self.label < other.label

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tree):
            return NotImplemented
        return self.label == other.label and sorted(self.children) == sorted(other.children)

    def find(self, label: str) -> Optional[Tree]:
        """Recursively search for a node by label."""
        if self.label == label:
            return self
        for child in self.children:
            if found := child.find(label):
                return found
        return None

    def adjacent(self) -> Generator[Tree, None, None]:
        """Return all adjacent nodes (parent + children)."""
        if self.parent:
            yield self.parent
        yield from self.children

    def children_from(self, parent: Optional[str]) -> list[Tree]:
        """Return children of `self`, assuming parent."""
        return [
            Tree(child.label, child.children_from(self.label))
            for child in self.adjacent()
            if child.label != parent
        ]

    def from_pov(self, from_node: str) -> Tree:
        """Build a Tree from a specific POV."""
        if not (start := self.find(from_node)):
            raise ValueError("Tree could not be reoriented")
        return Tree(start.label, start.children_from(None))

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        """Return the path between two nodes."""
        if not (start := self.find(from_node)):
            raise ValueError("Tree could not be reoriented")

        path = {start.label: [start.label]}

        # Explore all nodes breadth first begining with from_node until to_node.
        to_explore = {start}
        while to_explore:
            # Explore another node.
            current = to_explore.pop()
            # If this is the destination, return the path to here.
            if current.label == to_node:
                return path[current.label]
            for neighbor in current.adjacent():
                if neighbor.label in path:
                    continue
                # Update the path to this node and add it to be explored.
                path[neighbor.label] = path[current.label] + [neighbor.label]
                to_explore.add(neighbor)

        raise ValueError("No path found")
