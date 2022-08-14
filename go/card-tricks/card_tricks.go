// Package cards does card tricks.
package cards

func FavoriteCards() []int {
	return []int{2, 6, 9}
}

func PrependItems(slice []int, values ...int) []int {
	cards := make([]int, len(slice)+len(values))
	copy(cards, values)
	copy(cards[len(values):], slice)
	return cards
}

// GetItem retrieves an item from a slice at given position. The second return value indicates whether
// a the given index existed in the slice or not.
func GetItem(slice []int, index int) int {
	if index >= len(slice) || index < 0 {
		return -1
	}
	return slice[index]
}

// SetItem writes an item to a slice at given position overwriting an existing value.
// If the index is out of range it is be appended.
func SetItem(slice []int, index, value int) []int {
	if index >= len(slice) || index < 0 {
		return append(slice, value)
	}
	slice[index] = value
	return slice
}

// PrefilledSlice creates a slice of given length and prefills it with the given value.
func PrefilledSlice(value, length int) []int {
	if length < 0 {
		return nil
	}
	slice := make([]int, 0, length)
	for i := 0; i < length; i++ {
		slice = append(slice, value)
	}
	return slice
}

// RemoveItem removes an item from a slice by modifying the existing slice.
func RemoveItem(slice []int, index int) []int {
	if index > len(slice) || index < 0 {
		return slice
	}
	return append(slice[0:index], slice[index+1:]...)
}
