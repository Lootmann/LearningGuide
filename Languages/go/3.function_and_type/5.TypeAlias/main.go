package main

import "fmt"

type Counter int

func main() {
	var count Counter
	fmt.Println("count = ", count)

	count += 1
	fmt.Println("count = ", count)
}
