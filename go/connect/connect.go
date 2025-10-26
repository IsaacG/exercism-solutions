package connect

// coord represents a hex coordinate.
type coord [2]int

// add adds two coordinates and/or a coordinate and offset/direction.
func (c coord) add(o coord) coord {
	return coord{c[0] + o[0], c[1] + o[1]}
}

// neighbors returns six neighboring coordinates.
func (c coord) neighbors() []coord {
	hexDirections := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, -1}, {-1, 1}}
	var n []coord
	for _, d := range hexDirections {
		n = append(n, c.add(d))
	}
	return n
}

type game struct {
	pieces map[rune]map[coord]bool
	max    [2]int
}

// newGame parses and contructs a new game, storing all the X and O pieces.
func newGame(lines []string) game {
	pieces := map[rune]map[coord]bool{'X': map[coord]bool{}, 'O': map[coord]bool{}}
	for y, line := range lines {
		for x, piece := range line {
			if piece == 'X' || piece == 'O' {
				pieces[piece][coord{x, y}] = true
			}
		}
	}
	return game{pieces, [2]int{len(lines[0]) - 1, len(lines) - 1}}
}

// connects determines if a player has a line from one side to the other.
func (g game) connects(player rune, axis int) bool {
	pieces := g.pieces[player]
	var todo []coord
	added := map[coord]bool{}
	// Start with all the coordinates along one side.
	for piece := range pieces {
		if piece[axis] == 0 {
			todo = append(todo, piece)
			added[piece] = true
		}
	}
	// Breadth first explore.
	for len(todo) > 0 {
		// Pop one piece.
		piece := todo[0]
		todo = todo[1:]
		// Return true if the pieces connect to the far side.
		if piece[axis] == g.max[axis] {
			return true
		}
		// Append all unseen neighboring pieces.
		for _, neighbor := range piece.neighbors() {
			if !added[neighbor] && pieces[neighbor] {
				todo = append(todo, neighbor)
				added[neighbor] = true
			}
		}
	}
	return false
}

// ResultOf returns the winner of a game.
func ResultOf(lines []string) (string, error) {
	g := newGame(lines)
	if g.connects('X', 0) {
		return "X", nil
	}
	if g.connects('O', 1) {
		return "O", nil
	}
	return "", nil

	panic("Please implement the ResultOf function")
}
