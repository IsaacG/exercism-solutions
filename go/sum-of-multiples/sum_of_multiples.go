// Package summultiples sums multiples.
package summultiples

func isDiv(n int, d []int) bool {
	for _, i := range d {
		if i == 0 {
			continue
		}
		if n%i == 0 {
			return true
		}
	}
	return false
}

// SumMultiples sums up multiples of the divisors.
func SumMultiples(lim int, div ...int) int {
	var sum int
	for i := 1; i < lim; i++ {
		if isDiv(i, div) {
			sum += i
		}
	}
	return sum
}
