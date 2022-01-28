"""Circular buffer."""


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""


class CircularBuffer:
    """Implement a circular buffer."""

    _read: int
    _write: int

    def __init__(self, capacity: int):
        """Initialize a buffer."""
        self._len = capacity + 1
        self.clear()

    def _next(self, pos: int) -> int:
        """Return the next position."""
        return (pos + 1) % self._len

    @property
    def full(self) -> bool:
        """Return if the buffer is full."""
        return self._read == self._next(self._write)

    @property
    def empty(self) -> bool:
        """Return if the buffer is empty."""
        return self._read == self._write

    def read(self) -> str:
        """Return the next value in the buffer."""
        if self.empty:
            raise BufferEmptyException("Circular buffer is empty")
        data = self._data[self._read]
        self._read = self._next(self._read)
        return data

    def write(self, data: str) -> None:
        """Write a value to the buffer."""
        if self.full:
            raise BufferFullException("Circular buffer is full")
        self._data[self._write] = data
        self._write = self._next(self._write)

    def overwrite(self, data: str) -> None:
        """Write a value to the buffer, overwriting when full."""
        if self.full:
            self.read()
        self.write(data)

    def clear(self):
        """Reset the buffer."""
        self._data = [None] * self._len
        self._read = 0
        self._write = 0
