package rectangles

type point struct{ x, y int }
type board struct {
	corners, horz, vert map[point]bool
}

func newBoard(diagram []string) board {
	corners := map[point]bool{}
	horz := map[point]bool{}
	vert := map[point]bool{}

	for y, line := range diagram {
		for x, char := range line {
			if char == ' ' {
				continue
			}
			p := point{x, y}
			switch char {
			case '+':
				corners[p] = true
				horz[p] = true
				vert[p] = true
			case '|':
				vert[p] = true
			case '-':
				horz[p] = true
			default:
				panic("Invalid char " + string(char))
			}
		}
	}
	return board{corners, horz, vert}
}

func (b board) isRect(topLeft, bottomRight point) bool {
	// topLeft must be above and left of bottomRight.
	if topLeft.x >= bottomRight.x || topLeft.y >= bottomRight.y {
		return false
	}
	// Check the other two corners exist.
	topRight := point{bottomRight.x, topLeft.y}
	bottomLeft := point{topLeft.x, bottomRight.y}
	if !b.corners[topRight] || !b.corners[bottomLeft] {
		return false
	}

	// Check the top and bottom edges exist.
	for x := topLeft.x; x <= topRight.x; x++ {
		if !b.horz[point{x, topLeft.y}] || !b.horz[point{x, bottomLeft.y}] {
			return false
		}
	}

	// Check the right and left edges exist.
	for y := topLeft.y; y <= bottomLeft.y; y++ {
		if !b.vert[point{topLeft.x, y}] || !b.vert[point{topRight.x, y}] {
			return false
		}
	}
	return true
}

// Count returns the number of rectangles in a diagram.
func Count(diagram []string) int {
	board := newBoard(diagram)

	count := 0
	// Iterate through all potential rectangle corners.
	for topLeft := range board.corners {
		for bottomRight := range board.corners {
			if board.isRect(topLeft, bottomRight) {
				count++
			}
		}
	}
	return count

	panic("Please implement the Count function")
}
