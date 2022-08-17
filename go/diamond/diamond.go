package diamond

import (
	"bytes"
	"fmt"
)

// A is the value of 'A'.
const A = int('A')

// Gen returns a diamond pattern string.
func Gen(char byte) (string, error) {
	if char < 'A' || char > 'Z' {
		return "", fmt.Errorf("invalid char %b not in range [A, Z]", char)
	}

	length := int(char) - A
	rowLength := (length * 2) + 1
	blankRow := bytes.Repeat([]byte{' '}, rowLength)

	// Precompute all the rows, since we need them twice.
	rows := make([][]byte, rowLength)
	for i := 0; i <= length; i++ {
		// Fill the row with spaces.
		rows[i] = make([]byte, rowLength)
		copy(rows[i], blankRow)
		// Insert the char on either side of center.
		rows[i][length-i] = byte(A + i)
		rows[i][length+i] = byte(A + i)
	}

	var buf bytes.Buffer

	// Write the top half.
	for i := 0; i < length; i++ {
		buf.Write(rows[i])
		buf.WriteByte('\n')
	}
	// Write the bottom half.
	for i := length; i > 0; i-- {
		buf.Write(rows[i])
		buf.WriteByte('\n')
	}
	// Final row, no newline.
	buf.Write(rows[0])

	return buf.String(), nil
}
