// Package say says numbers in English.
package say

var (
	ones = []string{"zero", "one", "two", "three", "four", "five", "six",
		"seven", "eight", "nine", "ten", "eleven", "twelve",
		"thirteen", "fourteen", "fifteen", "sixteen",
		"seventeen", "eighteen", "ninteen"}
	tens = []string{"", "", "twenty", "thirty", "forty", "fifty", "sixty",
		"seventy", "eighty", "ninty"}
)

// saySmall handles numbers under 100, i.e. with no "place" holder.
func saySmall(n int64) string {
	out := tens[n/10]
	if n%10 != 0 {
		out += "-" + ones[n%10]
	}
	return out
}

// sayLarge says a number recursively.
func sayLarge(n int64, divisor int64, label string) string {
	out, _ := Say(n / divisor)
	out += " " + label
	if r := n % divisor; r != 0 {
		rest, _ := Say(r)
		out += " " + rest
	}
	return out
}

// Say returns an English version of a number.
// Algorithm from https://exercism.org/tracks/javascript/exercises/say/solutions/515ab00bc90f46b0bde3732d9317a46b
func Say(n int64) (string, bool) {
	if n < 0 {
		return "", false
	}
	switch {
	case n < 20:
		return ones[n], true
	case n < 100:
		return saySmall(n), true
	case n < 1000:
		return sayLarge(n, 100, "hundred"), true
	case n < 1000000:
		return sayLarge(n, 1000, "thousand"), true
	case n < 1000000000:
		return sayLarge(n, 1000000, "million"), true
	case n < 1000000000000:
		return sayLarge(n, 1000000000, "billion"), true
	default:
		return "", false
	}
}
