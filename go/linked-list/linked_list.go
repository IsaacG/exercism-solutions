// Package linkedlist provides a linked list.
package linkedlist

import (
	"errors"
)

// Node is an item in the List.
type Node struct {
	Value any
	prev  *Node
	next  *Node
}

// List is a linked list of Node.
type List struct {
	head *Node
	tail *Node
}

// ErrEmptyList is the error when an empty list is used.
var ErrEmptyList = errors.New("err empty list")

// Next returns the next element.
func (e *Node) Next() *Node {
	if e.next == nil || e.next.next == nil {
		return nil
	}
	return e.next
}

// Prev returns the previous element.
func (e *Node) Prev() *Node {
	if e.prev == nil || e.prev.prev == nil {
		return nil
	}
	return e.prev
}

func (e *Node) link() {
	e.next.prev = e
	e.prev.next = e
}

func (e *Node) unlink() any {
	e.next.prev, e.prev.next = e.prev, e.next
	return e.Value
}

// NewList returns a new list, populated with the values provided.
func NewList(args ...any) *List {
	l := &List{&Node{}, &Node{}}
	l.head.next = l.tail
	l.tail.prev = l.head
	for _, e := range args {
		l.Push(e)
	}
	return l
}

// PushFront pushes an element to the front of the list.
func (l *List) Unshift(v any) {
	(&Node{Value: v, prev: l.head, next: l.head.next}).link()
}

// Push pushes an element to the back of the list.
func (l *List) Push(v any) {
	(&Node{Value: v, prev: l.tail.prev, next: l.tail}).link()
}

// PopFront pops an element from the front of the list.
func (l *List) Shift() (any, error) {
	if l.isEmpty() {
		return nil, ErrEmptyList
	}
	return l.First().unlink(), nil
}

// PopBack pops an element from the back of the list.
func (l *List) Pop() (any, error) {
	if l.isEmpty() {
		return nil, ErrEmptyList
	}
	return l.Last().unlink(), nil
}

// Reverse returns a new list, reversed.
func (l *List) Reverse() *List {
	for e := l.head; e != nil; e = e.prev {
		e.prev, e.next = e.next, e.prev
	}
	l.head, l.tail = l.tail, l.head
	return l
}

// First returns the first element of a list.
func (l *List) First() *Node {
	if l.isEmpty() {
		return nil
	}
	return l.head.next
}

// Last returns the last element of a list.
func (l *List) Last() *Node {
	if l.isEmpty() {
		return nil
	}
	return l.tail.prev
}

func (l *List) isEmpty() bool {
	return l.head.next == l.tail
}
