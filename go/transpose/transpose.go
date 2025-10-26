package transpose

import (
	"slices"
	"strings"
)

// Transpose a slice of strings.
func Transpose(input []string) []string {
	// Compute the longest line length.
	var longest int
	for _, line := range input {
		if len(line) > longest {
			longest = len(line)
		}
	}

	var out []string
	var priorLen int
	for idx := range longest {
		// Work in reverse to handle length padding - each line must be as long as the next line.
		idx = longest - idx - 1
		result := ""
		for _, line := range input {
			if idx < len(line) {
				result += string(line[idx])
			} else {
				result += " "
			}
		}
		// Strip trailing spaces then add back as much as is needed.
		result = strings.TrimRight(result, " ")
		for i := len(result); i < priorLen; i++ {
			result += " "
		}
		priorLen = len(result)
		out = append(out, result)
	}
	slices.Reverse(out)
	return out
}
