package sorting

import (
	"fmt"
	"strconv"
)

// DescribeNumber should return a string describing the number.
func DescribeNumber(f float64) string {
	return fmt.Sprintf("This is the number %0.1f", f)
}

// NumberBox is a box for a number.
type NumberBox interface {
	Number() int
}

// DescribeNumberBox should return a string describing the NumberBox.
func DescribeNumberBox(nb NumberBox) string {
	return fmt.Sprintf("This is a box containing the number %d.0", nb.Number())
}

// FancyNumber is a string encoded number.
type FancyNumber struct {
	n string
}

// Value returns the value inside a FancyNumber.
func (i FancyNumber) Value() string {
	return i.n
}

// FancyNumberBox is a fancy box for a number.
type FancyNumberBox interface {
	Value() string
}

// ExtractFancyNumber should return the integer value for a FancyNumber
// and 0 if any other FancyNumberBox is supplied.
func ExtractFancyNumber(fnb FancyNumberBox) int {
	if fn, ok := fnb.(FancyNumber); ok {
		num, _ := strconv.Atoi(fn.n)
		return num
	}
	return 0
}

// DescribeFancyNumberBox should return a string describing the FancyNumberBox.
func DescribeFancyNumberBox(fnb FancyNumberBox) string {
	return fmt.Sprintf("This is a fancy box containing the number %d.0", ExtractFancyNumber(fnb))
}

// DescribeAnything should return a string describing whatever it contains.
func DescribeAnything(i interface{}) string {
	switch i.(type) {
	case int:
		return DescribeNumber(float64(i.(int)))
	case float64:
		return DescribeNumber(i.(float64))
	case NumberBox:
		return DescribeNumberBox(i.(NumberBox))
	case FancyNumberBox:
		return DescribeFancyNumberBox(i.(FancyNumberBox))
	default:
		return "Return to sender"
	}
}
