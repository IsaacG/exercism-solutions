"""Binary Tree."""

from __future__ import annotations
from typing import Optional


class TreeNode:
    """Binary Tree Node."""

    def __init__(
        self,
        data: Optional[int],
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None
    ):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"

    def insert(self, value: int) -> None:
        """Insert a value into the tree."""
        if self.data is None:
            self.data = value
        elif value > self.data:
            if self.right is None:
                self.right = TreeNode(None)
            self.right.insert(value)
        else:
            if self.left is None:
                self.left = TreeNode(None)
            self.left.insert(value)

    def sorted(self) -> list[int]:
        """Return node values, sorted."""
        if self.data is None:
            return []
        data = []
        if self.left:
            data.extend(self.left.sorted())
        data.append(self.data)
        if self.right:
            data.extend(self.right.sorted())
        return data


class BinarySearchTree:
    """Binary Tree."""

    def __init__(self, tree_data: list[int]):
        """Initialize."""
        self.root = TreeNode(None)
        for value in tree_data:
            self.root.insert(value)
            print(f"Insert {value=} => {self.root}")

    def data(self) -> TreeNode:
        """Return Tree data."""
        return self.root

    def sorted_data(self) -> list[int]:
        """Return sorted data."""
        return self.root.sorted()
