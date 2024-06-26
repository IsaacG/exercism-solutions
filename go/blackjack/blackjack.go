package blackjack

// Actions
const (
	STAND = "S"
	HIT   = "H"
	SPLIT = "P"
	WIN   = "W"
)

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	case "ten", "jack", "queen", "king":
		return 10
	default:
		return 0
	}
}

// IsBlackjack returns true if the player has a blackjack, false otherwise.
func IsBlackjack(card1, card2 string) bool {
	return ParseCard(card1)+ParseCard(card2) == 21
}

// LargeHand implements the decision tree for hand scores larger than 20 points.
func LargeHand(isBlackjack bool, dealerScore int) string {
	switch {
	case !isBlackjack && dealerScore == 11:
		return "P"
	case isBlackjack && dealerScore < 10:
		return "W"
	default:
		return "S"
	}
}

// SmallHand implements the decision tree for hand scores with less than 21 points.
func SmallHand(handScore, dealerScore int) string {
	switch {
	case handScore >= 17:
		return "S"
	case handScore <= 11:
		return "H"
	case dealerScore >= 7:
		return "H"
	default:
		return "S"
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	handVal := ParseCard(card1) + ParseCard(card2)
	if handVal == 22 {
		return SPLIT
	}
	if handVal == 21 && ParseCard(dealerCard) < 10 {
		return WIN
	}
	if handVal >= 17 {
		return STAND
	}
	if handVal >= 12 && ParseCard(dealerCard) < 7 {
		return STAND
	}
	return HIT
}
