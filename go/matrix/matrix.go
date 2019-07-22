// Package matrix handles a matrix.
package matrix

import (
	"errors"
	"strconv"
	"strings"
)

// Matrix represents a matrix.
type Matrix struct {
	rows [][]int
}

// New returns a new matrix from string.
func New(in string) (*Matrix, error) {
	var rows [][]int
	var cols = -1
	for _, line := range strings.Split(in, "\n") {
		row := make([]int, 0)
		for _, val := range strings.Split(strings.TrimSpace(line), " ") {
			i, err := strconv.Atoi(val)
			if err != nil {
				return nil, err
			}
			row = append(row, i)
		}
		if cols == -1 {
			cols = len(row)
		} else if cols != len(row) {
			return nil, errors.New("inconsistent length")
		}
		rows = append(rows, row)
	}
	return &Matrix{rows}, nil
}

// Rows returns the rows of a matric.
func (m *Matrix) Rows() [][]int {
	rows := make([][]int, len(m.rows))
	for i, r := range m.rows {
		row := make([]int, len(r))
		for j, c := range r {
			row[j] = c
		}
		rows[i] = row
	}
	return rows
}

// Cols returns the columns of a matric.
func (m *Matrix) Cols() [][]int {
	if len(m.rows) == 0 {
		return nil
	}
	cols := make([][]int, len(m.rows[0]))
	for i := 0; i < len(m.rows[0]); i++ {
		cols[i] = make([]int, len(m.rows))
	}
	for i, r := range m.rows {
		for j, c := range r {
			cols[j][i] = c
		}
	}
	return cols
}

// Set sets a matrix value.
func (m *Matrix) Set(x, y, val int) bool {
	if len(m.rows) == 0 {
		return false
	}
	if x < 0 || y < 0 {
		return false
	}
	if x >= len(m.rows) || y >= len(m.rows[x]) {
		return false
	}
	m.rows[x][y] = val
	return true
}
