// Package scrabble solves the scrabble exercise.
package scrabble

import "strings"

var value = map[rune]int{
	'A': 1,
	'E': 1,
	'I': 1,
	'O': 1,
	'U': 1,
	'L': 1,
	'N': 1,
	'R': 1,
	'S': 1,
	'T': 1,
	'D': 2,
	'G': 2,
	'B': 3,
	'C': 3,
	'M': 3,
	'P': 3,
	'F': 4,
	'H': 4,
	'V': 4,
	'W': 4,
	'Y': 4,
	'K': 5,
	'J': 8,
	'X': 8,
	'Q': 10,
	'Z': 10,
}

// Score a Scrabble word.
func ScoreMap(w string) int {
	score := 0
	for _, r := range strings.ToUpper(w) {
		score += value[r]
	}
	return score
}

var pointsTable = [26]int{
//  A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q,  R, S, T, U, V, W, X, Y, Z
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10}

var bigTable = []int{
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 2,
  1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 0, 1, 1, 1, 4, 4, 8, 4, 10,
  0, 0, 0, 0, 0, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1,
  1, 1, 1, 4, 4, 8, 4, 10}

// Score returns the score of a given word in scrabble.
func Score(word string) int {
    var score int
    for i := 0; i < len(word); i++ {
    	score += bigTable[word[i]]
    }
    return score
}

// Score returns the score of a given word in scrabble.
func ScoreSmall(word string) int {
    var score int
    for i := 0; i < len(word); i++ {
        if word[i] > 'Z' {
            score += pointsTable[word[i]-'a']
        } else {
            score += pointsTable[word[i]-'A']
        }
    }
    return score
}

