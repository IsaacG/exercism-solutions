// Package meteorology formats data.
package meteorology

import "fmt"

// TemperatureUnit is a unit of temperature.
type TemperatureUnit int

const (
	// Celsius unit.
	Celsius TemperatureUnit = 0
	// Fahrenheit unit.
	Fahrenheit TemperatureUnit = 1
)

// String returns a string format for TemperatureUnit.
func (t TemperatureUnit) String() string {
	switch t {
	case Celsius:
		return "°C"
	case Fahrenheit:
		return "°F"
	default:
		panic("Unknown unit")
	}
}

// Temperature data.
type Temperature struct {
	degree int
	unit   TemperatureUnit
}

// String returns a string format for Temperature.
func (t Temperature) String() string {
	return fmt.Sprintf("%d %s", t.degree, t.unit)
}

// SpeedUnit is a unit of speed.
type SpeedUnit int

const (
	// KmPerHour unit.
	KmPerHour SpeedUnit = 0
	// MilesPerHour unit.
	MilesPerHour SpeedUnit = 1
)

// String returns a string format for SpeedUnit.
func (s SpeedUnit) String() string {
	switch s {
	case KmPerHour:
		return "km/h"
	case MilesPerHour:
		return "mph"
	default:
		panic("Unknown unit")
	}
}

// Speed data.
type Speed struct {
	magnitude int
	unit      SpeedUnit
}

// String returns a string format for Speed.
func (s Speed) String() string {
	return fmt.Sprintf("%d %s", s.magnitude, s.unit)
}

// MeteorologyData data.
type MeteorologyData struct {
	location      string
	temperature   Temperature
	windDirection string
	windSpeed     Speed
	humidity      int
}

// String returns a string format for MeteorologyData.
func (m MeteorologyData) String() string {
	return fmt.Sprintf("%s: %s, Wind %s at %s, %d%% Humidity", m.location, m.temperature, m.windDirection, m.windSpeed, m.humidity)
}
