// Package weather handles weather info.
package weather

// CurrentCondition holds a condition.
var CurrentCondition string

// CurrentLocation stores the location.
var CurrentLocation string

// Forecast returns a weather forecase.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
