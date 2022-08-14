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

// Rotate returns a rotated direction.
func (d Dir) Rotate(a Action) Dir {
	switch a {
	case 'R':
		return (d + 1) % 4
	case 'L':
		return (d + 3) % 4
	default:
		panic("invalid rotation " + string(a))
	}
}

// Right rotates Step1Robot to the right.
func Right() {
	Step1Robot.Dir = Step1Robot.Dir.Rotate('R')
}

// Left rotates Step1Robot to the left.
func Left() {
	Step1Robot.Dir = Step1Robot.Dir.Rotate('L')
}

// Advance advances Step1Robot.
func Advance() {
	switch Step1Robot.Dir {
	case N:
		Step1Robot.Y++
	case E:
		Step1Robot.X++
	case S:
		Step1Robot.Y--
	case W:
		Step1Robot.X--
	}
}

func (d Dir) String() string {
	switch d {
	case N:
		return "North"
	case E:
		return "East"
	case S:
		return "South"
	case W:
		return "West"
	default:
		panic("invalid direction")
	}
}

// ================================
// ============ Step 2 ============
// ================================

// Contains returns if a Pos is within a Rect.
func (r Rect) Contains(p Pos) bool {
	if !(r.Min.Easting <= p.Easting && p.Easting <= r.Max.Easting) {
		return false
	}
	if !(r.Min.Northing <= p.Northing && p.Northing <= r.Max.Northing) {
		return false
	}
	return true
}

// Shift returns a shifted position.
func (p Pos) Shift(d Dir) Pos {
	switch d {
	case N:
		return Pos{p.Easting + 0, p.Northing + 1}
	case E:
		return Pos{p.Easting + 1, p.Northing + 0}
	case S:
		return Pos{p.Easting + 0, p.Northing - 1}
	case W:
		return Pos{p.Easting - 1, p.Northing + 0}
	default:
		panic("invalid direction")
	}
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
			robot.Dir = robot.Dir.Rotate(a)
		case 'A':
			newPos := robot.Pos.Shift(robot.Dir)
			if extent.Contains(newPos) {
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

// ValidateRobots checks for invalid setup and returns the map.
func ValidateRobots(extent Rect, robots []Step3Robot) (map[string]*Step3Robot, string) {
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
		if !extent.Contains(robot.Pos) {
			errMsg = "Robot placed outside of a room: " + robot.Name
		}
		robotMap[robot.Name] = &robots[i]
	}
	return robotMap, errMsg
}

// Room3 handles actions from multiple robots.
func Room3(extent Rect, robots []Step3Robot, action chan Action3, report chan []Step3Robot, log chan string) {
	defer close(report)

	robotMap, errMsg := ValidateRobots(extent, robots)
	if errMsg != "" {
		log <- errMsg
		return
	}

	// Keep track of whether any robot is still active.
	active := len(robots)

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
			robot.Dir = robot.Dir.Rotate(act.Act)
		case act.Act == 'A':
			newPos := robot.Pos.Shift(robot.Dir)
			logMsg := ""
			if !extent.Contains(newPos) {
				logMsg = "Robot attempted to walk into a wall: " + act.Name
			}
			for otherName, other := range robotMap {
				if otherName != act.Name && other.Pos == newPos {
					logMsg = "Robot " + act.Name + " attempted to walk into " + otherName
				}
			}
			if logMsg == "" {
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
