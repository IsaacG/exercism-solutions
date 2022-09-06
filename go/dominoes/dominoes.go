// Package dominoes builds a chain of dominoes.
package dominoes

// Domino is a single tile with two int values.
type Domino [2]int

// Chain is a list of dominoes.
type Chain []Domino

// closes returns if a Chain makes a closed loop.
func (c Chain) closes() bool {
	return len(c) == 0 || c[0][0] == c[len(c)-1][1]
}

// matches returns if a domino can be added on top of prior.
func (d Domino) matches(prior *Domino) bool {
	return prior == nil || prior[1] == d[0]
}

// orientations returns all domino orientations.
func (d Domino) orientations() []Domino {
	return []Domino{{d[0], d[1]}, {d[1], d[0]}}
}

// without returns a Chain with one element removed.
func (c Chain) without(i int) Chain {
	newHand := make(Chain, len(c)-1)
	copy(newHand, c[0:i])
	copy(newHand[i:], c[i+1:])
	return newHand
}

// makeLine tries to build a connected line of dominoes.
func (c Chain) makeLine(prior *Domino) []Chain {
	switch len(c) {
	case 0:
		// Chain of length 0 is a valid Chain.
		return []Chain{{}}
	case 1:
		if c[0].matches(prior) {
			return []Chain{Chain{c[0]}}
		}
		return []Chain{}
	}
	var lines []Chain
	// Try using each available Domino is any orientation to build a chain.
	for i := 0; i < len(c); i++ {
		for _, domino := range c[i].orientations() {
			if !domino.matches(prior) {
				continue
			}
			for _, chain := range c.without(i).makeLine(&domino) {
				lines = append(lines, append(Chain{domino}, chain...))
			}
		}
	}
	return lines
}

// MakeChain returns a Domino Chain if one exists.
func MakeChain(input []Domino) (Chain, bool) {
	for _, chain := range Chain(input).makeLine(nil) {
		if chain.closes() {
			return chain, true
		}
	}
	return nil, false
}
