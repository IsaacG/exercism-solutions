package wordy

import (
	"regexp"
	"strconv"
	"strings"
)

var operations = map[*regexp.Regexp]func(a, b int) int{
	regexp.MustCompile(`^(.*) multiplied by (-?\d+)$`): func(a, b int) int { return a * b },
	regexp.MustCompile(`^(.*) divided by (-?\d+)$`):    func(a, b int) int { return a / b },
	regexp.MustCompile(`^(.*) plus (-?\d+)$`):          func(a, b int) int { return a + b },
	regexp.MustCompile(`^(.*) minus (-?\d+)$`):         func(a, b int) int { return a - b },
}

func solve(question string) (int, bool) {
	v, err := strconv.Atoi(question)
	if err == nil {
		return v, true
	}
	for re, op := range operations {
		if m := re.FindStringSubmatch(question); m != nil {
			a, okA := solve(m[1])
			b, okB := solve(m[2])
			if okA && okB {
				return op(a, b), true
			}
		}
	}
	return 0, false
}

// Answer returns an int answer to a string question.
func Answer(question string) (int, bool) {
	if !strings.HasPrefix(question, "What is ") {
		return 0, false
	}
	if !strings.HasSuffix(question, "?") {
		return 0, false
	}
	question = strings.TrimPrefix(question, "What is ")
	question = strings.TrimSuffix(question, "?")
	return solve(question)
}
