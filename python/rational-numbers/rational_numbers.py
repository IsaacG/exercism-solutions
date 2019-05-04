from __future__ import division

import math


def gcd(a, b):
  """Greatest Common Denominator, Euclid's algorithm."""
  if b == 0:
    return a
  return gcd(b, a % b)


class Rational(object):
  def __init__(self, numer, denom):
    div = gcd(numer, denom)
    self.numer = numer / div
    self.denom = denom / div

  def __eq__(self, other):
    return self.numer == other.numer and self.denom == other.denom

  def __repr__(self):
    return '{}/{}'.format(self.numer, self.denom)

  def __add__(self, other):
    # (a1 * b2 + a2 * b1) / (b1 * b2).
    numer = self.numer * other.denom + other.numer * self.denom
    denom = self.denom * other.denom
    return Rational(numer, denom)

  def __sub__(self, other):
    numer = self.numer * other.denom - other.numer * self.denom
    denom = self.denom * other.denom
    return Rational(numer, denom)

  def __mul__(self, other):
    return Rational(self.numer * other.numer, self.denom * other.denom)

  def __truediv__(self, other):
    return Rational(self.numer * other.denom, other.numer * self.denom)

  def __abs__(self):
    return Rational(abs(self.numer), abs(self.denom))

  def __pow__(self, power):
    if power >= 0:
      return Rational(self.numer ** power, self.denom ** power)
    else:
      power = abs(power)
      return Rational(self.denom ** power, self.numer ** power)

  def __rpow__(self, base):
    # n'th root of x = root(x, n) = power(x, 1/n)
    return math.pow(base**self.numer, 1/self.denom)


# vim:ts=2:sw=2:expandtab
