package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func Title(msg string) {
	fmt.Printf("\n>>> %s", msg)
}

func Walk() error {
	fmt.Println(">>> Walk()")
	err := filepath.Walk(".", func(path string, info os.FileInfo, err error) error {
		if filepath.Ext(path) == ".go" {
			fmt.Println(path)
		}
		return nil
	})

	if err != nil {
		return err
	}

	return nil
}

func main() {
	// file path
	Title("file path")
	path := filepath.Join("dir", "main.go")

	fmt.Println(filepath.Ext(path))
	fmt.Println(filepath.Base(path))
	fmt.Println(filepath.Dir(path))

	// directory walk
	Title("directory walk")
	Walk()
}
