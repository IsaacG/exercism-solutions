package main

import (
	"./luhn"
	"fmt"
)

func main() {
	fmt.Printf("%r", luhn.Valid("059"))
}
