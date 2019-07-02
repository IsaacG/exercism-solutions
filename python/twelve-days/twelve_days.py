#!/bin/python

opening = 'On the %s day of Christmas my true love gave to me: '
item = [
  'zero',
  'and a Partridge in a Pear Tree',
  'two Turtle Doves',
  'three French Hens',
  'four Calling Birds',
  'five Gold Rings',
  'six Geese-a-Laying',
  'seven Swans-a-Swimming',
  'eight Maids-a-Milking',
  'nine Ladies Dancing',
  'ten Lords-a-Leaping',
  'eleven Pipers Piping',
  'twelve Drummers Drumming',
]
numbers = [
  'zeroth', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
  'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


def verse(i):
  out = opening % numbers[i]
  if i == 1:
    items = ['a Partridge in a Pear Tree']
  else:
    items = item[i:0:-1]
  out += ', '.join(items) + '.'
  return out

  
def recite(start, end):
    return [verse(i) for i in range(start, end + 1)]


# vim:ts=2:sw=2:expandtab
