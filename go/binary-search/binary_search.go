package binarysearch

// SearchInts returns the index of an int in a list using a binary search.
func SearchInts(list []int, key int) int {
	for low, high := 0, len(list); low != high; {
		mid := (high + low) / 2
		val := list[mid]
		switch {
		case val == key:
			return mid
		case val > key:
			high = mid
		default:
			low = mid + 1
		}
	}

	return -1
}
