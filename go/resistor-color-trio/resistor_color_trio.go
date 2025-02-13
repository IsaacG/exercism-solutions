package resistorcolortrio

import (
	"fmt"
	"math"
	"slices"
)

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

var units = []string{"ohms", "kiloohms", "megaohms", "gigaohms"}

// Label describes the resistance value given the colors of a resistor.
// The label is a string with a resistance value with an unit appended
// (e.g. "33 ohms", "470 kiloohms").
func Label(colors []string) string {
	ohms := (slices.Index(Colors, colors[0])*10 + slices.Index(Colors, colors[1])) * int(math.Pow10(slices.Index(Colors, colors[2])))
	var places int
	for ; ohms > 1000; ohms = ohms / 1000 {
		places++
	}
	return fmt.Sprintf("%d %s", ohms, units[places])
}
