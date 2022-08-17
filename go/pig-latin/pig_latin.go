package piglatin

import (
	"regexp"
	"strings"
)

// Rule maps specific string patterns to specific Pig Latin replacement rules.
type Rule struct {
	Test    *regexp.Regexp
	Pattern *regexp.Regexp
}

var rules = []Rule{
	// xr and yt are special; just add "ay".
	Rule{regexp.MustCompile(`^((?:xr|yt).*)`), regexp.MustCompile(`((?:xr|yt).*)()`)},
	// If the starts contains "qu", do not split on "u".
	Rule{regexp.MustCompile(`^[^aeiou]*qu`), regexp.MustCompile(`([^aeioy]*)([aeioy].*)`)},
	// If the word starts with a "y", keep "y" in the start.
	Rule{regexp.MustCompile(`^y`), regexp.MustCompile(`([^aeiou]*)([aeiou].*)`)},
	// Default is to split at the first vowel.
	Rule{regexp.MustCompile(``), regexp.MustCompile(`([^aeiouy]*)([aeiouy].*)`)},
}

// Word converts one word to Pig Latin.
func Word(word string) string {
	for _, rule := range rules {
		if rule.Test.MatchString(word) {
			parts := rule.Pattern.FindStringSubmatch(word)
			return parts[2] + parts[1] + "ay"
		}
	}
	panic("should have matched a rule")
}

// Sentence converts a whole sentence to Pig Latin.
func Sentence(sentence string) string {
	words := strings.Split(sentence, " ")
	for i, word := range words {
		words[i] = Word(word)
	}
	return strings.Join(words, " ")
}
