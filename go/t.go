package main

import (
	"./linked-list"
	"fmt"
)

func main() {
	l := linkedlist.NewList([]interface{}{1, 2, 3, 4})
	fmt.Printf("%s\n", l)
}
