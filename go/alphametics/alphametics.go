package alphametics

import (
	"errors"
	"strings"
)

type Puzzle struct {
	lhs     map[rune]int
	rhs     map[rune]int
	chars   []rune
	nonZero map[rune]bool
	maxVal  int
}


type values struct {
	m       map[rune]int
	chars   []rune
	nonZero map[rune]bool
}

func charWeight(words []string) map[rune]int {
	w := map[rune]int{}
	for _, word := range words {
		runes := []rune(word)
		base := 1
		for i := len(runes) - 1; i >= 0; i-- {
			w[runes[i]] += base
			base *= 10
		}
	}
	return w
}

func newValues(chars []rune, nonZero map[rune]bool) *values {
	l := len(chars)
	v := make(map[rune]int, len(chars))
	for i, c := range chars {
		v[c] = l - i
	}
	return &values{v, chars, nonZero}
}

func (v *values) stringMap() map[string]int {
	sm := make(map[string]int, len(v.m))
	for r, i := range v.m {
		sm[string(r)] = i
	}
	return sm
}

func (v *values) increment() {
	for _, c := range v.chars {
		v.m[c]++
		if v.m[c] != 10 {
			break
		}
		if v.nonZero[c] {
			v.m[c] = 1
		} else {
			v.m[c] = 0
		}
	}
}

func (p Puzzle) valid(v *values) bool {
	// Check the equallity.
	lhs := 0
	for r, w := range p.lhs {
		lhs += v.m[r] * w
	}
	rhs := 0
	for r, w := range p.rhs {
		rhs += v.m[r] * w
	}
	if lhs != rhs {
		return false
	}
	// Disqualify repeating numbers.
	vals := make(map[int]struct{}, len(v.m))
	for _, val := range v.m {
		vals[val] = struct{}{}
	}
	if len(vals) != len(v.m) {
		return false
	}
	return true
}

func newPuzzle(input string) (*Puzzle, error) {
	// Split into LHS and RHS words.
	parts := strings.Split(input, "==")
	if len(parts) != 2 {
		return nil, errors.New("puzzle must have exactly one '=='")
	}
	words := make([]string, 0)
	for _, word := range strings.Split(parts[0], "+") {
		words = append(words, strings.Trim(word, " "))
	}
	words = append(words, strings.Trim(parts[1], " "))

	// Compute chars and nonZero chars.
	nonZero := make(map[rune]bool, len(words))
	charMap := make(map[rune]struct{}, len(input))
	for _, word := range words {
		nonZero[rune(word[0])] = true
		for _, c := range word {
			charMap[c] = struct{}{}
		}
	}

	chars := make([]rune, 0, len(charMap))
	maxVal := 1
	for c := range charMap {
		chars = append(chars, c)
		maxVal *= 10
	}

	return &Puzzle{
		lhs:     charWeight(words[:len(words)-1]),
		rhs:     charWeight(words[len(words)-1:]),
		chars:   chars,
		nonZero: nonZero,
		maxVal:  maxVal,
	}, nil
}

func (p Puzzle) solve() (map[string]int, error) {
	v := newValues(p.chars, p.nonZero)
	for i := 0; i < p.maxVal; i++ {
		if p.valid(v) {
			return v.stringMap(), nil
		}
		v.increment()
	}
	return nil, errors.New("no solution found")
}

func Solve(puzzle string) (map[string]int, error) {
	p, err := newPuzzle(puzzle)
	if err != nil {
		return nil, err
	}
	return p.solve()

}
