// Package gigasecond solves gigasecond.
package gigasecond

// import path for the time package from the standard library
import "time"

// AddGigasecond adds 10^9
func AddGigasecond(t time.Time) time.Time {
	return t.Add((1000000000) * time.Second)
}
