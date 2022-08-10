// Package thefarm does some cow fodder calculations.
package thefarm

import (
	"errors"
	"fmt"
)

// SillyNephewError is returned when cows are negative.
type SillyNephewError struct {
	cows int
}

// Error returns the error message.
func (e *SillyNephewError) Error() string {
	return fmt.Sprintf("silly nephew, there cannot be %d cows", e.cows)
}

// DivideFood computes the fodder amount per cow for the given cows.
func DivideFood(weightFodder WeightFodder, cows int) (float64, error) {
	total, err := weightFodder.FodderAmount()
	if err == ErrScaleMalfunction {
		total *= 2
	}
	switch {
	case err != nil && err != ErrScaleMalfunction:
		return 0, err
	case total < 0:
		return 0, errors.New("negative fodder")
	case cows == 0:
		return 0, errors.New("division by zero")
	case cows < 0:
		return 0, &SillyNephewError{cows}
	default:
		return total / float64(cows), nil
	}
}
