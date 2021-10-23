// Package lasagna does baking time.
package lasagna

// OvenTime is total time in the oven.
const OvenTime = 40

// RemainingOvenTime returns time left in the oven.
func RemainingOvenTime(elapsed int) int {
	return OvenTime - elapsed
}

// PreparationTime returns time needed to prep.
func PreparationTime(layers int) int {
	return layers * 2
}

// ElapsedTime returns time already elapsed.
func ElapsedTime(layers, elapsed int) int {
	return PreparationTime(layers) + elapsed
}
