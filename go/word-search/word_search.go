package wordsearch


func Solve(words []string, puzzle []string) (map[string][2][2]int, error) {
	grid := make([][]rune, 0, len(words))
	notFound := make(map[int]map[string]struct{})
	notFoundCount := make(map[int]int)
	for i, word := range words {
		grid[i] = []rune(word)
		notFound[len(word)][word] = struct{}{}
		notFoundCount[len(word)]++
	}
	found := make(map[string][2][2]int)

	for each starting point {
		for each direction {
			get words, end, lengths
		}
		for len, word in found {
			if want word {
				found[word] = pos
				count[len] --
				del notFound[word]
			}
		}
	}

	foundAll := true
	for _, word := notFound {
		found[word] = -1, -1, -1, -1
		foundAll = false
	}

	return found, foundAll
}
