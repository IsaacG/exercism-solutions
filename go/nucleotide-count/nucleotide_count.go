// Package dna counts nucleotides.
package dna

import "errors"

// Histogram is a mapping from nucleotide to its count in given DNA.
type Histogram map[byte]int

// DNA is a list of nucleotides. Choose a suitable data type.
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
// Returns an error if d contains an invalid nucleotide.
func (d DNA) Counts() (Histogram, error) {
	var h Histogram = map[byte]int{'A': 0, 'C': 0, 'G': 0, 'T': 0}
	for i := 0; i < len(d); i++ {
		c := d[i]
		if c != 'A' && c != 'C' && c != 'G' && c != 'T' {
			return nil, errors.New("invalid DNA")
		}
		h[c]++
	}
	return h, nil
}
