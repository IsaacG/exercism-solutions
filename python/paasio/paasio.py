"""Wrap some IO objects with counters."""

from __future__ import annotations

import io
import socket
from typing import Optional


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        """Initialize."""
        super().__init__(*args, **kwargs)
        self._read_ops = 0
        self._read_bytes = 0
        self._write_ops = 0
        self._write_bytes = 0

    def __enter__(self) -> MeteredFile:
        """Enter context."""
        return self

    def __iter__(self) -> MeteredFile:
        """Return an iterator."""
        return self

    def __next__(self) -> bytes:
        """Read and return the next line."""
        data = super().readline()
        self._read_ops += 1
        self._read_bytes += len(data)
        if not data:
            raise StopIteration
        return data

    def read(self, *args, **kwargs) -> bytes:
        """Read and return data."""
        data = super().read(*args, **kwargs)
        self._read_ops += 1
        self._read_bytes += len(data)
        return data

    @property
    def read_bytes(self) -> int:
        """Return number of bytes read."""
        return self._read_bytes

    @property
    def read_ops(self) -> int:
        """Return number of read ops."""
        return self._read_ops

    def write(self, b) -> int:
        """Write data."""
        res = super().write(b)
        self._write_ops += 1
        self._write_bytes += res
        return res

    @property
    def write_bytes(self) -> int:
        """Return number of bytes written."""
        return self._write_bytes

    @property
    def write_ops(self) -> int:
        """Return number of write ops."""
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, sock: socket.socket):
        self._socket = sock
        self._read_ops = 0
        self._read_bytes = 0
        self._write_ops = 0
        self._write_bytes = 0

    def __enter__(self) -> MeteredSocket:
        return self

    def __exit__(self, *args, **kwargs) -> Optional[bool]:
        return self._socket.__exit__(*args, **kwargs)

    def recv(self, bufsize: int, *args, **kwargs) -> bytes:
        """Read and return data."""
        data = self._socket.recv(bufsize, *args, **kwargs)
        self._read_ops += 1
        self._read_bytes += len(data)
        return data

    @property
    def recv_bytes(self) -> int:
        """Return number of bytes read."""
        return self._read_bytes

    @property
    def recv_ops(self) -> int:
        """Return number of read ops."""
        return self._read_ops

    def send(self, *args, **kwargs) -> int:
        """Write data."""
        count = self._socket.send(*args, **kwargs)
        self._write_ops += 1
        self._write_bytes += count
        return count

    @property
    def send_bytes(self) -> int:
        """Return number of bytes written."""
        return self._write_bytes

    @property
    def send_ops(self) -> int:
        """Return number of write ops."""
        return self._write_ops
