package main

import "fmt"

type Counter int

// method
func (c *Counter) increment() {
	*c += 1
}

// method
func (c *Counter) decrement() {
	*c -= 1
}

// method
func (c Counter) String() string {
	return fmt.Sprintf("counter = %d", c)
}

type Hex int

// method
func (h Hex) String() string {
	return fmt.Sprintf("%x", int(h))
}

func main() {
	var hex Hex = 100
	fmt.Println(hex.String())

	var counter Counter = 0

	counter.increment()
	counter.increment()
	counter.increment()
	counter.increment()
	fmt.Println(counter.String())

	counter.decrement()
	counter.decrement()
	fmt.Println(counter.String())

	f := Hex.String
	fmt.Println(f(hex))
}
