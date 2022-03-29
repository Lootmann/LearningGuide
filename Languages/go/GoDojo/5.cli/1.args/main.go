package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

var msg = flag.String("msg", "default value", "description")
var n int

func init() {
	flag.IntVar(&n, "n", 1, "times")
}

func main() {
	flag.Parse()
	fmt.Println(strings.Repeat(*msg, n))

	fmt.Println(os.Args)
}
