// Package twelve generates the Twelve Days.
package twelve

import (
	"fmt"
	"strings"
)

var (
	opening = "On the %s day of Christmas my true love gave to me: "
	item    = []string{
		"twelve Drummers Drumming",
		"eleven Pipers Piping",
		"ten Lords-a-Leaping",
		"nine Ladies Dancing",
		"eight Maids-a-Milking",
		"seven Swans-a-Swimming",
		"six Geese-a-Laying",
		"five Gold Rings",
		"four Calling Birds",
		"three French Hens",
		"two Turtle Doves",
		"and a Partridge in a Pear Tree.",
	}
	numbers = []string{
		"first", "second", "third", "fourth", "fifth", "sixth",
		"seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"}
)

// Verse generates a single verse.
func Verse(n int) string {
	v := fmt.Sprintf(opening, numbers[n-1])
	if n == 1 {
		return v + "a Partridge in a Pear Tree."
	}
	return v + strings.Join(item[12-n:12], ", ")
}

// Song generates the whole song.
func Song() string {
	s := make([]string, 12)
	for i := 0; i < 12; i++ {
		s[i] = Verse(i + 1)
	}
	return strings.Join(s, "\n") + "\n"
}
