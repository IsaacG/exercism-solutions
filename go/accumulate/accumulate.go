// Package accumulate stuff
package accumulate

func Accumulate(in []string, f func(string)string) []string {
	var res []string
	for _, i := range in {
		res = append(res, f(i))
	}
	return res
}
