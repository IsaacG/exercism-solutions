// Package pangram tests for pangrams.
package pangram

import "strings"

func IsPangram(s string) bool {
	s = strings.ToLower(s)
	for i := 'a'; i <= 'z'; i++ {
		if ! strings.ContainsRune(s, i) {
			return false
		}
	}
	return true
}
