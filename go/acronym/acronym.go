// Package acronym solves acronym
package acronym

import (
	"strings"
)

// Abbreviate a string.
func Abbreviate(s string) string {
	s = strings.ReplaceAll(s, "-", " ")
	s = strings.ReplaceAll(s, "_", " ")
	s = strings.ToUpper(s)
	var out []byte
	for _, word := range strings.Split(s, " ") {
		if len(word) > 0 {
			out = append(out, word[0])
		}
	}
	return string(out)
}
