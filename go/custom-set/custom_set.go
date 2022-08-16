package stringset

import "strings"

// Implement Set as a collection of unique string values.
//
// For Set.String, use '{' and '}', output elements as double-quoted strings
// safely escaped with Go syntax, and use a comma and a single space between
// elements. For example, a set with 2 elements, "a" and "b", should be formatted as {"a", "b"}.
// Format the empty set as {}.

// Set provides a StringSet.
type Set map[string]struct{}

// New returns a new empty Set.
func New() Set {
	return Set{}
}

// NewFromSlice returns a new Set populated with data from a slice.
func NewFromSlice(l []string) Set {
	s := New()
	for _, v := range l {
		s.Add(v)
	}
	return s
}

// String stringifies a Set.
func (s Set) String() string {
	b := strings.Builder{}
	b.WriteString(`{`)
	first := true
	for k := range s {
		if first {
			b.WriteString(`"`)
			first = false
		} else {
			b.WriteString(`, "`)
		}
		b.WriteString(k)
		b.WriteString(`"`)
	}
	b.WriteString(`}`)
	return b.String()
}

// IsEmpty returns if a Set is empty.
func (s Set) IsEmpty() bool {
	return len(s) == 0
}

// Has returns if a Set has an element.
func (s Set) Has(elem string) bool {
	_, ok := s[elem]
	return ok
}

// Add adds an element to a Set.
func (s Set) Add(elem string) {
	s[elem] = struct{}{}
}

// Subset returns if s1 is a subset of s2.
func Subset(s1, s2 Set) bool {
	for k := range s1 {
		if !s2.Has(k) {
			return false
		}
	}
	return true
}

// Equal returns if s1 is the same as s2.
func Equal(s1, s2 Set) bool {
	return Subset(s1, s2) && len(s1) == len(s2)
}

// Disjoint returns if s1 and s2 are disjoint (no common elements).
func Disjoint(s1, s2 Set) bool {
	return Intersection(s1, s2).IsEmpty()
}

// Intersection returns the intersection of s1 and s2.
func Intersection(s1, s2 Set) Set {
	s := New()
	for k := range s1 {
		if s2.Has(k) {
			s.Add(k)
		}
	}
	return s
}

// Difference returns the difference of s1 and s2.
func Difference(s1, s2 Set) Set {
	s := New()
	for k := range s1 {
		if !s2.Has(k) {
			s.Add(k)
		}
	}
	return s
}

// Union returns the union of s1 and s2.
func Union(s1, s2 Set) Set {
	s := New()
	for k := range s1 {
		s.Add(k)
	}
	for k := range s2 {
		s.Add(k)
	}
	return s
}
