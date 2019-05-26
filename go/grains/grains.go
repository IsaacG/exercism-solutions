// Package grains computes grains on a board.
package grains

import (
	"errors"
	"math"
)

// Square computes the grains on a given square.
func Square(s int) (uint64, error) {
	if s < 1 || s > 64 {
		return 0, errors.New("invalid square")
	}
	return uint64(math.Pow(2, float64(s-1))), nil
}

// Total computes the total grains on a board.
func Total () uint64 {
	s, _ := Square(64)
	return 2 * s - 1
}
