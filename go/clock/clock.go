// Package clock implements a date-less clock.
package clock

import "fmt"

// Clock represents a time-of-day.
type Clock int

const day = 24 * 60

// New returns a new Clock.
func New(hour, minute int) Clock {
	return Clock((((hour*60 + minute) % day) + day) % day)
}

// String converts a Clock to a string.
func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c/60, c%60)
}

// Add adds time to a Clock
func (c Clock) Add(minutes int) Clock {
	return New(0, int(c)+minutes)
}

// Subtract subtracts time from a Clock
func (c Clock) Subtract(minutes int) Clock {
	return New(0, int(c)-minutes)
}
