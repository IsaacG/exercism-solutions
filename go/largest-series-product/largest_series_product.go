// Package lsproduct solves lsproduct.
package lsproduct

import (
	"errors"
	"strconv"
	"strings"
)

// digits converts a string to a list of ints.
func digits(s string) ([]int, error){
	ret := make([]int, 0, len(s))
	for _, c := range s {
		i, err := strconv.Atoi(string(c))
		if err != nil {
			return nil, err
		}
		ret = append(ret, i)
	}
	return ret, nil
}

// LargestSeriesProduct computers the largest product in a series.
func LargestSeriesProduct(s string, span int) (int, error) {
	var max int

	// Input validation.
	if span == 0 {
		return 1, nil
	} else if span < 1 {
		return 0, errors.New("bad span")
	} else if len(s) < span {
		return 0, errors.New("string too short")
	}

	// Spans containing "0" are 0. Ignore and handle spans between 0's.
	for _, ss := range strings.Split(s, "0") {
		p, err := lsp(ss, span)
		if err != nil {
			return 0, err
		}
		if max < p {
			max = p
		}
	}
	return max, nil
}

// Walk a span and compute the largest product by removing the first element and adding the last.
func lsp(s string, span int) (int, error) {
	if len(s) < span {
		return 0, nil
	}

	d, err := digits(s)
	if err != nil {
		return 0, err
	}

	prod := 1
	max := 0
	// Initial span.
	for i := 0; i < span; i++ {
		prod *= d[i]
	}
	max = prod

	// Shift the span over and recompute.
	for i := 0; i + span < len(d); i++ {
		prod /= d[i]
		prod *= d[i + span]
		if prod > max {
			max = prod
		}
	}

	return max, nil
}
