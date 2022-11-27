package bottlesong

import (
	"fmt"
	"strings"
)

var numbers = []string{"No", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"}

func bottles(num int) string {
	var format string
	if num == 1 {
		format = "%s green bottle"
	} else {
		format = "%s green bottles"
	}
	return fmt.Sprintf(format, numbers[num])
}

// Recite returns song verses.
func Recite(startBottles, takeDown int) []string {
	verses := make([]string, 0, takeDown*5)
	for i := startBottles; i > startBottles-takeDown; i-- {
		verses = append(verses, fmt.Sprintf("%s hanging on the wall,", bottles(i)))
		verses = append(verses, fmt.Sprintf("%s hanging on the wall,", bottles(i)))
		verses = append(verses, "And if one green bottle should accidentally fall,")
		verses = append(verses, fmt.Sprintf("There'll be %s hanging on the wall.", strings.ToLower(bottles(i-1))))
		verses = append(verses, "")
	}
	return verses[:takeDown*5-1]
}
