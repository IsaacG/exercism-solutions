package queenattack

import "fmt"

func position(p string) (int, int, error) {
	r := []rune(p)
	if len(r) != 2 {
		return 0, 0, fmt.Errorf("invalid position, %s", p)
	}
	if r[0] < 'a' || r[0] > 'h' {
		return 0, 0, fmt.Errorf("invalid file, %c", r[0])
	}
	if r[1] < '1' || r[1] > '8' {
		return 0, 0, fmt.Errorf("invalid file, %c", r[1])
	}
	return int(r[0] - 'a'), int(r[1] - '1'), nil
}

// CanQueenAttack returns if a queen can attack another.
func CanQueenAttack(whitePosition, blackPosition string) (bool, error) {
	if whitePosition == blackPosition {
		return false, fmt.Errorf("positions cannot be the same, %s", whitePosition)
	}
	wX, wY, err := position(whitePosition)
	if err != nil {
		return false, err
	}
	bX, bY, err := position(blackPosition)
	if err != nil {
		return false, err
	}

	canAttack := wX == bX || wY == bY || (wY-bY == wX-bX) || (wY-bY == bX-wX)
	return canAttack, nil
}
