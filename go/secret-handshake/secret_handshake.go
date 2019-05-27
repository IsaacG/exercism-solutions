// Package secret interprets a secret handshake.
package secret

// Handshake performs the secret handshake.
func Handshake(code uint) []string {
	actions := []string{"wink", "double blink", "close your eyes", "jump"}
	response := make([]string, 0, 4)
	for i, act := range actions {
		if 1<<uint(i)&code != 0 {
			response = append(response, act)
		}
	}
	if 1<<4&code == 0 {
		return response
	}

	rev := make([]string, len(response))
	for i, act := range response {
		rev[len(rev)-1-i] = act
	}
	return rev
}
