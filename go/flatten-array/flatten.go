// Package flatten flattens arrays.
package flatten

// Flatten flattens arbitrary depth lists.
func Flatten(in interface{}) []interface{} {
	var out = []interface{}{}
	if list, ok := in.([]interface{}); ok {
		for _, i := range list {
			l := Flatten(i)
			for _, j := range l {
				out = append(out, j)
			}
		}
	} else if in == nil {
		out = []interface{}{}
	} else {
		out = []interface{}{in}
	}
	return out
}
