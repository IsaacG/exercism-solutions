// Package isbn checks for valid ISBNs
package isbn

import (
	"strconv"
	"strings"
)

func IsValidISBN(s string) bool {
	s = strings.ReplaceAll(s, "-", "")
	if len(s) != 10 {
		return false
	}

	var sum, v int
	for i, c := range s {
		if i == 9 && c == 'X' {
			v = 10
		} else {
			var err error
			v, err = strconv.Atoi(string(c))
			if err != nil {
				return false
			}
		}
		sum += v * (10 - i)
	}
	return sum % 11 == 0
}

