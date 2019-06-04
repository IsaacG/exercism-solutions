// Package grains computes grains on a board.
package grains

import (
	"errors"
)

// Square computes the grains on a given square.
func Square(s int) (uint64, error) {
	if s < 1 || s > 64 {
		return 0, errors.New("invalid square")
	}
	return 1 << uint(s-1), nil
}

// Total computes the total grains on a board.
func Total() uint64 {
	return 1<<64 - 1
}
