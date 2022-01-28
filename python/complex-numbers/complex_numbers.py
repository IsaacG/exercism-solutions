"""Implement complex numbers."""

import math
import numbers

class ComplexNumber:
    """Complex Number."""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, numbers.Real):
            return self == ComplexNumber(other, 0)

        return (
            isinstance(other, ComplexNumber)
            and self.real == other.real
            and self.imaginary == other.imaginary)

    def __add__(self, other):
        if isinstance(other, numbers.Real):
            return self + ComplexNumber(other, 0)

        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return self * ComplexNumber(other, 0)

        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary
        )

    def __sub__(self, other):
        if isinstance(other, numbers.Real):
            return self - ComplexNumber(other, 0)

        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return other + -1 * self

    def __rtruediv__(self, other):
        div = (self.real**2 + self.imaginary**2)
        return other * ComplexNumber(self.real / div, - self.imaginary / div)

    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            return self / ComplexNumber(other, 0)

        div = (other.real**2 + other.imaginary**2)
        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / div,
            (self.imaginary * other.real - self.real * other.imaginary) / div,
        )

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        """Return the conjugate."""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """Return the exponent."""
        e_i = ComplexNumber(math.cos(self.imaginary), math.sin(self.imaginary))
        return e_i * math.exp(self.real)

    def __repr__(self):
        return f"{self.real} + {self.imaginary} * i"


# vim:ts=2:sw=2:expandtab
