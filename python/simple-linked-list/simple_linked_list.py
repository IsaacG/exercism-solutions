class Node:
    """Doubly-linked list node."""
    def __init__(self, value):
        self._value = value
        self._prev = None
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self.__next__()

    def __next__(self):
        return self._next


class LinkedList:
    """Linked list."""
    def __init__(self, values=[]):
        self._head = None
        self._tail = None
        # Push the items to the list. list(LinkedList([1, 2, 3])) == [3, 2, 1]
        for v in values:
            self.push(v)

    def __len__(self):
        """Return the list length by walking the list."""
        node = self._head
        count = 0
        while node:
            count += 1
            node = node._next
        return count

    def head(self):
        """Return the first node."""
        if self._head:
            return self._head
        raise EmptyListException("No data")

    def push(self, value):
        """Push a value to the front of the list."""
        node = Node(value)
        node._next = self._head
        self._head = node
        if node._next:
            node._next._prev = node
        else:
            self._tail = node

    def pop(self):
        """Pop a value from the front of the list."""
        if self._head is None:
            raise EmptyListException("Empty")
        node = self._head
        self._head = node._next
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        return node.value()

    def reversed(self):
        """Reverse a list by pushing the elements in order."""
        ll = LinkedList()
        for value in self:
            ll.push(value)
        return ll

    def __iter__(self):
        """Yield the values in the list."""
        node = self._head
        while node:
            yield node.value()
            node = node._next


class EmptyListException(Exception):
    pass
