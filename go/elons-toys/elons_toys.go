package elon

import "fmt"

// Car implements a remote controlled car.
type Car struct {
	speed        int
	batteryDrain int

	battery  int
	distance int
}

// Track implements a race track.
type Track struct {
	distance int
}

// CreateCar creates a new car with given specifications.
func CreateCar(speed, batteryDrain int) *Car {
	return &Car{
		speed, batteryDrain, 100, 0}
}

// CreateTrack creates a new track with given distance.
func CreateTrack(distance int) Track {
	return Track{distance}
}

// Drive drives the car one time.
func (c *Car) Drive() {
	if c.batteryDrain > c.battery {
		return
	}
	c.battery -= c.batteryDrain
	c.distance += c.speed
}

// CanFinish checks if a car is able to finish a certain track.
func (c *Car) CanFinish(track Track) bool {
	drives := int(c.battery / c.batteryDrain)
	distance := drives * c.speed
	return distance >= track.distance
}

// DisplayDistance displays the distance the car is driven.
func (c *Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %d meters", c.distance)
}

// DisplayBattery displays the battery level.
func (c *Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %d%%", c.battery)
}
