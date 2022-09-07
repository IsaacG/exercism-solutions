package house

import "strings"

var (
	prefix = "This is the "
	segments = []string{
		"horse and the hound and the horn\nthat belonged to",
		"farmer sowing his corn\nthat kept",
		"rooster that crowed in the morn\nthat woke",
		"priest all shaven and shorn\nthat married",
		"man all tattered and torn\nthat kissed",
		"maiden all forlorn\nthat milked",
		"cow with the crumpled horn\nthat tossed",
		"dog\nthat worried",
		"cat\nthat killed",
		"rat\nthat ate",
		"malt\nthat lay in",
		"house that Jack built.",
	}
)

func Verse(v int) string {
	parts := segments[len(segments) - v:]
	return prefix + strings.Join(parts, " the ")
}

func Song() string {
	parts := make([]string, len(segments))
	for i := 0; i < len(segments); i++ {
		parts[i] = Verse(i+1)
	}
	return strings.Join(parts, "\n\n")
}
