package beer

import (
	"errors"
	"fmt"
	"strings"
)

func Song() string {
	s, _ := Verses(99, 0)
	return s
}

func Verses(start, stop int) (string, error) {
	if start < stop {
		return "", errors.New("invalid")
	}
	var out []string
	for i := start; i >= stop; i-- {
		v, err := Verse(i)
		if err != nil {
			return "", err
		}
		out = append(out, v)
	}
	return strings.Join(out, "\n") + "\n", nil
}

func bottle(n int) string {
	if n > 1 {
		return fmt.Sprintf("%d bottles", n)
	}
	if n == 1 {
		return "1 bottle"
	}
	return "No more bottles"
}

func Verse(n int) (string, error) {
	if n < 0 || n >= 100 {
		return "", errors.New("invalid")
	}
	out := fmt.Sprintf("%s of beer on the wall, %s of beer.\n", bottle(n), strings.ToLower(bottle(n)))
	if n > 0 {
		subject := "one"
		if n == 1 {
			subject = "it"
		}
		out += fmt.Sprintf("Take %s down and pass it around, %s of beer on the wall.\n", subject, strings.ToLower(bottle(n-1)))
	} else {
		out += "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
	}
	return out, nil
}
