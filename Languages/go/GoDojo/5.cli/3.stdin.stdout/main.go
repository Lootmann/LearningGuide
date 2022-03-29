package main

import (
	"errors"
	"fmt"
	"log"
	"os"
)

func doError() error {
	return errors.New("Noooo")
}

func f() {
	if err := doError(); err != nil {
		log.Fatal(err)
	}
}

func main() {
	defer fmt.Println("hello world")
	defer fmt.Println("hi greeting")

	fmt.Fprintln(os.Stdout, "Error")
	fmt.Fprintln(os.Stderr, "Hello")
}
