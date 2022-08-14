package beer

import (
	"fmt"
	"strconv"
	"strings"
)

func Song() string {
	s, _ := Verses(99, 0)
	return s
}

func Verses(start, stop int) (string, error) {
	if start < stop {
		return "", fmt.Errorf("invalid start, stop [%d, %d]; expected start >= stop", start, stop)
	}
	var b strings.Builder
	for i := start; i >= stop; i-- {
		v, err := Verse(i)
		if err != nil {
			return "", err
		}
		b.WriteString(v + "\n")
	}
	return b.String(), nil
}

func bottle(n int) string {
	if n > 1 {
		return strconv.Itoa(n) + " bottles"
	}
	if n == 1 {
		return "1 bottle"
	}
	return "No more bottles"
}

func Verse(n int) (string, error) {
	if n < 0 || n >= 100 {
		return "", fmt.Errorf("invalid number of bottles, %d; must be [0, 99]", n)
	}
	// out := fmt.Sprintf("%s of beer on the wall, %s of beer.\n", bottle(n), strings.ToLower(bottle(n)))
	out := bottle(n) + " of beer on the wall, " + strings.ToLower(bottle(n)) + " of beer.\n"
	if n > 0 {
		subject := "one"
		if n == 1 {
			subject = "it"
		}
		out += "Take " + subject + " down and pass it around, " + strings.ToLower(bottle(n-1)) + " of beer on the wall.\n"
	} else {
		out += "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
	}
	return out, nil
}
