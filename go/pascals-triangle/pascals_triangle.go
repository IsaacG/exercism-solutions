// Package pascal drawns a Pascal's triangle.
package pascal

// Triangle generates a Triangle.
func Triangle(n int) [][]int {
	t := make([][]int, 0)
	t = append(t, []int{1})
	for i := 1; i < n; i++ {
		r := []int{1}
		for j := 1; j < len(t[i-1]); j++ {
			r = append(r, t[i-1][j-1]+t[i-1][j])
		}
		r = append(r, 1)
		t = append(t, r)
	}
	return t
}
