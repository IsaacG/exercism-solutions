package forth

import (
	"fmt"
	"strconv"
	"strings"
)

// emulator contains emulator details: the stack and any custom definitions.
type emulator struct {
	stack     []int
	operators map[string][]string
}

// define handles a ": name ... ;" definition.
func (e *emulator) define(line []string) error {
	l := len(line)
	if l < 4 || line[0] != ":" || line[l-1] != ";" {
		return fmt.Errorf("malformed define, %v", line)
	}
	// The custom command name cannot be an integer.
	if _, err := strconv.Atoi(line[1]); err == nil {
		return fmt.Errorf("invalid define %s", line[1])
	}
	var operation []string
	for _, w := range line[2 : l-1] {
		// When storing a definition, expand existing definitions.
		if o, ok := e.operators[w]; ok {
			operation = append(operation, o...)
		} else {
			operation = append(operation, w)
		}
	}
	e.operators[line[1]] = operation
	return nil
}

// Evalute a command that operates on the stack.
func (e *emulator) stackOp(op string, count int) error {
	l := len(e.stack)
	if l < count {
		return fmt.Errorf("%s requires %d values; stack size is %d", op, count, l)
	}
	// Read the operands from the stack.
	var result, operands []int
	for i := range count {
		operands = append(operands, e.stack[l-count+i])
	}
	switch op {
	case "+":
		result = []int{operands[0] + operands[1]}
	case "-":
		result = []int{operands[0] - operands[1]}
	case "*":
		result = []int{operands[0] * operands[1]}
	case "/":
		if op == "/" && operands[1] == 0 {
			return fmt.Errorf("illegal division by zero")
		}
		result = []int{operands[0] / operands[1]}
	case "DUP":
		result = []int{operands[0], operands[0]}
	case "DROP":
		result = []int{}
	case "SWAP":
		result = []int{operands[1], operands[0]}
	case "OVER":
		result = []int{operands[0], operands[1], operands[0]}
	}
	// Update the stack.
	e.stack = append(e.stack[:l-count], result...)
	return nil
}

// eval evaluates one line.
func (e *emulator) eval(line []string) error {
	if line[0] == ":" {
		return e.define(line)
	}
	for _, word := range line {
		var err error
		var val int
		if val, err = strconv.Atoi(word); err == nil {
			// Integers get pushed to the stack.
			e.stack = append(e.stack, val)
		} else if v, ok := e.operators[word]; ok {
			// Custom definitions take precendence over built-in operators.
			err = e.eval(v)
		} else {
			switch word {
			case "+", "-", "*", "/":
				err = e.stackOp(word, 2)
			case "DUP", "DROP":
				err = e.stackOp(word, 1)
			case "SWAP", "OVER":
				err = e.stackOp(word, 2)
			default:
				return fmt.Errorf("invalid command %s", word)
			}
		}
		if err != nil {
			return err
		}
	}
	return nil
}

// Forth emulates a Forth program.
func Forth(input []string) ([]int, error) {
	e := &emulator{nil, map[string][]string{}}
	for _, line := range input {
		if err := e.eval(strings.Fields(strings.ToUpper(line))); err != nil {
			return nil, err
		}
	}
	return e.stack, nil
}
