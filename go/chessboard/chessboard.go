package chessboard

// File stores if a square is occupied by a piece - this will be a slice of bools
type File []bool

// Chessboard contains a map of eight Ranks, accessed with values from 1 to 8
type Chessboard map[string]File

// CountInFile returns how many squares are occupied in the chessboard,
// within the given rank
func CountInFile(cb Chessboard, rank string) int {
	var count int
	for _, occupied := range cb[rank] {
		if occupied {
			count++
		}
	}
	return count
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given file
func CountInRank(cb Chessboard, file int) int {
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
		count += CountInFile(cb, i)
	}
	return count
}
