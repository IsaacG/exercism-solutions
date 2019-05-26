// Package atbash does at-bash cipher.
package atbash

import (
	"strings"
	"unicode"
)

// Atbash does the at-bash cipher.
func Atbash(s string) string {
	s = strings.ToLower(s)
	out := make([]rune, 0, int(1.2*float64(len(s)+1)))
	count := 0
	for _, r := range s {
		if !(unicode.IsDigit(r) || unicode.IsLetter(r)) {
			continue
		}
		if count != 0 && count%5 == 0 {
			out = append(out, ' ')
		}
		count++
		if unicode.IsDigit(r) {
			out = append(out, r)
		} else {
			out = append(out, rune(25-int(r-'a'))+'a')
		}
	}
	return string(out)
}
