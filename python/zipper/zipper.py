"""Zipper."""


from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    """Tree node."""

    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None
    parent: Optional[Node] = None

    @classmethod
    def from_dict(cls, data: Optional[dict], parent: Optional[Node] = None) -> Optional[Node]:
        """Return a Tree from a dict."""
        if data is None:
            return None
        node = Node(
            value=data["value"],
            parent=parent
        )
        node.left = Node.from_dict(data["left"], parent=node)
        node.right = Node.from_dict(data["right"], parent=node)
        return node

    def to_dict(self):
        """Convert to a dict."""
        return {
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }


class Zipper:
    """A Tree with a Focus."""

    def __init__(self, tree: dict):
        """Build a Tree."""
        root = Node.from_dict(tree)
        if root is None:
            raise ValueError("root needs data")
        self.root = root
        self.focus = root

    @classmethod
    def from_tree(cls, tree: dict) -> Zipper:
        """Return a Tree from a dict."""
        return cls(tree)

    def value(self) -> int:
        """Return the Focus value."""
        return self.focus.value

    def set_value(self, value: int) -> Zipper:
        """Set the Focus value."""
        self.focus.value = value
        return self

    def left(self) -> Optional[Zipper]:
        """Return a Zipper with the Focus on the left."""
        if self.focus.left is None:
            return None
        self.focus = self.focus.left
        return self

    def set_left(self, tree: dict) -> Zipper:
        """Return a Zipper with the left set to a self Tree."""
        self.focus.left = Node.from_dict(tree)
        return self

    def right(self) -> Optional[Zipper]:
        """Return a Zipper with the Focus on the right."""
        if self.focus.right is None:
            return None
        self.focus = self.focus.right
        return self

    def set_right(self, tree: dict) -> Zipper:
        """Return a Zipper with the right set to a self Tree."""
        self.focus.right = Node.from_dict(tree)
        return self

    def up(self) -> Optional[Zipper]:
        """Return a Zipper with the Focus on the parent."""
        if self.focus.parent is None:
            return None
        self.focus = self.focus.parent
        return self

    def to_tree(self) -> dict:
        """Return a dict representation of the Tree."""
        return self.root.to_dict()
