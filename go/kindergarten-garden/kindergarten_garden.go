package kindergarten

import (
	"errors"
	"sort"
	"strings"
)

// Garden stores a class garden.
type Garden map[string][]byte

var plants = map[byte]string{
	'C': "clover",
	'G': "grass",
	'R': "radishes",
	'V': "violets",
}

// NewGarden returns a garden from a diagram.
func NewGarden(diagram string, children []string) (*Garden, error) {
	rows := strings.Split(diagram, "\n")
	if len(rows) != 3 {
		return nil, errors.New("diagram should contain 3 lines")
	}
	if len(rows[0]) != 0 {
		return nil, errors.New("diagram should start with newline")
	}
	if len(rows[1]) != len(rows[2]) {
		return nil, errors.New("rows must be same size")
	}
	if len(rows[1]) != 2*len(children) {
		return nil, errors.New("rows contain two cups per child")
	}
	for _, c := range diagram {
		if c == '\n' {
			continue
		}
		if _, ok := plants[byte(c)]; !ok {
			return nil, errors.New("invalid cup code " + string(c))
		}
	}
	garden := make(Garden, len(children))
	c := make([]string, len(children))
	copy(c, children)
	sort.Slice(c, func(i, j int) bool { return c[i] < c[j] })
	for i, child := range c {
		if _, ok := garden[child]; ok {
			return nil, errors.New("duplicate child name, " + child)
		}
		garden[child] = make([]byte, 4)
		garden[child][0] = rows[1][2*i]
		garden[child][1] = rows[1][2*i+1]
		garden[child][2] = rows[2][2*i]
		garden[child][3] = rows[2][2*i+1]
	}
	return &garden, nil
}

// Plants returns the plants for a child.
func (g *Garden) Plants(child string) ([]string, bool) {
	cups, ok := (*g)[child]
	if !ok {
		return nil, false
	}
	p := make([]string, 4)
	for i := 0; i < 4; i++ {
		p[i] = plants[cups[i]]
	}
	return p, true
}
