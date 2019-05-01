// Package etl solves ETL.
package etl

import "strings"

// Transform one map to another.
func Transform(in map[int][]string) map[string]int {
	out := make(map[string]int)
	for score, chars := range in {
		for _, c := range chars {
			out[strings.ToLower(c)] = score
		}
	}
	return out
}
