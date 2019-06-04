// Package perfect checks perfect numbers.
package perfect

import "errors"

// Classification indicates the number type.
type Classification int

const (
	// NoClassification when no classification was done.
	NoClassification = 0
	// ClassificationAbundant for abundant numbers.
	ClassificationAbundant = 1
	// ClassificationDeficient for deficient numbers.
	ClassificationDeficient = 2
	// ClassificationPerfect for perfect numbers.
	ClassificationPerfect = 3
)

// ErrOnlyPositive when the number is not positive.
var ErrOnlyPositive = errors.New("only positive values allowed")

func aliquotSum(n int64) (sum int64) {
	for i := int64(1); i < n; i++ {
		if n%i == 0 {
			sum += i
		}
	}
	return
}

// Classify classifies a number as abundant, perfect or deficient.
func Classify(n int64) (Classification, error) {
	if n <= 0 {
		return NoClassification, ErrOnlyPositive
	}
	a := aliquotSum(n)
	if a < n {
		return ClassificationDeficient, nil
	}
	if a > n {
		return ClassificationAbundant, nil
	}
	return ClassificationPerfect, nil
}
