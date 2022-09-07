// Package alphametics solves alphametics puzzles.
package alphametics

import (
	"errors"
	"strings"
)

// charWeight returns a weight of each rune, used to evaluate equations.
// "ABA + BC" has weights {'A': 101, 'B': 20, 'C': 1}.
// By multiplying weights be char value, euqations can be evaluated quickly.
// For example, given values {'A': 2, 'B': 3, 'C': 4}, the above equation
// has a value of 2 * 101 + 3 * 20 + 4 * 1.
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

// solver solves puzzles.
type solver struct {
	// Weight of runes for equation LHS - RHS = 0
	charWeights map[rune]int
	// List of runes to solve.
	chars []rune
	// Map indicating which runes cannot be zero.
	nonZero map[rune]bool
}

// newSolver builds and returns a new solver.
func newSolver(input string) (*solver, error) {
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
	for c := range charMap {
		chars = append(chars, c)
	}

	weights := map[rune]int{}
	// LHS weights are positive.
	for c, w := range charWeight(words[:len(words)-1]) {
		weights[c] += w
	}
	// RHS weights are negative..
	for c, w := range charWeight(words[len(words)-1:]) {
		weights[c] -= w
	}
	return &solver{
		chars:       chars,
		nonZero:     nonZero,
		charWeights: weights,
	}, nil
}

// recursiveSolve solves a puzzle recursively, one char at a time.
// An equation is valid when LHS == RHS. Alternatively, LHS - RHS == 0.
// Equations can be solved recursively by replacing one char at a time and tracking
// the computed "balance" of LHS - RHS. When all characters are evaluated, LHS - RHS = 0
// must be true.
func (p solver) recursiveSolve(balance int, chars []rune, used map[int]bool) (map[string]int, bool) {
	// Split the chars into the current char to replace and the rest to be recursively handled.
	c, rest := chars[0], chars[1:]
	weight := p.charWeights[c]
	// Try using values [0..9] or [1..9] as a value for c.
	start := 0
	if p.nonZero[c] {
		start = 1
	}
	for i := start; i < 10; i++ {
		if used[i] {
			continue
		}

		used[i] = true
		// If there are no remaining chars, check if the equation balances.
		if len(rest) == 0 {
			// If the equation balances, we found a solution.
			if balance+weight*i == 0 {
				return map[string]int{string(c): i}, true
			}
		} else {
			// Check if we can find a solution with this value for c.
			vals, ok := p.recursiveSolve(balance+weight*i, rest, used)
			if ok {
				vals[string(c)] = i
				return vals, true
			}
		}
		used[i] = false
	}
	return nil, false
}

// Solve solves an alphametics puzzle.
func Solve(puzzle string) (map[string]int, error) {
	p, err := newSolver(puzzle)
	if err != nil {
		return nil, err
	}
	solution, ok := p.recursiveSolve(0, p.chars, map[int]bool{})
	if !ok {
		return nil, errors.New("no solution found")
	}
	return solution, nil
}
