// Package listops solves listops.
package listops

type IntList []int
type binFunc func(x, y int) int
type predFunc func(n int) bool
type unaryFunc func(x int) int

func (i IntList) Foldl (f binFunc, res int) int {
	for _, v := range i {
		res = f(res, v)
	}
	return res
}

func (i IntList) Foldr (f binFunc, res int) int {
	for o, _ := range i {
		res = f(i[len(i) - o - 1], res)
	}
	return res
}

func (i IntList) Length () int {
	return len(i)
}

func (i IntList) Filter (f predFunc) IntList {
	ret := []int{}
	for _, v := range i {
		if f(v) {
			ret = append(ret, v)
		}
	}
	return ret
}

func (i IntList) Map (f unaryFunc) IntList {
	ret := make([]int, 0, len(i))
	for _, v := range i {
		ret = append(ret, f(v))
	}
	return ret
}

func (i IntList) Reverse () IntList {
	l := len(i)
	ret := make([]int, l)
	for o, v := range i {
		ret[l - o - 1] = v
	}
	return ret
}

func (i IntList) Append (j IntList) IntList {
	ret := make([]int, len(i) + len(j))
	for o, v := range i {
		ret[o] = v
	}
	for o, v := range j {
		ret[o + len(i)] = v
	}
	return ret
}

func (i IntList) Concat (j []IntList) IntList {
	for _, l := range j {
		i = i.Append(l)
	}
	return i
}

