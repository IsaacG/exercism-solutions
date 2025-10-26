package matrix

import (
	"strconv"
	"strings"
)

// Pair stores a coordinate.
type Pair struct{ row, col int }

// Matrix is used to get a saddle point.
type Matrix struct {
	data           [][]int
	width, height  int
	rowMax, colMin []int
}

// New returns a Matrix for a string.
func New(s string) (*Matrix, error) {
	var data [][]int
	var rowMax []int
	for line := range strings.SplitSeq(s, "\n") {
		if line == "" {
			break
		}
		var row []int
		max := 0
		for word := range strings.FieldsSeq(line) {
			num, err := strconv.Atoi(word)
			if err != nil {
				return nil, err
			}
			row = append(row, num)
			if num > max {
				max = num
			}
		}
		rowMax = append(rowMax, max)
		data = append(data, row)
	}
	columns := 0
	if len(data) != 0 {
		columns = len(data[0])
	}
	colMin := make([]int, columns)
	for col := range columns {
		min := 0
		for row := range data {
			if row == 0 || data[row][col] < min {
				min = data[row][col]
			}
		}
		colMin[col] = min
	}

	height := len(data)
	var width int
	if height > 0 {
		width = len(data[0])
	}
	return &Matrix{data, width, height, rowMax, colMin}, nil
}

// Saddle returns saddle points for a Matrix.
func (m *Matrix) Saddle() []Pair {
	pairs := []Pair{}
	for row := range m.height {
		for col := range m.width {
			// Check if this location has an optimal height.
			if height := m.data[row][col]; height == m.rowMax[row] && height == m.colMin[col] {
				pairs = append(pairs, Pair{row + 1, col + 1})
			}
		}
	}
	return pairs
}
