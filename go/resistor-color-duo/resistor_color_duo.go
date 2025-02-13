package resistorcolorduo

import "slices"

var Colors = []string{
		"black",
		"brown",
		"red",
		"orange",
		"yellow",
		"green",
		"blue",
		"violet",
		"grey",
		"white",
	}

// Value should return the resistance value of a resistor with a given colors.
func Value(colors []string) int {
	return slices.Index(Colors, colors[0]) * 10 + slices.Index(Colors, colors[1])
}
