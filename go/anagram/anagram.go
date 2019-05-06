// Package anagram computes anagrams.
package anagram

import "strings"

type CharCount map[rune]int

func Count(s string) CharCount {
	count := make(CharCount)
	for _, r := range strings.ToLower(s) {
		count[r]++
	}
	return count
}

func (c CharCount) Equal(other CharCount) bool {
	if len(c) != len(other) {
		return false
	}
	for r, n := range c {
		if n != other[r] {
			return false
		}
	}
	return true
}

func Detect(s string, cs []string) []string {
	var res []string
	count := Count(s)
	for _, c := range cs {
		if strings.ToLower(s) == strings.ToLower(c) {
			continue
		}
		if count.Equal(Count(c)) {
			res = append(res, c)
		}
	}
	return res
}
