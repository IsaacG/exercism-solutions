package change

import (
	"errors"
	"slices"
)

// min returns the shorter of two slices.
func min(a, b []int) []int {
	if len(a) < len(b) {
		return a
	}
	return b
}

// Solver uses dynamic programming to solve the change problem.
type Solver struct {
	coins []int
	cache map[int][]int
}

// NewSolver returns a new Solver.
func NewSolver(coins []int) *Solver {
	cache := make(map[int][]int)
	// Initialize the cache with the base cases for each coin.
	for _, coin := range coins {
		cache[coin] = []int{coin}
	}
	// Clone and reverse sort the coins so we can solve from large to small.
	coins = slices.Clone(coins)
	slices.Sort(coins)
	slices.Reverse(coins)
	return &Solver{coins, cache}
}

// Fewest returns the fewest coins needed.
func (s *Solver) Fewest(target int) ([]int, error) {
	got, err := s.run(s.coins, target)
	slices.Sort(got)
	return got, err
}

func (s *Solver) run(coins []int, target int) ([]int, error) {
	// If the target is 0, we can make change with no coins.
	if target == 0 {
		return []int{}, nil
	}
	// If we have no coins left to consider, error.
	if len(coins) == 0 {
		return nil, errors.New("invalid")
	}
	// If the largest coin is larger than the target, drop it.
	if coins[0] > target {
		return s.run(coins[1:], target)
	}
	// Attempt using a cached entry.
	if got, ok := s.cache[target]; ok {
		return got, nil
	}

	// Option A: we use the largest coin.
	// Solve using target - largest coin and add the coin to the results.
	fewestA, errA := s.run(coins, target-coins[0])
	if errA == nil {
		fewestA = append(slices.Clone(fewestA), coins[0])
	}

	// Option B: we do not use the largest coin. Solve with the largest coin dropped.
	fewestB, errB := s.run(coins[1:], target)

	if errA != nil && errB != nil {
		return nil, errA
	}

	// Select the best option and cache the result.
	var fewest []int
	if errA != nil {
		fewest = fewestB
	} else if errB != nil {
		fewest = fewestA
	} else {
		fewest = min(fewestA, fewestB)
	}
	s.cache[target] = fewest
	return fewest, nil
}

// Change solves for the fewest coins.
func Change(coins []int, target int) ([]int, error) {
	return NewSolver(coins).Fewest(target)
}
