package tournament

import (
	"errors"
	"fmt"
	"io"
	"io/ioutil"
	"sort"
	"strings"
)

type tally struct {
	played int
	won    int
	draw   int
	lost   int
	points int
	name   string
}

type byScore []*tally

func (a byScore) Len() int      { return len(a) }
func (a byScore) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a byScore) Less(i, j int) bool {
	if a[i].points != a[j].points {
		return a[i].points > a[j].points
	}
	return a[i].name < a[j].name
}

func addWin(t *tally) {
	t.played++
	t.points += 3
	t.won++
}

func addLoss(t *tally) {
	t.played++
	t.lost++
}

func addDraw(t *tally) {
	t.played++
	t.points++
	t.draw++
}

func writeHeader(w io.Writer) {
	io.WriteString(w, fmt.Sprintf("%-30s | %2s | %2s | %2s | %2s | %2s\n", "Team", "MP", "W", "D", "L", "P"))
}

func writeTally(w io.Writer, t *tally) {
	io.WriteString(w, fmt.Sprintf("%-30s | %2d | %2d | %2d | %2d | %2d\n", t.name, t.played, t.won, t.draw, t.lost, t.points))
}

// Tally tallies scores.
func Tally(r io.Reader, w io.Writer) error {
	b, err := ioutil.ReadAll(r)
	if err != nil {
		return errors.New("failed to read")
	}

	score := make(map[string]*tally)
	for _, line := range strings.Split(string(b), "\n") {
		if len(line) == 0 || line[0] == '#' {
			continue
		}
		fields := strings.Split(line, ";")
		if len(fields) != 3 {
			return fmt.Errorf("line does not contain three fields: %s", line)
		}
		if fields[2] != "win" && fields[2] != "draw" && fields[2] != "loss" {
			return errors.New("invalid match result")
		}

		teamA, teamB, result := fields[0], fields[1], fields[2]
		if _, ok := score[teamA]; !ok {
			score[teamA] = &tally{name: teamA}
		}
		if _, ok := score[teamB]; !ok {
			score[teamB] = &tally{name: teamB}
		}
		if result == "win" {
			addWin(score[teamA])
			addLoss(score[teamB])
		} else if result == "loss" {
			addLoss(score[teamA])
			addWin(score[teamB])
		} else {
			addDraw(score[teamA])
			addDraw(score[teamB])
		}
	}

	// Sort the team tallies.
	tallies := []*tally{}
	for _, t := range score {
		tallies = append(tallies, t)
	}
	sort.Sort(byScore(tallies))

	// Write the results.
	writeHeader(w)
	for _, t := range tallies {
		writeTally(w, t)
	}
	return nil
}
