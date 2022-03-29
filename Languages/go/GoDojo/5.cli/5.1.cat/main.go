//
// mycat -n hoge.txt fuga.txt
//
package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
)

func cat_files(filenames []string, show_linenumber bool) {
	var linenumber int = 1

	for _, filename := range filenames {
		fp, err := os.Open(filename)
		if err != nil {
		}
		defer fp.Close()

		scanner := bufio.NewScanner(fp)

		for scanner.Scan() {
			if show_linenumber {
				fmt.Printf("%d: %s\n", linenumber, scanner.Text())
				linenumber += 1
			} else {
				fmt.Println(scanner.Text())
			}
		}
	}
}

var n bool

func main() {
	fmt.Println(">>> run")

	var show_linenumber *bool = flag.Bool("n", false, "")
	flag.Parse()
	var filenames []string = flag.Args()

	cat_files(filenames, *show_linenumber)
}
