package pov

import (
	"errors"
)

// Tree holds a tree structure.
type Tree struct {
	val    string
	parent *Tree
	// adjacencies = parent + children
	adjacencies []*Tree
}

// New creates and returns a new Tree with the given root value and children.
func New(value string, children ...*Tree) *Tree {
	t := &Tree{value, nil, children}
	for _, c := range children {
		c.adjacencies = append(c.adjacencies, t)
		c.parent = t
	}
	return t
}

// findNode searches downwards (ignoring the parent) for a node.
func (tr *Tree) findNode(value string) (*Tree, error) {
	if tr.Value() == value {
		return tr, nil
	}
	for _, child := range tr.Children() {
		if found, err := child.findNode(value); err == nil {
			return found, nil
		}
	}
	return nil, errors.New("unable to find node")
}

// setParent recursively updates the parent of a tree.
func (tr *Tree) setParent(parent *Tree) {
	tr.parent = parent
	for _, child := range tr.Children() {
		child.setParent(tr)
	}
}

// Value returns the value at the root of a tree.
func (tr *Tree) Value() string {
	return tr.val
}

// Children returns a slice containing the children of a tree.
func (tr *Tree) Children() []*Tree {
	var children []*Tree
	for _, node := range tr.adjacencies {
		if node != tr.parent {
			children = append(children, node)
		}
	}
	return children
}

// FromPov returns the pov from the node specified in the argument.
func (tr *Tree) FromPov(from string) *Tree {
	root, err := tr.findNode(from)
	if err != nil {
		return nil
	}
	root.setParent(nil)
	return root
}

// PathTo returns the shortest path between two nodes in the tree.
// O(n^2) time.
func (tr *Tree) PathTo(from, to string) []string {
	// Validate the from and to exist in the tree.
	if _, err := tr.findNode(from); err != nil {
		return nil
	}
	if _, err := tr.findNode(to); err != nil {
		return nil
	}

	tr = tr.FromPov(from)
	out := []string{tr.Value()}

	// Walk the tree one step at a time towards the "to".
	for ; tr.Value() != to; out = append(out, tr.Value()) {
		for _, child := range tr.Children() {
			// When we find a child leading towards the target, repeat from that child.
			if _, err := child.findNode(to); err == nil {
				tr = child
				break
			}
		}

	}
	return out
}
