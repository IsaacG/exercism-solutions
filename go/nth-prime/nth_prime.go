// Package prime
package prime

var primes = []int{2}

func isPrime(i int) bool {
	for _, n := range primes {
		if i % n == 0 {
			return false
		}
	}
	return true
}

func Nth(n int) (int, bool) {
	if n < 1 {
		return 0, false
	}

	for i := 3; len(primes) < n; i += 2 {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes[n - 1], true
}
