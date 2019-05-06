// Package encode does runlength encoding/decoding.
package encode

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

var repeated = regexp.MustCompile(`^(\d+)(\D)`)

func enc(r rune, c int) string {
	if c == 0 {
		return ""
	} else if c == 1 {
		return string(r)
	} else {
		return fmt.Sprintf("%d%c", c, r)
	}
}

// RunLengthEncode encodes.
func RunLengthEncode(s string) string {
	var res string
	var last rune
	var count int
	for _, c := range s {
		if c == last {
			count++
		} else {
			res += enc(last, count)
			count = 1
			last = c
		}
	}
	res += enc(last, count)
	return res
}

// RunLengthDecode decodes.
func RunLengthDecode(s string) string {
	var res string
	for i := 0; i < len(s); i++ {
		matches := repeated.FindStringSubmatch(s[i:])
		if len(matches) == 0 {
			res += string(s[i])
			continue
		}
		n, _ := strconv.Atoi(matches[1])
		res += strings.Repeat(matches[2], n)
		i += len(matches[1])
	}
	return res
}
