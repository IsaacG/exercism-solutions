package foodchain

import (
	"fmt"
	"strings"
)

type data struct {
	object      string
	subject     string
	description string
}

func (d data) subj() string {
	if len(d.subject) > 0 {
		return d.subject
	}
	return d.object
}

var reactions = []data{
	data{"fly", "", "I don't know why she swallowed the fly. Perhaps she'll die."},
	data{"spider", "spider that wriggled and jiggled and tickled inside her", "It wriggled and jiggled and tickled inside her."},
	data{"bird", "", "How absurd to swallow a bird!"},
	data{"cat", "", "Imagine that, to swallow a cat!"},
	data{"dog", "", "What a hog, to swallow a dog!"},
	data{"goat", "", "Just opened her throat and swallowed a goat!"},
	data{"cow", "", "I don't know how she swallowed a cow!"},
	data{"horse", "", "She's dead, of course!"},
}

func Verse(v int) string {
	parts := make([]string, 0, v+2)
	parts = append(parts, fmt.Sprintf("I know an old lady who swallowed a %s.", reactions[v-1].object))
	if v > 1 {
		parts = append(parts, reactions[v-1].description)
	}
	if v < len(reactions) {
		for i := v - 1; i > 0; i-- {
			parts = append(parts, fmt.Sprintf("She swallowed the %s to catch the %s.", reactions[i].object, reactions[i-1].subj()))
		}
		parts = append(parts, reactions[0].description)
	}
	return strings.Join(parts, "\n")
}

func Verses(start, end int) string {
	parts := make([]string, end-start+1)
	for i := start; i <= end; i++ {
		parts[i-start] = Verse(i)
	}
	return strings.Join(parts, "\n\n")
}

func Song() string {
	return Verses(1, len(reactions))
}
