package dndcharacter

import "math/rand"

type Character struct {
	Strength     int
	Dexterity    int
	Constitution int
	Intelligence int
	Wisdom       int
	Charisma     int
	Hitpoints    int
}

// Modifier calculates the ability modifier for a given ability score
func Modifier(score int) int {
	if score < 10 {
		score--
	}
	return (score - 10) / 2
}

// Ability uses randomness to generate the score for an ability
func Ability() int {
	var total int
	smallest := 7
	for range 4 {
		roll := rand.Intn(6) + 1
		if roll < smallest {
			smallest = roll
		}
		total += roll
	}
	return total - smallest
}

// GenerateCharacter creates a new Character with random scores for abilities
func GenerateCharacter() Character {
	con := Ability()
	return Character{
		Ability(),
		Ability(),
		con,
		Ability(),
		Ability(),
		Ability(),
		10 + Modifier(con),
	}
}
