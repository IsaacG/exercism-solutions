// Package cipher implements a simple cipher.
package cipher

import (
	"strings"
	"unicode"
)


func scrub(s string) []rune {
	t := make([]rune, 0, len(s))
	for _, r := range strings.ToLower(s) {
		if !unicode.IsLetter(r) {
			continue
		}
		t = append(t, r)
	}
	return t
}


type Caesar struct {
	cipher *Shift
}


func NewCaesar () *Caesar {
	return &Caesar{NewShift(3)}
}


func (c Caesar) Encode (s string) string {
	return c.cipher.Encode(s)
}


func (c Caesar) Decode (s string) string {
	return c.cipher.Decode(s)
}


type Shift struct {
	distance int
}


func NewShift (distance int) *Shift {
	if distance >= 26 || distance <= -26 || distance == 0 {
		return nil
	}
	if distance < 0 {
		distance += 26
	}
	return &Shift{distance % 26}
}


func (c Shift) rotate (s string, d int) string {
	t := scrub(s)
	for i, r := range t {
		t[i] = rune((int(r-'a')+d)%26) + 'a'
	}
	return string(t)
}


func (c Shift) Encode (s string) string {
	return c.rotate(s, c.distance)
}


func (c Shift) Decode (s string) string {
	return c.rotate(s, 26 - c.distance)
}


type Vigenere struct {
	phrase string
}


func NewVigenere (phrase string) *Vigenere {
	if len(phrase) < 4 {
		return nil
	}
	if string(scrub(phrase)) != phrase {
		return nil
	}
	return &Vigenere{phrase}
}


func (c Vigenere) rotate (s string, encode bool) string {
	t := scrub(s)
	p_len := len(c.phrase)
	for i, r := range t {
		d := rune(c.phrase[i % p_len]) - 'a'
		if ! encode {
			d *= -1
		}
		t[i] = r + d
		if (t[i] > 'z') {
			t[i] -= rune(26)
		} else if (t[i] < 'a') {
			t[i] += rune(26)
		}
	}
	return string(t)
}

func (c Vigenere) Encode (s string) string {
	return c.rotate(s, true)
}

func (c Vigenere) Decode (s string) string {
	return c.rotate(s, false)
}

