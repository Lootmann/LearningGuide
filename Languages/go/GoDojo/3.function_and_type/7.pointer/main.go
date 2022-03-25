package main

import "fmt"

func f(xp *int) {
	*xp = 100
}

func swap(x, y int) (int, int) {
	return y, x
}

func swap2(x, y *int) {
	*x, *y = *y, *x
}

func main() {
	var x int = 10
	fmt.Println(x)

	f(&x)
	fmt.Println(x)

	// swap
	n, m := swap(10, 20)
	fmt.Println(n, m)

	swap2(&n, &m)
	fmt.Println(n, m)
}
