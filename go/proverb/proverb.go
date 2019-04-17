// Package proverb generates proverb-ish lines.
package proverb

import "fmt"

// Proverb returns a proverb from rhyming inputs.
func Proverb(rhyme []string) []string {
	r := []string{}
	for i := 0; i+1 < len(rhyme); i++ {
		r = append(r, fmt.Sprintf("For want of a %s the %s was lost.", rhyme[i], rhyme[i+1]))
	}
	if len(rhyme) > 0 {
		r = append(r, fmt.Sprintf("And all for the want of a %s.", rhyme[0]))
	}
	return r
}
