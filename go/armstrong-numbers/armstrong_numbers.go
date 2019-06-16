// Package armstrong tests for Armstrong numbers.
package armstrong

// IsNumber checks if a number is an Armstrong number.
func IsNumber(i int) bool {
	var parts []int
	j := i
	for j != 0 {
		parts = append(parts, j%10)
		j /= 10
	}
	p := len(parts)
	var sum int
	for _, v := range parts {
		sum += iPow(v, p)
	}
	return sum == i
}

// https://groups.google.com/d/msg/golang-nuts/PnLnr4bc9Wo/m4MIhzFuSo8J
func iPow(a, b int) int {
	var result = 1

	for 0 != b {
		if 0 != (b & 1) {
			result *= a

		}
		b >>= 1
		a *= a
	}

	return result
}
