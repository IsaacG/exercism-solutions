// Package romannumerals does stuff?
package romannumerals

import (
	"errors"
	"regexp"
	"strings"
)

var (
	val = map[rune]int {
		'M': 1000,
		'D': 500,
		'C': 100,
		'L': 50,
		'X': 10,
		'V': 5,
		'I': 1,
		'0': 0,
	}
	// These maps could be generated from one another.
	rom = map[int]rune {
		1000: 'M',
		500: 'D',
		100: 'C',
		50: 'L',
		10: 'X',
		5: 'V',
		1: 'I',
		0: '0',
	}
	valid = regexp.MustCompile("^M{0,3}(C?[DM])?C{0,3}(X?[LC])?X{0,3}(I?[VX])?I{0,3}$")
)

func FromRomanNumeral(s string) int {
	if ! valid.MatchString(s) {
		println("Invalid roman numberal input")
		return 0
	}
	s = s + "0"
	var parts []int
	l := 0
	c := '0'
	// Walk the string and look for where we go from MMM to C or other breaks in repeats.
	for _, v := range s {
		// Changing characters! Chunk here.
		if v != c {
			if l != 0 {
				parts = append(parts, val[c] * l)
			}
			c = v
			l = 1
		} else {
			// Tally up length of the repeats.
			l++
		}
	}

	var r int
	for i := 0; i < len(parts); i++ {
		if i + 1 < len(parts) && parts[i] < parts[i+1] {
			r -= parts[i]
		} else {
			r += parts[i]
		}
	}

	return r
}

func ToRomanNumeral(i int) (string, error)  {
	var s string
	sets := []struct{
		factor int
		ten string
		five string
		one string
	}{
		// Note: if I was less lazy, I could generate these at runtime
		// from some input like []rune{'M', 'D', 'C', 'L', 'X', 'V', 'I'
		{1000, " ", " ", "M"},
		{100, "M", "D", "C"},
		{10, "C", "L", "X"},
		{1, "X", "V", "I"},
	}

	if i < 1 || i > 3000 {
		return s, errors.New("value out of range")
	}
	for _, set := range sets {
		// For each digit, extract just that single number
		v := (i / set.factor) % 10
		// Just explicitly call out 9 and 4 (IX, IV)
		if v == 9 {
			s += set.one + set.ten
			continue
		} else if v == 4 {
			s += set.one + set.five
			continue
		}
		if v >= 5 {
			s += set.five
			v = v - 5
		}
		s += strings.Repeat(set.one, v)
	}

	// Since I'm too lazy to write my own unit tests:
	if FromRomanNumeral(s) != i {
		return "", errors.New("Reverse failed")
	}
	return s, nil
}
