// Package luhn checks if a number satisfies the Luhn requirements.
package luhn

import (
	"strconv"
	"strings"
)

// Valid Luhn number or not?
func Valid(s string) bool {
	sum := 0
	s = strings.ReplaceAll(s, " ", "")
	if len(s) <= 1 {
		return false
	}
	if len(s)%2 == 1 {
		s = "0" + s
	}
	for i, c := range s {
		v, err := strconv.Atoi(string(c))
		if err != nil {
			return false
		}
		if i%2 == 0 {
			v *= 2
			if v > 9 {
				v -= 9
			}
		}
		sum += v
	}
	return sum%10 == 0
}
