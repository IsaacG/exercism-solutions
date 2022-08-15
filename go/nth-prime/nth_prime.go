// Package prime
package prime

import "errors"

var primes = []int{2}

func isPrime(i int) bool {
	for _, n := range primes {
		if i % n == 0 {
			return false
		}
	}
	return true
}

func Nth(n int) (int, error) {
	if n < 1 {
		return 0, errors.New("n must be 1 or larger")
	}

	for i := 3; len(primes) < n; i += 2 {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes[n - 1], nil
}
