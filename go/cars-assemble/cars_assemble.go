// Package cars does car math.
package cars

// SuccessRate is used to calculate the ratio of an item being created without
// error for a given speed
func SuccessRate(speed int) float64 {
	if speed == 0 {
		return 0.0
	} else if speed < 5 {
		return 1.00
	} else if speed < 9 {
		return 0.90
	} else {
		return 0.77
	}
}

// CalculateProductionRatePerHour for the assembly line, taking into account
// its success rate
func CalculateProductionRatePerHour(speed int) float64 {
	return float64(speed*221) * SuccessRate(speed)
}

// CalculateProductionRatePerMinute describes how many working items are
// produced by the assembly line every minute
func CalculateProductionRatePerMinute(speed int) int {
	return int(CalculateProductionRatePerHour(speed) / 60)
}

func CalculateWorkingCarsPerMinute(prod int, success float64) int {
	return int(CalculateWorkingCarsPerHour(prod, success) / 60.0)
}

func CalculateWorkingCarsPerHour(prod int, success float64) float64 {
	return float64(prod) * success / 100
}

func CalculateCost(num int) uint {
	return uint(95000*(num/10) + 10000*(num%10))
}
