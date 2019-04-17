// Package leap determines if a year is a leap year.
package leap

type test struct {
	Dividend int
	Result   bool
}

// IsLeapYear checks if a year is a leap year.
func IsLeapYear(y int) bool {
	tests := []test{
		{400, true},
		{100, false},
		{4, true},
		{1, false}, // This is a catch-all and will always match.
	}
	for _, t := range tests {
		if (y % t.Dividend) == 0 {
			return t.Result
		}
	}
	panic("you should never get here!")
}
