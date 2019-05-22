// Package cryptosquare solves cryptosquare.
package cryptosquare

import (
	"math"
	"strings"
	"unicode"
)

// Encode the string.
func Encode(s string) string {
	var normalized = make([]rune, 0, len(s))
	var l, c, r int
	// Normalize the string - lowercase and discard unless letter or digit.
	for _, c := range strings.ToLower(s) {
		if unicode.IsLetter(c) || unicode.IsDigit(c) {
			normalized = append(normalized, c)
		}
	}

	// Computer size and pad with spaces.
	l = len(normalized)
	c = int(math.Ceil(math.Sqrt(float64(l))))
	if (c * (c - 1)) >= l {
		r = c - 1
	} else {
		r = c
	}
	for len(normalized) < c*r {
		normalized = append(normalized, ' ')
	}

	// Build chunks of output.
	chunks := make([]string, c)
	for i := 0; i < c; i++ {
		chunk := make([]rune, r)
		for j := 0; j < r; j++ {
			chunk[j] = normalized[i+j*c]
		}
		chunks[i] = string(chunk)
	}

	return strings.Join(chunks, " ")
}
