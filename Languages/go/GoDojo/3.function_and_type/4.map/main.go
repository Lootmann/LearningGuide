package main

import "fmt"

func main() {
	var m map[string]int
	m = make(map[string]int)
	fmt.Println(m, len(m))

	var m1 map[string]int
	m1 = make(map[string]int)
	fmt.Println(m1, len(m1))

	m2 := map[string]int{"x": 10, "y": 20}
	fmt.Println(m2)
	fmt.Println(m2["x"])

	x, ok := m2["x"]
	fmt.Println(x, ok)

	z, no := m2["z"]
	fmt.Println(z, no)
}
