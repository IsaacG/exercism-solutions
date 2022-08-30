// Package say says numbers in English.
package say

import "strings"

var (
	ones = []string{"zero", "one", "two", "three", "four", "five", "six",
		"seven", "eight", "nine", "ten", "eleven", "twelve",
		"thirteen", "fourteen", "fifteen", "sixteen",
		"seventeen", "eighteen", "ninteen"}
	tens = []string{"", "", "twenty", "thirty", "forty", "fifty", "sixty",
		"seventy", "eighty", "ninty"}
)

// saySmall handles numbers under 100, i.e. with no "place" holder.
func saySmall(sb *strings.Builder, n int64) {
	sb.WriteString(tens[n/10])
	if n%10 != 0 {
		sb.WriteString("-" + ones[n%10])
	}
}

// sayLarge says a number recursively.
func sayLarge(sb *strings.Builder, n int64, divisor int64, label string) {
	sayBuilder(sb, n/divisor)
	sb.WriteString(" " + label)
	if r := n % divisor; r != 0 {
		sb.WriteRune(' ')
		sayBuilder(sb, r)
	}
}

// Algorithm from https://exercism.org/tracks/javascript/exercises/say/solutions/515ab00bc90f46b0bde3732d9317a46b
func sayBuilder(sb *strings.Builder, n int64) bool {
	if n < 0 || n >= 1_000_000_000_000 {
		return false
	}
	switch {
	case n < 20:
		sb.WriteString(ones[n])
	case n < 100:
		saySmall(sb, n)
	case n < 1_000:
		sayLarge(sb, n, 100, "hundred")
	case n < 1_000_000:
		sayLarge(sb, n, 1_000, "thousand")
	case n < 1_000_000_000:
		sayLarge(sb, n, 1_000_000, "million")
	case n < 1_000_000_000_000:
		sayLarge(sb, n, 1_000_000_000, "billion")
	}
	return true
}

// Say returns an English version of a number.
func Say(n int64) (string, bool) {
	sb := &strings.Builder{}
	if ok := sayBuilder(sb, n); !ok {
		return "", false
	} else {
		return sb.String(), true
	}
}
