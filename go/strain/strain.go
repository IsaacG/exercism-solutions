// Package strain does straining.
package strain

type Ints []int
type Lists [][]int
type Strings []string

func (i Ints) Keep(f func(int) bool) Ints {
	var ret Ints
	for _, v := range i {
		if f(v) {
			ret = append(ret, v)
		}
	}
	return ret
}

func (i Ints) Discard(f func(int) bool) Ints {
	return i.Keep(func(v int) bool { return ! f(v) })
}

func (l Lists) Keep(f func([]int) bool) Lists {
	var ret Lists
	for _, v := range l {
		if f(v) {
			ret = append(ret, v)
		}
	}
	return ret
}

func (s Strings) Keep(f func(string) bool) Strings {
	var ret Strings
	for _, v := range s {
		if f(v) {
			ret = append(ret, v)
		}
	}
	return ret
}
