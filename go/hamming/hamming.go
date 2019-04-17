// Package hamming computes Hamming distances
package hamming

import "errors"

// Distance computers a Hamming distance.
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("strings must be the same size")
	}

	d := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			d++
		}
	}
	return d, nil
}
