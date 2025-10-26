package bowling

import (
	"errors"
	"fmt"
	"slices"
)

// sum returns the sum of a slice of ints.
func sum(vals []int) int {
	var total int
	for _, v := range vals {
		total += v
	}
	return total
}

// Frame stores one game frame.
type Frame struct {
	num   int
	rolls []int
	next  *Frame
}

// nextTwoRolls returns two more rolls for use in computing a strike or spare.
func (f *Frame) nextTwoRolls() []int {
	rolls := slices.Clone(f.next.rolls)
	if len(rolls) > 2 {
		rolls = rolls[:2]
	} else if len(rolls) < 2 {
		rolls = append(rolls, f.next.next.rolls[0])
	}
	return rolls
}

// score returns the score of a frame, handling a strike or spare.
func (f *Frame) score() int {
	if len(f.rolls) == 0 {
		return 0
	}
	total := sum(f.rolls)
	if f.num < 9 {
		if f.rolls[0] == 10 {
			total += sum(f.nextTwoRolls())
		} else if total == 10 {
			total += f.nextTwoRolls()[0]
		}
	}
	return total
}

// full returns if a frame is full/complete.
func (f *Frame) full() bool {
	if f.num < 9 {
		return len(f.rolls) == 2 || (len(f.rolls) == 1 && f.rolls[0] == 10)
	}
	return len(f.rolls) == 3 || (len(f.rolls) == 2 && f.rolls[0]+f.rolls[1] < 10)
}

// Game represents a bowling game.
type Game struct {
	frames   []*Frame
	frameIdx int
}

// NewGame returns a new Game with the first frame ready to use.
func NewGame() *Game {
	return &Game{frames: []*Frame{&Frame{}}}
}

// bumpFrame adds the next Frame to a game if the current frame is full.
func (g *Game) bumpFrame() {
	frame := g.frames[g.frameIdx]
	if frame.full() && g.frameIdx < 10 {
		g.frameIdx++
		new := &Frame{num: g.frameIdx}
		frame.next = new
		g.frames = append(g.frames, new)
	}
}

// Roll adds a roll to the game.
func (g *Game) Roll(pins int) error {
	if pins < 0 || pins > 10 {
		return errors.New("invalid pins")
	}
	frame := g.frames[g.frameIdx]
	var priorRoll int
	if len(frame.rolls) > 0 {
		priorRoll = frame.rolls[len(frame.rolls)-1]
	}
	if pins == 60 {
		fmt.Println("prior", priorRoll)
	}
	if g.frameIdx < 9 && len(frame.rolls) > 0 && priorRoll != 10 && priorRoll+pins > 10 {
		return errors.New("invalid frame")
	}
	if g.frameIdx == 9 && sum(frame.rolls) != 10 && priorRoll != 10 && priorRoll+pins > 10 {
		return errors.New("invalid frame")
	}
	if g.frameIdx >= 10 {
		return errors.New("invalid game over")
	}
	frame.rolls = append(frame.rolls, pins)
	g.bumpFrame()

	return nil
}

// Score returns the score of a game.
func (g *Game) Score() (int, error) {
	if g.frameIdx != 10 {
		return 0, errors.New("game not over")
	}
	var total int
	for _, f := range g.frames {
		total += f.score()
	}
	return total, nil
}
