// Package pythagorean is.
package pythagorean

import "math"

type Triplet [3]int

// Range returns a list of all Pythagorean triplets with sides in the
// range min to max inclusive.
func Range(min, max int) []Triplet {
	var ret []Triplet

	for a := min; a <= max; a++ {
		for b := a; b <= max; b++ {
			c := int(math.Sqrt(float64(a*a + b*b)))
			if c >= min && c <= max && isPythag(a, b, c) {
				ret = append(ret, Triplet{a, b, c})
			}
		}
	}

	return ret
}

func isPythag(a, b, c int) bool {
	return a*a + b*b == c*c
}

// Sum returns a list of all Pythagorean triplets where the sum a+b+c
// (the perimeter) is equal to p.
func Sum(p int) []Triplet {
	var ret []Triplet

	for b := p; b >= p / 3; b-- {
		for a := 1; a <= b; a++ {
			c := p - a - b
			if isPythag(a, b, c) {
				ret = append(ret, Triplet{a, b, c})
			}
		}
	}

	return ret
}
