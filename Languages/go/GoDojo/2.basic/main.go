package main

import (
	"fmt"
	"math/rand"
	"time"
)

func out() int {
	return 2
}

func odd_even(length int) {
	for i := 0; i < length; i++ {
		var msg string
		if i%2 == 0 {
			msg = fmt.Sprintf("%d-odd", i)
		} else {
			msg = fmt.Sprintf("%d-even", i)
		}
		fmt.Println(msg)
	}
}

func title(str string) {
	fmt.Printf(">>> %s\n", str)
}

func lottery() {
	t := time.Now().UnixNano()
	rand.Seed(t)
	s := rand.Intn(6) + 1

	var lot string
	switch s {
	case 6:
		lot = "大吉"
	case 4, 5:
		lot = "中吉"
	case 2, 3:
		lot = "吉"
	case 1:
		lot = "凶"
	}
	fmt.Println(lot)
}

func main() {
	var n int = 100
	fmt.Println(n)

	x := "hello world"
	fmt.Printf("name: %s\n", x)
	fmt.Println("hello world")

	const k int = 999
	fmt.Println("k = ", k)

	const (
		a = 1 + 1
		b
		c
	)
	fmt.Println(a, b, c)

	{
		const (
			a = iota
			b
		)
		fmt.Println(a, b)

		const (
			c = 1 << iota
			d
			e
		)
		fmt.Println(c, d, e)
	}

	msg := "foo" + "bar"
	fmt.Println(msg)

	if a := out(); a >= 3 {
		fmt.Println("a >= ", a)
	} else {
		fmt.Println("a < ", a)
	}

	// switch
	title("switch")
	var num int = 10
	switch num {
	case 1, 10, 100:
		fmt.Println("1, 10, 100")
	default:
		fmt.Println("default")
	}

	// for
	title("for")
	{
		var sum int = 0
		for i := 0; i <= 100; i++ {
			sum += i
		}
		fmt.Println(sum)
	}

	// for range
	title("for range")
	{
		for i, v := range []int{1, 2, 3, 4, 5} {
			fmt.Println(i, v)
		}
	}

	// rand
	title("Lottery")
	for i := 0; i < 6; i++ {
		lottery()
	}

	// odd even
	title("odd even function")
	odd_even(10)
}
