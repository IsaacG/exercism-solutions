// Package robotname names robots.
package robotname

import (
	"errors"
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var used = make(map[string]bool)
var letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
var rnd *rand.Rand
var mutex sync.Mutex

func init() {
	rnd = rand.New(rand.NewSource(time.Now().UnixNano()))
}

func getName() (string, error) {
	mutex.Lock()
	defer mutex.Unlock()
	if len(used) == 26*26*10*10*10 {
		return "", errors.New("out of names")
	}
	var n string
	for {
		n = fmt.Sprintf(
			"%c%c%d%d%d",
			letters[rnd.Intn(26)],
			letters[rnd.Intn(26)],
			rnd.Intn(10),
			rnd.Intn(10),
			rnd.Intn(10))
		if _, ok := used[n]; !ok {
			break
		}
	}
	used[n] = true
	return n, nil
}

// Robot is a named machine.
type Robot struct {
	name string
}

// Name returns the robot's name.
func (r *Robot) Name() (string, error) {
	if r.name == "" {
		n, err := getName()
		if err != nil {
			return "", err
		}
		r.name = n
	}
	return r.name, nil
}

// Reset resets the robot's name.
func (r *Robot) Reset() {
	r.name = ""
}
