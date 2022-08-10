package purchase

import "fmt"

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	return kind == "car" || kind == "truck"
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {
	var want string
	if option1 < option2 {
		want = option1
	} else {
		want = option2
	}
	return fmt.Sprintf("%s is clearly the better choice.", want)
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {
	var percent float64
	if age < 3 {
		percent = 0.80
	} else if age < 10 {
		percent = 0.70
	} else {
		percent = 0.50
	}
	return originalPrice * percent
}
