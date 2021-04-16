package darts

import "math"

type scoreLine struct {
	threshold float64
	points    int
}

var scores = []scoreLine{
	{10, 0},
	{5, 1},
	{1, 5},
	{-1, 10},
}

func Score(x, y float64) int {
	distance := math.Sqrt(math.Pow(x, 2) + math.Pow(y, 2))
	for _, line := range scores {
		if distance > line.threshold {
			return line.points
		}
	}
	panic("How did you get here?")
}
