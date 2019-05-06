// Package diffsquares solves diffsquares.
package diffsquares

// SumOfSquares sums up a sequence of squares.
func SumOfSquares(n int) int {
	var sum int
	for i := 1; i <= n; i++ {
		sum += i * i
	}
	return sum
}

// SquareOfSum is the square of the sum of a sequence.
func SquareOfSum(n int) int {
	var sum int
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum * sum
}

// Difference between SquareOfSum and SumOfSquares.
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
