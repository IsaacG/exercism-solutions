// Package linkedlist provides a linked list.
package linkedlist

import (
	"errors"
	"fmt"
)

// Element is an item in the List.
type Element struct {
	Value  interface{}
	prev *Element
	next *Element
}

// List is a linked list of Elements.
type List struct {
	head *Element
	tail *Element
}

func (e Element) String() string {
	return fmt.Sprintf("%s", e.Value)
}

func (l List) String() string {
	if l.isEmpty() {
		return "(empty)"
	}
	e := l.head
	s := e.String()
	for e := l.head.next; e != nil; e = e.next {
		s += " - " + e.String()
	}
	return s
}

// ErrEmptyList is the error when an empty list is used.
var ErrEmptyList = errors.New("err empty list")

// Next returns the next element.
func (e *Element) Next() *Element {
	return e.next
}

// Prev returns the previous element.
func (e *Element) Prev() *Element {
	return e.prev
}

// NewList returns a new list, populated with the values provided.
func NewList(args ...interface{}) *List {
	l := &List{}
	for _, e := range args {
		l.Push(e)
	}
	return l
}

// PushFront pushes an element to the front of the list.
func (l *List) Unshift(v interface{}) {
	e := &Element{Value: v}
	if l.isEmpty() {
		l.head = e
		l.tail = e
		return
	}
	e.next = l.head
	l.head.prev = e
	l.head = e
}

// Push pushes an element to the back of the list.
func (l *List) Push(v interface{}) {
	e := &Element{Value: v}
	if l.isEmpty() {
		l.head = e
		l.tail = e
		return
	}
	e.prev = l.tail
	l.tail.next = e
	l.tail = e
}

// PopFront pops an element from the front of the list.
func (l *List) Shift() (interface{}, error) {
	if l.isEmpty() {
		// Unit tests expect int(0) for the default here.
		return int(0), ErrEmptyList
	}
	v := l.head.Value
	l.head = l.head.next
	if l.head == nil {
		l.tail = nil
	} else {
		l.head.prev = nil
	}
	return v, nil
}

// PopBack pops an element from the back of the list.
func (l *List) Pop() (interface{}, error) {
	if l.isEmpty() {
		// Unit tests expect int(0) for the default here.
		return int(0), ErrEmptyList
	}
	v := l.tail.Value
	l.tail = l.tail.prev
	if l.tail == nil {
		l.head = nil
	} else {
		l.tail.next = nil
	}
	return v, nil
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
func (l *List) First() *Element {
	return l.head
}

// Last returns the last element of a list.
func (l *List) Last() *Element {
	return l.tail
}

func (l *List) isEmpty() bool {
	return l.head == nil
}
