package minesweeper

import (
	"strconv"
	"strings"
)

type point struct{ x, y int }

// neighbors returns the 8 adjacent points.
func (p point) neighbors() []point {
	neighbors := make([]point, 0, 8)
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			if x != 0 || y != 0 {
				neighbors = append(neighbors, point{p.x + x, p.y + y})
			}
		}
	}
	return neighbors

}

type minefield struct {
	mines         map[point]bool
	width, height int
}

func newMinefield(board []string) minefield {
	mines := map[point]bool{}

	for y, line := range board {
		for x, char := range line {
			switch char {
			case '*':
				mines[point{x, y}] = true
			case ' ':
			default:
				panic("Invalid char " + string(char))
			}
		}
	}

	width := 0
	if len(board) > 0 {
		width = len(board[0])
	}

	return minefield{mines, width, len(board)}
}

// cell returns the annotation for a single cell.
func (m minefield) cell(p point) string {
	if m.mines[p] {
		return "*"
	}
	count := 0
	for _, n := range p.neighbors() {
		if m.mines[n] {
			count++
		}
	}
	if count == 0 {
		return " "
	}
	return strconv.Itoa(count)
}

func (m minefield) annotate() []string {
	out := make([]string, m.height)
	for y := 0; y < m.height; y++ {
		var sb strings.Builder
		for x := 0; x < m.width; x++ {
			sb.WriteString(m.cell(point{x, y}))
		}
		out[y] = sb.String()
	}
	return out
}

// Annotate returns an annotated board
func Annotate(board []string) []string {
	return newMinefield(board).annotate()
}
