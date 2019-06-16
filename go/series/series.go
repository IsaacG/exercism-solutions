// Package series solves the series exercise.
package series

// All returns a list of all substrings of s with length n.
func All(n int, s string) (out []string) {
	for i := 0; i+n <= len(s); i++ {
		out = append(out, s[i:i+n])
	}
	return out

}

// UnsafeFirst returns the first substring of s with length n.
func UnsafeFirst(n int, s string) string {
	return All(n, s)[0]
}

// First returns the first substring of s with length n and an `ok`.
// Test with `go test -tags first`.
func First(n int, s string) (first string, ok bool) {
	all := All(n, s)
	if len(all) == 0 {
		return "", false
	}
	return all[0], true
}
