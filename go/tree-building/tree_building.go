// Package tree builds trees.
package tree

import (
	"errors"
	"sort"
)

// Record stores a DB record.
type Record struct {
	ID     int
	Parent int
}

// Node represents a tree node.
type Node struct {
	ID       int
	Children []*Node
}

// Build generates a tree of nodes from a list of records.
func Build(records []Record) (*Node, error) {
	nodes := make(map[int]*Node)
	children := make(map[int]sort.IntSlice)

	for _, r := range records {
		if _, ok := nodes[r.ID]; ok {
			return nil, errors.New("node defined twice")
		}
		if r.ID < r.Parent || (r.ID == r.Parent && r.ID != 0) {
			return nil, errors.New("parent ID must be smaller than child")
		}
		if r.ID == 0 && r.Parent != 0 {
			return nil, errors.New("root node cannot have a parent")
		}
		nodes[r.ID] = &Node{r.ID, nil}
		children[r.Parent] = append(children[r.Parent], r.ID)
	}

	for i := 0; i < len(children); i++ {
		if _, ok := children[i]; !ok {
			return nil, errors.New("non-continuous IDs")
		}
	}

	for p, cs := range children {
		p, ok := nodes[p]
		if !ok {
			return nil, errors.New("invalid parent referenced")
		}
		cs.Sort()
		for _, c := range cs {
			if c == 0 {
				continue
			}
			p.Children = append(p.Children, nodes[c])
		}
	}
	return nodes[0], nil
}
