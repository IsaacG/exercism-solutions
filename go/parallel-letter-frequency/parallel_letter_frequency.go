// Package letter counts letter frequency.
package letter

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
