// Package luhn checks if a number satisfies the Luhn requirements.
package luhn

import (
	"strconv"
	"strings"
)

// Valid checks is the string s contains a valid Luhn number, wherein every other digit is doubled and the sum must be divisible by 10.
func Valid(s string) bool {
	s = strings.ReplaceAll(s, " ", "")
	if len(s) <= 1 {
		return false
	}
	var sum int
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
