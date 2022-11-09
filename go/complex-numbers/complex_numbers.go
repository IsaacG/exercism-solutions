// Package complex provides complex number support.
package complex

import "math"

// Number is a complex number.
type Number struct {
	real float64
	imag float64
}

// Real gives the real part of a complex number.
func (n Number) Real() float64 {
	return n.real
}

// Imaginary gives the imaginary part of a complex number.
func (n Number) Imaginary() float64 {
	return n.imag
}

// Add returns the sum of two complex numbers.
func (n Number) Add(other Number) Number {
	return Number{n.real + other.real, n.imag + other.imag}
}

// Subtract returns the difference of two complex numbers.
func (n Number) Subtract(other Number) Number {
	return Number{n.real - other.real, n.imag - other.imag}
}

// Multiply returns the product of two complex numbers.
func (n Number) Multiply(other Number) Number {
	return Number{
		n.real*other.real - n.imag*other.imag,
		n.imag*other.real + n.real*other.imag,
	}
}

// Times returns the product of a complex and real number.
func (n Number) Times(factor float64) Number {
	return Number{factor * n.real, factor * n.imag}
}

// Div returns the quotient of a complex and real number.
func (n Number) Div(factor float64) Number {
	return n.Times(1 / factor)
}

func (n Number) absSqr() float64 {
	return n.real*n.real + n.imag*n.imag
}

// Divide returns the quotient of two complex numbers.
func (n Number) Divide(other Number) Number {
	return n.Multiply(other.Conjugate()).Div(other.absSqr())
}

// Conjugate returns the conjugate of a complex number.
func (n Number) Conjugate() Number {
	return Number{n.real, -n.imag}
}

// Abs returns the absolute value of a complex number.
func (n Number) Abs() float64 {
	return math.Sqrt(n.absSqr())
}

// Exp returns e ** n for a complex number n.
func (n Number) Exp() Number {
	return Number{math.Cos(n.imag), math.Sin(n.imag)}.Times(math.Exp(n.real))
}
