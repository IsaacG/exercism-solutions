package railfence

import "strings"

// heights returns which rails we visit, in what order.
func heights(message string, rails int) []int {
	var heights []int
	for idx := range rails - 1 {
		heights = append(heights, idx)
	}
	for idx := range rails - 1 {
		heights = append(heights, rails - idx - 1)
	}
	return heights
}

/// writeZigZag returns a fence with a message written out to the rails in a zig zag.
func writeZigZag(message string, rails int) [][]rune {
	heights := heights(message, rails)

	// Set up the fence rails.
	var fence [][]rune
	for range rails {
		fence = append(fence, []rune{})
	}


	// Populate the fence rails.
	for idx, char := range message {
		rail := heights[idx % len(heights)]
		fence[rail] = append(fence[rail], char)
	}
	return fence
}

// Encode returns an encoded message.
func Encode(message string, rails int) string {
	// Write to the rails in a zig zag. Collect the rails.
	var out strings.Builder
	for _, rail := range writeZigZag(message, rails) {
		out.WriteString(string(rail))
	}

	return out.String()
}

// Decode returns an decoded message.
func Decode(message string, rails int) string {
	var fence [][]rune

	// Use a zig zag to determine how many runes go on each rail.
	// Write the message out to the rails.
	var start int
	for _, zig := range writeZigZag(message, rails) {
		l := len(zig)
		fence = append(fence, []rune(message[start:start+l]))
		start += l
	}

	// Read the rails in a zig zag to contruct the decoded message.
	heights := heights(message, rails)
	var out strings.Builder
	for idx := range len(message) {
		rail := heights[idx % len(heights)]
		out.WriteRune(fence[rail][0])
		fence[rail] = fence[rail][1:]
	}
	return out.String()
}
