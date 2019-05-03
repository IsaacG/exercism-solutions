// Package reverse solves reverse
package reverse

import "strings"

func String(s string) string {
	// Unpack runes into a slice of runes.
	runes := make([]rune, 0, len(s))
	for read := strings.NewReader(s);; {
		if r, _, err := read.ReadRune(); err == nil {
			runes = append(runes, r)
		} else {
			break
		}
	}

	// Reverse read runes into a string builder.
	var build strings.Builder
	build.Grow(len(s))
	for i, _ := range runes {
		build.WriteRune(runes[len(runes) - i - 1])
	}
	return build.String()
}
