"""Implement a linked list."""
from __future__ import annotations
from typing import Generator, Generic, Iterable, Optional, TypeVar


class EmptyListException(Exception):
    """Exception raised when accessing an empty list."""


NodeVal = TypeVar("NodeVal")


class Node(Generic[NodeVal]):
    """Doubly-linked list node."""
    def __init__(self, value: NodeVal, next_node: Optional[Node] = None):
        self._value = value
        self._next = next_node

    def value(self) -> NodeVal:
        """Return node value."""
        return self._value

    def next(self) -> Optional[Node]:
        """Return next node."""
        return self._next


class LinkedList:
    """Linked list."""
    def __init__(self, values: Iterable[NodeVal] = ()):
        self._head: Optional[Node] = None
        # Push the items to the list. list(LinkedList([1, 2, 3])) == [3, 2, 1]
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        """Return the list length by walking the list."""
        return sum(1 for _ in self)

    def head(self) -> Node:
        """Return the first node."""
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: NodeVal) -> None:
        """Push a value to the front of the list."""
        self._head = Node(value, self._head)

    def pop(self) -> NodeVal:
        """Pop a value from the front of the list."""
        if self._head is None:
            raise EmptyListException("The list is empty.")
        node = self._head
        self._head = node.next()
        return node.value()

    def reversed(self) -> LinkedList:
        """Reverse a list by pushing the elements in order."""
        return LinkedList(self)

    def __iter__(self) -> Generator[NodeVal, None, None]:
        """Yield the values in the list."""
        node = self._head
        while node:
            yield node.value()
            node = node.next()
