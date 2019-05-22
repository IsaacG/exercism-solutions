package main

import (
	"./isbn-verifier"
	"fmt"
)

func main() {
	fmt.Printf("IsValidISBN(3-598-21507-X) %v\n", isbn.IsValidISBN("3-598-21507-X"))
}
