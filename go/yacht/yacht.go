// Package yacht scores a roll in Yacht.
package yacht

// I could map the string directly to a function but I opted
// to make use of an interface that has a .score method.
// This keeps the map and code easier to read, though longer.
var scorer = map[string]turn{
	"ones":            singles{1},
	"twos":            singles{2},
	"threes":          singles{3},
	"fours":           singles{4},
	"fives":           singles{5},
	"sixes":           singles{6},
	"full house":      fullHouse{},
	"four of a kind":  fourOfAKind{},
	"little straight": straight{6},
	"big straight":    straight{1},
	"choice":          choice{},
	"yacht":           yacht{},
}

// turn encapsulates information needed to score a turn.
type turn interface {
	score(dice []int) int
}

type singles struct {
	num int
}
type fullHouse struct{}
type fourOfAKind struct{}
type straight struct {
	missing int
}
type choice struct{}
type yacht struct{}

func count(dice []int) map[int]int {
	m := make(map[int]int)
	for _, d := range dice {
		m[d]++
	}
	return m
}

func sum(dice []int) (s int) {
	for _, d := range dice {
		s += d
	}
	return s
}

func (t singles) score(dice []int) (score int) {
	for _, d := range dice {
		if d == t.num {
			score += t.num
		}
	}
	return score
}

func (t fullHouse) score(dice []int) int {
	m := count(dice)
	if len(m) == 2 && (m[dice[0]] == 2 || m[dice[0]] == 3) {
		return sum(dice)
	}
	return 0
}

func (t fourOfAKind) score(dice []int) int {
	m := count(dice)
	if m[dice[0]] >= 4 {
		return 4 * dice[0]
	}
	if m[dice[1]] >= 4 {
		return 4 * dice[1]
	}
	return 0
}

func (t straight) score(dice []int) int {
	m := count(dice)
	if len(m) == 5 && m[t.missing] == 0 {
		return 30
	}
	return 0
}

func (t choice) score(dice []int) int {
	return sum(dice)
}

func (t yacht) score(dice []int) int {
	if len(count(dice)) != 1 {
		return 0
	}
	return 50
}

// Score scores a hand of dice and a category.
func Score(dice []int, category string) int {
	return scorer[category].score(dice)
}
