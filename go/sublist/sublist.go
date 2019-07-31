// Package sublist checks for sublists.
package sublist

// Relation describes how lists are related.
type Relation string

func startswith(a, b []int) bool {
	for i, v := range b {
		if v != a[i] {
			return false
		}
	}
	return true
}

// Sublist returns a Relation: equal, unequal, sublist or superlist.
func Sublist(a, b []int) Relation {
	if len(a) == len(b) && startswith(a, b) {
		return "equal"
	}

	// a is the longer list. Check that b is in a.
	swapped := len(a) < len(b)
	r := Relation("superlist")
	if swapped {
		a, b = b, a
		r = Relation("sublist")
	}

	for i := 0; i <= len(a)-len(b); i++ {
		if startswith(a[i:], b) {
			return r
		}
	}
	return "unequal"
}
