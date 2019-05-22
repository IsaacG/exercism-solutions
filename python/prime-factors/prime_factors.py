#!/bin/python

def prime_factors(num):
  factors = []
  divisor = 2
  
  while num > 1:
    # Repeat divide and append.
    if num % divisor == 0:
      num /= divisor
      factors.append(divisor)
    else:
      divisor += 1

  return factors

# vim:ts=2:sw=2:expandtab
