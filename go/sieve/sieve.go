// Package sieve solves for primes using the Sieve of Eratosthenes.
package sieve

// Sieve applies the Sieve of Eratosthenes to compute primes.
func Sieve(lim int) []int {
	isPrime := make([]bool, lim + 1)
	// Note this wastes the first two elements.
	// Mark all values (2+) as prime initially.
	for i:= 2; i <= lim; i++ {
		isPrime[i] = true
	}
	for i:= 2; i <= lim; i++ {
		if ! isPrime[i] {
			continue
		}
		for j := i * 2; j <= lim; j += i {
			isPrime[j] = false
		}
	}

	var results []int
	for i:= 2; i <= lim; i++ {
		if isPrime[i] {
			results = append(results, i)
		}
	}
	return results
}
