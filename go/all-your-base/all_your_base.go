// Package allyourbase does base conversion.
package allyourbase

import "errors"

// ConvertToBase converts between bases
func ConvertToBase(ibase int, digits []int, obase int) ([]int, error) {
	if ibase < 2 {
		return nil, errors.New("input base must be >= 2")
	}
	if obase < 2 {
		return nil, errors.New("output base must be >= 2")
	}
	val := 0
	for i, v := range rev(digits) {
		if v < 0 || v >= ibase {
			return nil, errors.New("all digits must satisfy 0 <= d < input base")
		}
		val += v * pow(ibase, i)
	}

	if val == 0 {
		return []int{0}, nil
	}
	var out []int
	for i := 0; val > 0; i++ {
		d := (val / pow(obase, i)) % obase
		out = append(out, d)
		val -= d * pow(obase, i)
	}
	return rev(out), nil
}

func pow(a, b int) int {
	p := 1
	for b > 0 {
		if b&1 != 0 {
			p *= a
		}
		b >>= 1
		a *= a
	}
	return p
}

func rev(a []int) []int {
	b := make([]int, len(a))
	for i := 0; i < len(a); i++ {
		b[len(a)-1-i] = a[i]
	}
	return b
}
