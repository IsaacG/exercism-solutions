// Package rotationalcipher rotates.
package rotationalcipher

import (
	"strings"
	"unicode"
)

// RotationalCipher rotates a string.
func RotationalCipher(s string, d int) string {
	return strings.Map(func(r rune) rune {
		var a rune
		if !unicode.IsLetter(r) {
			return r
		} else if unicode.IsUpper(r) {
			a = 'A'
		} else {
			a = 'a'
		}
		return rune((int(r-a)+d)%26) + a
	}, s)
}
