// Package collatzconjecture solves collatzconjecture.
package collatzconjecture

import "errors"

func CollatzConjecture(i int) (int, error) {
	if i < 1 {
		return 0, errors.New("Bad input")
	}
	count := 0
	for i != 1 {
		if (i % 2 == 0) {
			i = i / 2
		} else {
			i = i * 3 + 1
		}
		count++
	}
	return count, nil
}
