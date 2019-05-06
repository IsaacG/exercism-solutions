// Package wordcount counts words.
package wordcount

import (
	"regexp"
	"strings"
)

var word = regexp.MustCompile(`[[:alnum:]']+\b`)

type Frequency map[string]int

func (f Frequency) Add(s string) {
	s = strings.ToLower(s)
	s = strings.Trim(s, "'")
	f[s]++
}

func WordCount (s string) Frequency {
	f := Frequency{}
	for _, w := range word.FindAllString(s, -1) {
		f.Add(w)
	}
	return f
}
