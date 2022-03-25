package main

import "fmt"

func main() {
	var sum int
	sum = 5 + 6 + 3
	avg := float32(sum) / 3

	// error
	// compare int with float
	if avg > 4.5 {
		fmt.Println("good")
	}

	var a, b, c bool
	if a && b || !c {
		fmt.Println("true")
	} else {
		fmt.Println("false")
	}
}
