package main

import "fmt"

func title(msg string) {
	fmt.Printf(">>> %s\n", msg)
}

func main() {

	title("array")
	var ns [5]int
	for i := 0; i < 5; i++ {
		ns[i] = i + 1
	}

	for i, v := range ns {
		fmt.Println(i, v)
	}

	var ns1 = [5]int{1, 2, 3, 4, 5}
	for i, v := range ns1 {
		fmt.Println(i, v)
	}
	fmt.Println(ns1[1:3])

	title("map")
	var m map[string]int

	m = make(map[string]int)
	m["one"] = 1
	m["two"] = 2
	m["three"] = 3
	fmt.Println(m)

	title("struct")
	p := struct {
		name string
		age  int
	}{
		name: "hello mr. monkey",
		age:  10,
	}
	p.age += 1
	fmt.Println(p, p.name, p.age)

	title("slice")
	ns2 := [...]int{10, 20, 30, 40, 50}
	fmt.Println(ns2[1:4])

	title("slice, array")
	/*
	   make([]int, 3, 10)

	   var array[10]int
	   array[0:3]
	*/
	ns3 := make([]int, 3, 10)
	fmt.Println(ns3)

	ms := []int{1, 2, 3, 4, 5}
	fmt.Println(ms, len(ms), cap(ms))

	ms = append(ms, 10)
	ms = append(ms, 20)
	fmt.Println(ms, len(ms), cap(ms))
}
