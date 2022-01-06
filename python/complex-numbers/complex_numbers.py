import math
import numbers

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, numbers.Real):
            return self == ComplexNumber(other, 0)

        return (
            type(self) == type(other)
            and self.real == other.real
            and self.imaginary == other.imaginary)

    def __add__(self, other):
        if isinstance(other, numbers.Real):
            return self + ComplexNumber(other, 0)

        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return self * ComplexNumber(other, 0)

        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(r, i)

    def __sub__(self, other):
        if isinstance(other, numbers.Real):
            return self - ComplexNumber(other, 0)

        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            return self / ComplexNumber(other, 0)

        div = (other.real**2 + other.imaginary**2) 
        r = (self.real * other.real + self.imaginary * other.imaginary) / div
        i = (self.imaginary * other.real - self.real * other.imaginary) / div
        return ComplexNumber(r, i)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        e_i = ComplexNumber(math.cos(self.imaginary), math.sin(self.imaginary))
        return e_i * math.exp(self.real)

    def __repr__(self):
        return '%d + %d * i' % (self.real, self.imaginary)
