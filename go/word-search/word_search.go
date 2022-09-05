// Package wordsearch performs a puzzle word search.
package wordsearch

import (
	"errors"
	"sort"
)

// point is a coordinate point in a puzzle, or a direction.
type point struct {
	i, j int
}
type direction point

// board stores information about a puzzle.
type board struct {
	puzzle        []string
	width, height int
}

// solver handles solving a puzzle.
type solver struct {
	b            *board
	toFind       map[string]struct{}
	toFindCounts map[int]int
	wantLengths  []int
	found        map[string][2][2]int
}

// copy returns a copy of a point.
func (p *point) copy() point {
	return point{p.i, p.j}
}

// negate negates a point (reverses a direction).
func (d *direction) negate() direction {
	return direction{-d.i, -d.j}
}

// add increments a point by a direction.
func (p *point) add(dir direction) {
	p.i += dir.i
	p.j += dir.j
}

// directions is all the directions we need to search in from any given start point.
var directions = []direction{{0, 1}, {1, 0}, {1, 1}, {1, -1}}

// points returns all the starting points to search in a puzzle.
func (b board) points() []point {
	p := make([]point, 0, b.width*b.height)
	for i := 0; i < b.width; i++ {
		for j := 0; j < b.height; j++ {
			p = append(p, point{i, j})
		}
	}
	return p
}

// char returns a character from a puzzle as a given point.
func (b board) char(p point) byte {
	return b.puzzle[p.j][p.i]
}

// valid returns if a point is on the board.
func (b board) valid(p point) bool {
	return 0 <= p.i && p.i < b.width && 0 <= p.j && p.j < b.height
}

// foundAll returns if all the words have been found.
func (s solver) foundAll() bool {
	return len(s.toFind) == 0
}

// recordFinding records coordinates of found words if the word is in the word list.
func (s solver) recordFinding(wordLen int, start point, dir direction) {
	w := make([]byte, wordLen)
	cur := start.copy()
	for k := 0; k < wordLen; k++ {
		w[k] = s.b.char(cur)
		cur.add(dir)
	}
	word := string(w)
	if _, ok := s.toFind[word]; !ok {
		return
	}
	s.found[word] = [2][2]int{{start.i, start.j}, {cur.i - dir.i, cur.j - dir.j}}
	delete(s.toFind, word)
	s.toFindCounts[len(word)]--
	if len(word) == s.wantLengths[0] && s.toFindCounts[len(word)] == 0 {
		s.wantLengths = s.wantLengths[1:]
	}
}

// recordWordsAt records all potential words with a given start point.
func (s solver) recordWordsAt(start point) {
	// Try creating words from start in direction.
	for _, dir := range directions {
		end := start.copy()
		for wl := 1; wl <= s.wantLengths[0]; wl++ {
			// Stop when we get off the edge of the board.
			if !s.b.valid(end) {
				break
			}
			if s.toFindCounts[wl] != 0 {
				s.recordFinding(wl, start, dir)
				s.recordFinding(wl, end, dir.negate())
			}
			end.add(dir)
		}
	}
}

// solve tries to solve a puzzle, returning whether all words were found.
func (s *solver) solve() bool {
	for _, start := range s.b.points() {
		s.recordWordsAt(start)
		if s.foundAll() {
			return true
		}
	}
	return false
}

// newSolver constructs and returns a new solver.
func newSolver(words []string, puzzle []string) *solver {
	notFound := make(map[string]struct{})
	notFoundCount := make(map[int]int)
	for _, word := range words {
		notFound[word] = struct{}{}
		notFoundCount[len(word)]++
	}

	lengths := []int{}
	for l := range notFoundCount {
		lengths = append(lengths, l)
	}
	sort.Ints(lengths)
	for i := 0; i < len(lengths)/2; i++ {
		lengths[i], lengths[len(lengths)-1-i] = lengths[len(lengths)-1-i], lengths[i]
	}
	b := &board{puzzle: puzzle, width: len(puzzle[0]), height: len(puzzle)}
	return &solver{b: b, toFind: notFound, toFindCounts: notFoundCount, wantLengths: lengths, found: make(map[string][2][2]int)}
}

// Solve returns the start and end coordinates of words in a puzzle.
func Solve(words []string, puzzle []string) (map[string][2][2]int, error) {
	s := newSolver(words, puzzle)
	if !s.solve() {
		return nil, errors.New("could not find some words")
	}
	return s.found, nil
}
