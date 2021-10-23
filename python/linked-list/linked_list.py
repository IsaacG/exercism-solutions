"""Doubly linked list."""

from __future__ import annotations
from typing import Callable, Generic, Generator, Optional, TypeVar
NodeValue = TypeVar('NodeValue')


class Node(Generic[NodeValue]):
    """List node."""
    def __init__(self, value: NodeValue):
        """Create a new node."""
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def add_prev(self, value: NodeValue) -> Node:
        """Add a node prior to self."""
        new_node = Node(value)
        assert self.prev is not None
        self.link(self.prev, new_node, self)
        return new_node

    def add_next(self, value: NodeValue) -> Node:
        """Add a node after self."""
        new_node = Node(value)
        assert self.next is not None
        self.link(self, new_node, self.next)
        return new_node

    @staticmethod
    def link(node_a: Node, node_b: Node, node_c: Node) -> None:
        """Set up node linkage between three nodes in a sequence."""
        node_a.next, node_b.next = node_b, node_c
        node_b.prev, node_c.prev = node_a, node_b

    def remove(self) -> NodeValue:
        """Remove a node from the list and return its value."""
        assert self.prev is not None
        assert self.next is not None
        self.next.prev = self.prev
        self.prev.next = self.next
        return self.value


def increment(
    func: Callable[[LinkedList, NodeValue], None]
) -> Callable[[LinkedList, NodeValue], None]:
    """LinkedList increment decorator to bump the length."""

    def wrapper(linked_list: LinkedList, value: NodeValue) -> None:
        func(linked_list, value)
        linked_list.length += 1

    return wrapper


def decrement(func: Callable[[LinkedList], NodeValue]) -> Callable[[LinkedList], NodeValue]:
    """LinkedList decrement decorator to check and reduce the length."""

    def wrapper(linked_list: LinkedList):
        if linked_list.length <= 0:
            raise IndexError("Cannot remove from an empty list.")
        linked_list.length -= 1
        return func(linked_list)

    return wrapper


class LinkedList:
    """A linked list."""

    def __init__(self):
        """Set up a linked list with an empty head and tail node."""
        # Create the head and last nodes.
        self.head = Node(None)
        self.last = Node(None)
        # Link the end nodes.
        self.head.next, self.last.prev = self.last, self.head
        self.length = 0

    @increment
    def push(self, value: NodeValue) -> None:
        """Push a node to the end of the list."""
        self.last.add_prev(value)

    @increment
    def unshift(self, value: NodeValue) -> None:
        """Insert a node at the start of the list."""
        self.head.add_next(value)

    @decrement
    def pop(self) -> NodeValue:
        """Pop a node from the end of the list."""
        return self.last.prev.remove()

    @decrement
    def shift(self) -> NodeValue:
        """Remove a node from the start of the list."""
        return self.head.next.remove()

    def __iter__(self) -> Generator[NodeValue, None, None]:
        """Iterate through the list."""
        cur = self.head.next
        while cur != self.last:
            yield cur.value
            cur = cur.next

    def __str__(self) -> str:
        """Return a string form."""
        return " -> ".join(repr(i) for i in self)

    def __len__(self) -> int:
        """Return the list length."""
        return self.length
