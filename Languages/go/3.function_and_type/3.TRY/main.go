package main

import "fmt"

func sum1(arr []int) int {
	var sum int
	for i := 0; i < len(arr); i++ {
		sum += arr[i]
	}
	return sum
}

func sum2(arr []int) int {
	var sum int
	for _, v := range arr {
		sum += v
	}
	return sum
}

func main() {
	n := []int{19, 86, 1, 12}

	fmt.Println("for -> ", sum1(n))
	fmt.Println("range -> ", sum2(n))
}
