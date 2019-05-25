// Package luhn checks if a number satisfies the Luhn requirements.
package luhn

import (
	"strconv"
	"strings"
)

// Valid Luhn number or not?
func Valid(s string) bool {
	s = strings.ReplaceAll(s, " ", "")
	if len(s) <= 1 {
		return false
	}
	c := make(chan bool, 2)
	go sumA(s, c)
	go sumB(s, c)
	a, b := <-c, <-c
	if a != b {
		panic("answers differ")
	}
	return a
}

func sumA(s string, ch chan<- bool) {
	var sum int
	if len(s)%2 == 1 {
		s = "0" + s
	}
	for i, c := range s {
		v, err := strconv.Atoi(string(c))
		if err != nil {
			ch <- false
		}
		if i%2 == 0 {
			v *= 2
			if v > 9 {
				v -= 9
			}
		}
		sum += v
	}
	ch <- sum%10 == 0
}

func sumB(s string, ch chan<- bool) {
	var sum int
	flip := len(s)%2 == 1
	for _, c := range s {
		v, err := strconv.Atoi(string(c))
		if err != nil {
			ch <- false
			return
		}
		flip = !flip
		if flip {
			v *= 2
			if v > 9 {
				v -= 9
			}
		}
		sum += v
	}
	ch <- sum%10 == 0
}
