// Package raindrops converts water to noise.
package raindrops

import (
	"strconv"
	"strings"
)

var sounds = []struct {
	div   int
	sound string
}{
	{
		div:   3,
		sound: "Pling",
	},
	{
		div:   5,
		sound: "Plang",
	},
	{
		div:   7,
		sound: "Plong",
	},
}

// Convert a number to its sound
func Convert(i int) string {
	var sb strings.Builder
	for _, s := range sounds {
		if i%s.div == 0 {
			sb.WriteString(s.sound)
		}
	}
	if sb.Len() == 0 {
		sb.WriteString(strconv.Itoa(i))
	}
	return sb.String()
}
