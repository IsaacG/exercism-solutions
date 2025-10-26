package knapsack

// Item represents one item which can be carried.
type Item struct {
	Weight, Value int
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Knapsack takes in a maximum carrying capacity and a collection of items
// and returns the maximum value that can be carried by the knapsack
// given that the knapsack can only carry a maximum weight given by maximumWeight
func Knapsack(maximumWeight int, items []Item) int {
	if len(items) == 0 {
		return 0
	}
	one := items[0]
	rest := items[1:]
	if one.Weight > maximumWeight {
		return Knapsack(maximumWeight, rest)
	}
	return max(
		one.Value+Knapsack(maximumWeight-one.Weight, rest),
		Knapsack(maximumWeight, rest),
	)
}
