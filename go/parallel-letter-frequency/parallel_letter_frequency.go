// Package letter counts letter frequency.
package letter

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

// ConcurrentFrequency computes Frequency in parallel.
func ConcurrentFrequency(inputs []string) FreqMap {
	// Launch multiple concurrent Frequency's.
	maps := make(chan FreqMap)
	for _, s := range inputs {
		s := s
		go func() { maps <- Frequency(s) }()
	}

	// Aggregate the results.
	result := FreqMap{}
	for range inputs {
		for r, v := range <-maps {
			result[r] += v
		}
	}
	return result
}
