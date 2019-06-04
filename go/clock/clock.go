// Package clock implements a date-less clock.
package clock

import "fmt"

// Clock represents a time, seconds since midnight.
type Clock int

const day = 24 * 60

func toPos(val int) int {
	return ((val % day) + day) % day
}

// New returns a new Clock.
func New(hour, minute int) Clock {
	return Clock(toPos(hour*60 + minute))
}

// String converts a Clock to a string.
func (c Clock) String() string {
	t := int(c) % day
	return fmt.Sprintf("%02d:%02d", t/60, t%60)
}

// Add adds time to a Clock
func (c Clock) Add(minutes int) Clock {
	return New(0, int(c)+minutes)
}

// Subtract subtracts time from a Clock
func (c Clock) Subtract(minutes int) Clock {
	return New(0, int(c)-minutes)
}
