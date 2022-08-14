package binarysearchtree

// BinarySearchTree is a search tree.
type BinarySearchTree struct {
	data  int
	left  *BinarySearchTree
	right *BinarySearchTree
}

// Bst returns a new tree.
func Bst(d int) *BinarySearchTree {
	return &BinarySearchTree{data: d}
}

// NewBst returns a new BinarySearchTree.
func NewBst(data int) *BinarySearchTree {
	return &BinarySearchTree{data: data}
}

// Insert an element into the tree.
func (s *BinarySearchTree) Insert(d int) {
	if d <= s.data {
		if s.left != nil {
			s.left.Insert(d)
		} else {
			s.left = Bst(d)
		}
	} else {
		if s.right != nil {
			s.right.Insert(d)
		} else {
			s.right = Bst(d)
		}
	}
}

// MapString applies a string mapper to the tree.
func (s *BinarySearchTree) MapString(f func(int) string) []string {
	var r []string
	if s.left != nil {
		r = s.left.MapString(f)
	}
	r = append(r, f(s.data))
	if s.right != nil {
		for _, m := range s.right.MapString(f) {
			r = append(r, m)
		}
	}
	return r
}

// MapInt applies an int mapper to the tree.
func (s *BinarySearchTree) MapInt(f func(int) int) []int {
	var r []int
	if s.left != nil {
		r = s.left.MapInt(f)
	}
	r = append(r, f(s.data))
	if s.right != nil {
		for _, m := range s.right.MapInt(f) {
			r = append(r, m)
		}
	}
	return r
}

// SortedData returns tree data in a sorted array.
func (s *BinarySearchTree) SortedData() []int {
	return s.MapInt(func(d int) int { return d })
}
