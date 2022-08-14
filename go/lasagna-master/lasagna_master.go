package lasagna

// PreparationTime returns how long it takes to prepare.
func PreparationTime(layers []string, time int) int {
	if time == 0 {
		time = 2
	}
	return len(layers) * time
}

// Quantities returns the quantity of noodles and sauce needed.
func Quantities(layers []string) (int, float64) {
	var noodles int
	var sauce float64
	for _, contents := range layers {
		if contents == "noodles" {
			noodles += 50
		} else if contents == "sauce" {
			sauce += 0.2
		}
	}
	return noodles, sauce
}

// AddSecretIngredient adds an ingredient to the list.
func AddSecretIngredient(friendList, myList []string) {
	myList[len(myList)-1] = friendList[len(friendList)-1]
}

// ScaleRecipe scales recipe amounts.
func ScaleRecipe(amounts []float64, portions int) []float64 {
	out := make([]float64, 0, len(amounts))
	scale := float64(portions) / 2
	for _, amount := range amounts {
		out = append(out, amount*scale)
	}
	return out
}
