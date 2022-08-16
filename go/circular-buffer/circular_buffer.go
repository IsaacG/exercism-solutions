// Package circular implements a circular buffer.
package circular

import "errors"

// Buffer provides a circular buffer.
type Buffer struct {
	data  []byte
	read  int
	write int
}

// NewBuffer returns a new buffer.
func NewBuffer(size int) *Buffer {
	return &Buffer{data: make([]byte, size + 1)}
}

func (b *Buffer) next(i int) int {
	return (i + 1) % len(b.data)
}

func (b *Buffer) full() bool {
	return b.next(b.write) == b.read
}

func (b *Buffer) empty() bool {
	return b.write == b.read
}

// ReadByte returns the next byte or an error when empty.
func (b *Buffer) ReadByte() (byte, error) {
	if b.empty() {
		return 0, errors.New("Empty")
	}
	data := b.data[b.read]
	b.read = b.next(b.read)
	return data, nil
}

// WriteByte adds a byte to the buffer or returns an error when full.
func (b *Buffer) WriteByte(c byte) error {
	if b.full() {
		return errors.New("Full")
	}
	b.data[b.write] = c
	b.write = b.next(b.write)
	return nil
}

// Overwrite writes a byte. If the buffer is full, the oldest byte is dropped.
func (b *Buffer) Overwrite(c byte) {
	if b.full() {
		b.read = b.next(b.read)
	}
	b.WriteByte(c)
}

// Reset clears the buffer.
func (b *Buffer) Reset() {
	b.read = 0
	b.write = 0
}
