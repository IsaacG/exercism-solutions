// Package brackets checks for pairs brackets.
package brackets

var open = map[rune]rune{
	']': '[',
	')': '(',
	'}': '{',
}

// Bracket checks for balanced brackets.
func Bracket(s string) bool {
	var stack []rune
	var r rune

	for _, c := range s {
		switch c {
		case '[', '(', '{':
			stack = append(stack, c)
		case ']', ')', '}':
			r = open[c]
			if len(stack) == 0 || stack[len(stack)-1] != r {
				return false
			}
			stack = stack[:len(stack)-1]
		}

	}
	return len(stack) == 0
}
