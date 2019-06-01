#!/usr/bin/env bash

days=(first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth)
items=("a Partridge in a Pear Tree" "two Turtle Doves" "three French Hens" "four Calling Birds"
    "five Gold Rings" "six Geese-a-Laying" "seven Swans-a-Swimming" "eight Maids-a-Milking"
    "nine Ladies Dancing" "ten Lords-a-Leaping" "eleven Pipers Piping" "twelve Drummers Drumming")

line () {
  list=''
  for (( j = $1; j >= 0; j -- )); do
    list+="${items[j]}";
    (( j > 0 )) && list+=', '
    (( j == 1 )) && list+='and '
  done
  printf 'On the %s day of Christmas my true love gave to me: %s.\n' "${days[$1]}" "$list"
}

sing () {
  for (( i = $1; i <= $2; i++ )); do line "$((i-1))"; done
}
sing "$@"

# vim:ts=2:sw=2:expandtab
