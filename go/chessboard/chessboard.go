package chessboard

// Rank stores if a square is occupied by a piece - this will be a slice of bools
type Rank []bool

// Chessboard contains a map of eight Ranks, accessed with values from 1 to 8
type Chessboard map[int]Rank

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank
func CountInRank(cb Chessboard, rank int) int {
	var count int
	for _, occupied := range cb[rank] {
		if occupied {
			count++
		}
	}
	return count
}

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file
func CountInFile(cb Chessboard, file int) int {
	if file < 1 || file > 8 {
		return 0
	}
	var count int
	for _, rank := range cb {
		if rank[file-1] {
			count++
		}
	}
	return count
}

// CountAll should count how many squares are present in the chessboard
func CountAll(cb Chessboard) (ret int) {
	var count int
	for _, rank := range cb {
		for range rank {
			count++
		}
	}
	return count
}

// CountOccupied returns how many squares are occupied in the chessboard
func CountOccupied(cb Chessboard) (ret int) {
	var count int
	for i := range cb {
		count += CountInRank(cb, i)
	}
	return count
}
