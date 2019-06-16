// Package phonenumber cleans up phone numbers.
package phonenumber

import (
	"errors"
	"fmt"
)

// Number cleans and validates a phone number.
func Number(s string) (string, error) {
	t := make([]rune, 0, 12)
	for _, c := range s {
		if c < '0' || c > '9' {
			continue
		}
		t = append(t, c)
		if len(t) > 10 {
			break
		}
	}
	s = string(t)

	if len(s) == 11 {
		if s[0] == '1' {
			s = s[1:]
		} else {
			return "", errors.New("10 digit numbers must start with a '1'")
		}
	}
	if len(s) != 10 {
		return "", errors.New("number must be 9 or 10 digits")
	}
	if s[0] == '0' || s[0] == '1' {
		return "", errors.New("invalid area code")
	}
	if s[3] == '0' || s[3] == '1' {
		return "", errors.New("invalid exchange code")
	}
	return s, nil
}

// AreaCode returns a number's area code.
func AreaCode(s string) (string, error) {
	s, err := Number(s)
	if err != nil {
		return "", err
	}
	return s[0:3], nil
}

// Format formats a number all pretty-like.
func Format(s string) (string, error) {
	s, err := Number(s)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("(%s) %s-%s", s[0:3], s[3:6], s[6:10]), nil
}
