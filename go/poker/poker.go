package poker

import (
	"errors"
	"slices"
	"strconv"
	"strings"
)

// Ranks of hands.
const (
	royalFlush = iota
	straightFlush
	fourOfAKind
	fullHouse
	flush
	straight
	threeOfAKind
	twoPair
	onePair
	highCard
)

func cmp(a, b int) int {
	if a < b {
		return -1
	}
	if a > b {
		return +1
	}
	return 0
}

var faceCards = map[string]int{
	"J": 11,
	"Q": 12,
	"K": 13,
	"A": 14,
}

// Card represents a single card.
type Card struct {
	val  int
	suit rune
}

// Hand represents a hand of five cards.
type Hand struct {
	input string
	cards []Card
}

// Values returns the pip values of the cards in a hand.
func (h Hand) Values() []int {
	var out []int
	for _, c := range h.cards {
		out = append(out, c.val)
	}
	return out
}

// Count returns a slice of pairs containing the card value and how many times it appears.
func (h Hand) Count() [][2]int {
	counts := map[int]int{}
	for _, c := range h.cards {
		counts[c.val]++
	}
	var out [][2]int
	for val, count := range counts {
		out = append(out, [2]int{val, count})
	}
	slices.SortFunc(out, func(a, b [2]int) int {
		if a[1] == b[1] {
			return -cmp(a[0], b[0])
		}
		return -cmp(a[1], b[1])
	})
	return out
}

func (h Hand) isFlush() bool {
	for _, c := range h.cards {
		if c.suit != h.cards[0].suit {
			return false
		}
	}
	return true
}

func (h Hand) isRoyal() bool {
	return h.cards[0].val > 10
}

func (h Hand) isStraight() bool {
	vals := h.Values()
	// The first four cards must be in order.
	for i := range 3 {
		if vals[i] != vals[i+1]-1 {
			return false
		}
	}
	// The fifth card must be in order or the cards much be "2 ... A".
	return vals[3] == vals[4]-1 || (vals[0] == 2 && vals[4] == faceCards["A"])
}

// cmp compares two hands and determines the better hand.
func (h Hand) cmp(other Hand) int {
	rankA, valsA := h.Value()
	rankB, valsB := other.Value()
	// Compare ranks first.
	if rankA != rankB {
		return -cmp(rankA, rankB)
	}
	// For matching ranks, compare the card values.
	for idx, v := range valsA {
		if v != valsB[idx] {
			return cmp(v, valsB[idx])
		}
	}
	return 0
}

// On a straight, we need special handling for "2 3 4 5 A" vs "2 3 4 5 6". Return the lowest "value".
func (h Hand) straightValues() []int {
	vals := h.Values()
	if vals[0] == 2 && vals[4] == 14 {
		return []int{1}
	}
	return vals[:1]
}

// Value returns the rank and relevant card values of a hand.
func (h Hand) Value() (int, []int) {
	count := h.Count() // [][2]int{value, count}
	vals := h.Values()
	if h.isRoyal() && h.isFlush() && h.isStraight() {
		return royalFlush, h.straightValues()
	}
	if h.isFlush() && h.isStraight() {
		return straightFlush, h.straightValues()
	}
	if count[0][1] == 4 {
		return fourOfAKind, []int{count[0][0], count[1][0]}
	}
	if count[0][1] == 3 && count[1][1] == 2 {
		return fullHouse, []int{count[0][0], count[1][0]}
	}
	if h.isFlush() {
		vals := h.Values()
		slices.Reverse(vals)
		return flush, vals
	}
	if h.isStraight() {
		return straight, h.straightValues()
	}
	if count[0][1] == 3 {
		return threeOfAKind, []int{count[0][0], count[1][0], count[2][0]}
	}
	if count[0][1] == 2 && count[1][1] == 2 {
		return twoPair, []int{count[0][0], count[1][0], count[2][0]}
	}
	if count[0][1] == 2 {
		return onePair, []int{count[0][0], count[1][0], count[2][0], count[3][0]}
	}
	slices.Reverse(vals)
	return highCard, vals
}

// NewHand returns a hand, validating the input.
func NewHand(s string) (Hand, error) {
	var cards []Card
	for c := range strings.FieldsSeq(s) {
		var face string
		var suit rune
		runes := []rune(c)
		for idx, r := range runes {
			if r == '♤' || r == '♡' || r == '♢' || r == '♧' {
				if idx != len(runes)-1 {
					return Hand{}, errors.New("invalid card")
				}
				suit = r
			} else {
				face += string(r)
			}
		}

		if suit == 0 {
			return Hand{}, errors.New("invalid suit")
		}
		v, ok := faceCards[face]
		if !ok {
			v, _ = strconv.Atoi(face)
			if v < 2 || v > 10 {
				return Hand{}, errors.New("invalid value")
			}
		}
		cards = append(cards, Card{v, suit})
	}
	if len(cards) != 5 {
		return Hand{}, errors.New("invalid card count")
	}
	slices.SortFunc(cards, func(a, b Card) int { return cmp(a.val, b.val) })
	return Hand{s, cards}, nil
}

// BestHand returns the best hands.
func BestHand(hands []string) ([]string, error) {
	var cardHands []Hand
	for _, h := range hands {
		hand, err := NewHand(h)
		if err != nil {
			return nil, err
		}
		cardHands = append(cardHands, hand)
	}
	ranked := slices.Clone(cardHands)
	slices.SortFunc(ranked, func(a, b Hand) int {
		return -a.cmp(b)
	})

	var out []string
	for _, hand := range cardHands {
		if hand.cmp(ranked[0]) == 0 {
			out = append(out, hand.input)
		}
	}
	return out, nil
}
