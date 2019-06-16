// Package allergies solves allergies.
package allergies

var allergens = []string{"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"}

// Allergies computes allergies based on a score.
func Allergies(code uint) []string {
	var results []string
	for i := uint(0); i < uint(len(allergens)); i++ {
		if 1<<i&code != 0 {
			results = append(results, allergens[i])
		}
	}
	return results
}

// AllergicTo computes if allergic to an allergen based on a score.
func AllergicTo(code uint, allergen string) bool {
	for _, a := range Allergies(code) {
		if a == allergen {
			return true
		}
	}
	return false
}
