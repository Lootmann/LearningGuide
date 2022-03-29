package main

import "fmt"

func f() {
	n := 100
	fmt.Println(n)
}

func g() {
	n := 200
	fmt.Println(n)
}

var msg string = "string"

func h() {
	fmt.Println(msg)
}

func main() {
	f()
	g()

	h()
	msg = "hi, Gophers"
	h()
}
