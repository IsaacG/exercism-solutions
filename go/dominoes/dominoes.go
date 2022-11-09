// Package dominoes builds a chain of dominoes.
package dominoes

// Domino is a single tile with two int values.
type Domino [2]int

// Puzzle stores state for solving a chain of dominoes.
type Puzzle struct {
	// Count of available tiles.
	available map[int]map[int]int
	// Current solution chain.
	chain []int
	// Store if the puzzle was solved.
	solved bool
	// len(input).
	length int
}

// NewPuzzle returns a new Puzzle for a given input.
func NewPuzzle(input []Domino) *Puzzle {
	l := len(input)
	// A chain of N dominoes can be represented as N+1 values.
	chain := make([]int, l+1)
	// Given that we need to use all tiles and create a closed loop,
	// we can start with any tile in any orientation and the rest must fit.
	if l > 0 {
		chain[0] = input[0][0]
		chain[1] = input[0][1]
	}
	puzzle := &Puzzle{
		available: make(map[int]map[int]int),
		chain:     chain,
		solved:    false,
		length:    l,
	}
	// Add all the tiles to the available tile map.
	for i := 1; i < l; i++ {
		puzzle.addTile(input[i][0], input[i][1])
	}
	return puzzle
}

// Solve a domino chain.
func (p *Puzzle) Solve() ([]Domino, bool) {
	// Special case: 0 tiles is considered a valid chain.
	if p.length == 0 {
		return []Domino{}, true
	}
	if p.length == 1 {
		p.solved = p.chain[0] == p.chain[1]
	} else {
		p.extend(1)
	}
	// Construct the return chain based on the state.
	var solution []Domino
	if p.solved {
		solution = make([]Domino, p.length)
		for i := 0; i < p.length; i++ {
			solution[i] = Domino{p.chain[i], p.chain[i+1]}
		}
	}
	return solution, p.solved
}

// extend recursively extends the chain until a solution is found.
func (p *Puzzle) extend(depth int) {
	dNext := depth + 1
	// Prior value in the chain.
	prior := p.chain[depth]
	// Is this the last tile in the chain?
	last := dNext == p.length
	for _, o := range p.options(prior) {
		p.chain[dNext] = o
		if last {
			if o == p.chain[0] {
				p.solved = true
				return
			}
		} else {
			p.remTile(prior, o)
			p.extend(dNext)
			if p.solved {
				return
			}
			p.addTile(prior, o)
		}
	}
}

func (p *Puzzle) addTile(a, b int) {
	if _, ok := p.available[a]; !ok {
		p.available[a] = make(map[int]int)
	}
	if _, ok := p.available[b]; !ok {
		p.available[b] = make(map[int]int)
	}
	p.available[a][b]++
	p.available[b][a]++
}

func (p *Puzzle) remTile(a, b int) {
	p.available[a][b]--
	p.available[b][a]--
}

func (p *Puzzle) options(a int) []int {
	var o []int
	for b, count := range p.available[a] {
		if count != 0 {
			o = append(o, b)
		}
	}
	return o
}

// MakeChain returns a Domino chain if one exists.
func MakeChain(input []Domino) ([]Domino, bool) {
	return NewPuzzle(input).Solve()
}
