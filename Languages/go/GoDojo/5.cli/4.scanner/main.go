package main

import (
	"bufio"
	"fmt"
	"os"
)

func scanner_test() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		if line := scanner.Text(); line == "" {
			break
		} else {
			fmt.Println(line)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "Fail to reader", err)
	}
}

func main() {
	scanner_test()
}
