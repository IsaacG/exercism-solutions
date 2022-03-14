"""Binary Tree."""

from __future__ import annotations
from typing import cast, Generator, Generic, Iterable, Optional, TypeVar


T = TypeVar("T")


class TreeNode(Generic[T]):
    """Binary Tree Node."""

    def __init__(
        self,
        data: Optional[T],
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None
    ):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation."""
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"

    def insert(self, value: T) -> None:
        """Insert a value into the tree."""
        if self.data is None:
            self.data = value
        elif value > self.data:  # type: ignore
            if self.right is None:
                self.right = TreeNode(None)
            self.right.insert(value)
        else:
            if self.left is None:
                self.left = TreeNode(None)
            self.left.insert(value)

    def __iter__(self) -> Generator[T, None, None]:
        """Return node values, sorted."""
        yield from self.left or []
        # if self.data is None: return
        # or this can be checked once in sorted_data() and assumed to exist here.
        yield cast(T, self.data)
        yield from self.right or []


class BinarySearchTree(Generic[T]):
    """Binary Tree."""

    def __init__(self, tree_data: Iterable[T]):
        """Initialize."""
        self.root: TreeNode[T] = TreeNode(None)
        for value in tree_data:
            self.root.insert(value)

    def data(self) -> TreeNode[T]:
        """Return Tree data."""
        return self.root

    def sorted_data(self) -> list[T]:
        """Return sorted data."""
        if self.root.data is None:
            return []
        return list(self.root)
