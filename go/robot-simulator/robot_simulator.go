// Package robot proviodes a robot simulator.
package robot

// ================================
// ============ Step 1 ============
// ================================
const (
	N Dir = 0 // North
	E Dir = 1 // East
	S Dir = 2 // South
	W Dir = 3 // West
)

var directions = map[Dir]string{
	N: "North",
	E: "East",
	S: "South",
	W: "West",
}
var movement = map[Dir]complex128{
	N: complex(0, 1),
	E: complex(1, 0),
	S: complex(0, -1),
	W: complex(-1, 0),
}
var rotation = map[Action]Dir{
	'R': 1,
	'L': 3,
}

// rotate returns a rotated direction.
func (d Dir) rotate(a Action) Dir {
	return (d + rotation[a]) % 4
}

// Right rotates Step1Robot to the right.
func Right() {
	Step1Robot.Dir = Step1Robot.Dir.rotate('R')
}

// Left rotates Step1Robot to the left.
func Left() {
	Step1Robot.Dir = Step1Robot.Dir.rotate('L')
}

// Advance advances Step1Robot.
func Advance() {
	newPos := complex(float64(Step1Robot.X), float64(Step1Robot.Y)) + movement[Step1Robot.Dir]
	Step1Robot.X, Step1Robot.Y = int(real(newPos)), int(imag(newPos))
}

func (d Dir) String() string {
	if s, ok := directions[d]; !ok {
		panic("invalid direction")
	} else {
		return s
	}
}

// ================================
// ============ Step 2 ============
// ================================

// contains returns if a Pos is within a Rect.
func (r Rect) contains(p Pos) bool {
	return ((r.Min.Easting <= p.Easting && p.Easting <= r.Max.Easting) &&
		(r.Min.Northing <= p.Northing && p.Northing <= r.Max.Northing))
}

// shift returns a shifted position.
func (p Pos) shift(d Dir) Pos {
	newPos := complex(float64(p.Easting), float64(p.Northing)) + movement[d]
	return Pos{RU(real(newPos)), RU(imag(newPos))}
}

// Action is simply a command.
type Action Command

// StartRobot tells the room to perform commands.
func StartRobot(command chan Command, action chan Action) {
	for c := range command {
		action <- Action(c)
	}
	close(action)
}

// Room handles robot actions.
func Room(extent Rect, robot Step2Robot, action chan Action, report chan Step2Robot) {
	for a := range action {
		switch a {
		case 'R', 'L':
			robot.Dir = robot.Dir.rotate(a)
		case 'A':
			newPos := robot.Pos.shift(robot.Dir)
			if extent.contains(newPos) {
				robot.Pos = newPos
			}
		}
	}
	report <- robot
	close(report)
}

// ================================
// ============ Step 3 ============
// ================================

// Action3 is a robot's action.
type Action3 struct {
	Name string // Name of the robot performing the action.
	Act  Action // Action being performed.
	Done bool   // Set when the script is done.
}

// StartRobot3 performs robot actions then signals when done.
func StartRobot3(name, script string, action chan Action3, log chan string) {
	for _, c := range script {
		action <- Action3{name, Action(c), false}
	}
	action <- Action3{name, 0, true}
}

// validateRobots checks for invalid setup and returns the map.
func validateRobots(extent Rect, robots []Step3Robot) (map[string]*Step3Robot, string) {
	robotMap := map[string]*Step3Robot{}
	errMsg := ""
	for i, robot := range robots {
		if robot.Name == "" {
			errMsg = "Robot has no name"
		}
		if _, ok := robotMap[robot.Name]; ok {
			errMsg = "Duplicate robot name: " + robot.Name
		}
		for _, other := range robotMap {
			if robot.Pos == other.Pos {
				errMsg = "Two robots placed in the same position"
			}
		}
		if !extent.contains(robot.Pos) {
			errMsg = "Robot placed outside of a room: " + robot.Name
		}
		robotMap[robot.Name] = &robots[i]
	}
	return robotMap, errMsg
}

func validateMove(extent Rect, robotMap map[string]*Step3Robot, positions <-chan futureMove, results chan<- string) {
	for f := range positions {
		res := ""
		if !extent.contains(f.pos) {
			res = "Robot attempted to walk into a wall: " + f.name
		}
		for otherName, other := range robotMap {
			if otherName != f.name && other.Pos == f.pos {
				res = "Robot " + f.name + " attempted to walk into " + otherName
			}
		}
		results <- res
	}
}

type futureMove struct {
	name string
	pos  Pos
}

// Room3 handles actions from multiple robots.
func Room3(extent Rect, robots []Step3Robot, action chan Action3, report chan []Step3Robot, log chan string) {
	defer close(report)

	robotMap, errMsg := validateRobots(extent, robots)
	if errMsg != "" {
		log <- errMsg
		return
	}

	// Keep track of whether any robot is still active.
	active := len(robots)

	posValidate := make(chan futureMove)
	posResult := make(chan string)
	defer close(posValidate)
	defer close(posResult)
	go validateMove(extent, robotMap, posValidate, posResult)

	// Process actions.
	for act := range action {
		robot, ok := robotMap[act.Name]
		if !ok {
			log <- "Received a command from an unknown robot, " + act.Name
			return
		}

		switch {
		case act.Act == 0 && act.Done:
			active--
		case act.Act == 'R' || act.Act == 'L':
			robot.Dir = robot.Dir.rotate(act.Act)
		case act.Act == 'A':
			newPos := robot.Pos.shift(robot.Dir)
			posValidate <- futureMove{act.Name, newPos}
			if logMsg := <-posResult; logMsg == "" {
				robot.Pos = newPos
			} else {
				log <- logMsg
			}
		default:
			log <- "Invalid command: " + string(act.Act)
			return
		}
		if active == 0 {
			break
		}
	}
	report <- robots
}
