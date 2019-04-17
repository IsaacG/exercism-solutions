// Package triangle tells you what type of triangle you got.
package triangle

import "math"

// Kind of triangles
type Kind int

const (
	// NaT not a triangle
	NaT = iota
	// Equ equilateral
	Equ
	// Iso isosceles
	Iso
	// Sca scalene
	Sca
)

// KindFromSides gives the triangle kind
func KindFromSides(a, b, c float64) Kind {
	if math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0) {
		return NaT
	}
	if math.IsNaN(a) || math.IsNaN(b) || math.IsNaN(c) {
		return NaT
	}
	if a <= 0 || b <= 0 || c <= 0 {
		return NaT
	}

	if (a+b) < c || (a+c) < b || (b+c) < a {
		return NaT
	}

	if a == b && a == c {
		return Equ
	}
	if a == b || a == c || b == c {
		return Iso
	}
	return Sca
}
