package main

import "fmt"

func add(x int, y int) int {
	return x + y + 1
}

func swap(x, y int) (int, int) {
	return y, x
}

func swap1(x, y int) (x2, y2 int) {
	y2, x2 = x, y
	return
}

func main() {
	fmt.Println(add(1, 2))

	var x, y int = 1, 2
	fmt.Println(x, y)

	x, y = swap(x, y)
	fmt.Println(x, y)

	x, y = y, x
	fmt.Println(x, y)

	x, y = swap1(x, y)
	fmt.Println(x, y)

	// anonymous function
	func() {
		fmt.Println("hello world :^)")
	}()

	// function is first object
	fs := make([]func() string, 2)
	fs[0] = func() string { return "first" }
	fs[1] = func() string { return "second" }
	for i, f := range fs {
		fmt.Println(i, f())
	}

	// closure
	fs1 := make([]func(), 3)
	for i := range fs1 {
		fmt.Println("i = ", i)
		fs1[i] = func() { fmt.Println("i = ", i) }
	}

	fmt.Println()
	for _, f := range fs1 {
		f()
	}

	// copy
	p := struct {
		age  int
		name string
	}{age: 10, name: "Gopher"}

	p2 := p
	p2.age = 20

	fmt.Println(p)
	fmt.Println(p2)
}
