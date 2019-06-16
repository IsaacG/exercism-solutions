// Package prime computes prime factors.
package prime

// Factors computes prime factors.
func Factors(n int64) []int64 {
	factors := make([]int64, 0)
	for i := int64(2); n > 1; {
		if n % i == 0 {
			factors = append(factors, i)
			n /= i
		} else {
			i++
		}
	}
	return factors
}
