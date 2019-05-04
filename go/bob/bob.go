// Package bob solves Bob
package bob

import "regexp"

var (
	loud     = regexp.MustCompile("^[^[:lower:]]+[[:upper:]][^[:lower:]]+$")
	question = regexp.MustCompile("\\?[[:space:]]*$")
	shh      = regexp.MustCompile("^[[:space:]]*$")
)

// Hey responds to a remark.
func Hey(remark string) string {
	if loud.MatchString(remark) && question.MatchString(remark) {
		return "Calm down, I know what I'm doing!"
	} else if question.MatchString(remark) {
		return "Sure."
	} else if loud.MatchString(remark) {
		return "Whoa, chill out!"
	} else if shh.MatchString(remark) {
		return "Fine. Be that way!"
	} else {
		return "Whatever."
	}
}
