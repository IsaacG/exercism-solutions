package stateoftictactoe

import (
	"errors"
	"strings"
)

type State string
type Point struct {
	x, y int
}
type Line []Point

const (
	Win     State  = "win"
	Ongoing State  = "ongoing"
	Draw    State  = "draw"
	Empty   string = " "
	O       string = "O"
	X       string = "X"
)

func isWin(pieces [][]string, player string) bool {
	var lines []Line

	var diagD, diagU Line
	for i := 0; i < 3; i++ {
		diagD = append(diagD, Point{i, i})
		diagU = append(diagU, Point{2 - i, i})
	}
	lines = append(lines, diagD, diagU)

	for i := 0; i < 3; i++ {
		var horiz, vert Line
		for j := 0; j < 3; j++ {
			horiz = append(horiz, Point{i, j})
			vert = append(vert, Point{j, i})
		}
		lines = append(lines, horiz, vert)
	}

	for _, line := range lines {
		if pieces[line[0].x][line[0].y] != player {
			continue
		}
		if pieces[line[0].x][line[0].y] == pieces[line[1].x][line[1].y] &&
			pieces[line[0].x][line[0].y] == pieces[line[2].x][line[2].y] {
			return true
		}
	}
	return false
}

func count(pieces [][]string) (int, int) {
	var x, o int
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			switch pieces[i][j] {
			case X:
				x++
			case O:
				o++
			}
		}
	}
	return x, o
}

func StateOfTicTacToe(board []string) (State, error) {
	var pieces [][]string
	for _, line := range board {
		pieces = append(pieces, strings.Split(line, ""))
	}
	if x, o := count(pieces); o > x || x-o > 1 {
		return "", errors.New("Invalid move count")
	}
	if isWin(pieces, X) && isWin(pieces, O) {
		return "", errors.New("Cannot have two winners")
	}
	if isWin(pieces, X) || isWin(pieces, O) {
		return Win, nil
	}
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if pieces[i][j] == Empty {
				return Ongoing, nil
			}
		}
	}
	return Draw, nil
}
