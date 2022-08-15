// Package isogram checks for isograms.
package isogram

import (
	"strings"
	"unicode"
)

// IsIsogram determines if a string is an isogram.
func IsIsogram(s string) bool {
	found := make(map[rune]bool)
	for _, r := range strings.ToUpper(s) {
		if !unicode.IsLetter(r) {
			continue
		}
		if found[r] {
			return false
		}
		found[r] = true
	}
	return true
}
