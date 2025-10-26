package twobucket

import "errors"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type bucket struct {
	name          string
	capacity      int
	volume, moves int
}

func (b *bucket) fillIfEmpty() {
	if b.volume == 0 {
		b.moves++
		b.volume = b.capacity
	}
}
func (b *bucket) emptyIfFull() {
	if b.volume == b.capacity {
		b.moves++
		b.volume = 0
	}
}
func (b *bucket) pourInto(other *bucket) {
	amount := min(b.volume, other.capacity-other.volume)
	if amount > 0 {
		b.moves++
		b.volume -= amount
		other.volume += amount
	}
}

// Solve the bucket puzzle.
func Solve(sizeBucketOne, sizeBucketTwo, goalAmount int, startBucket string) (string, int, int, error) {
	if sizeBucketOne == 0 || sizeBucketTwo == 0 || goalAmount == 0 || (startBucket != "one" && startBucket != "two") {
		return "", 0, 0, errors.New("no solution")
	}

	source := &bucket{name: "one", capacity: sizeBucketOne}
	dest := &bucket{name: "two", capacity: sizeBucketTwo}

	// If starting with bucket two, swap pour direction.
	if startBucket == "two" {
		source, dest = dest, source
	}

	// The first move must always be filling the source.
	source.fillIfEmpty()

	// Edge case: if goal == dest bucket size, fill the dest.
	if goalAmount == dest.capacity {
		dest.fillIfEmpty()
	}

	// Start the pouring! Stop when goal is hit.
	for source.volume != goalAmount && dest.volume != goalAmount {
		// In order to transfer, the source needs water and the dest needs space.
		source.fillIfEmpty()
		dest.emptyIfFull()
		// Loop detection.
		if source.volume == source.capacity && dest.volume == 0 && dest.moves > 0 {
			return "", 0, 0, errors.New("no solution")
		}
		source.pourInto(dest)
	}

	target, other := source, dest
	if dest.volume == goalAmount {
		target, other = other, target
	}
	moves := target.moves + other.moves
	return target.name, moves, other.volume, nil

}
