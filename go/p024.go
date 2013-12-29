package main

import "fmt"

func main() {
	x := 999999 // since it's the millionth
	q := 0
	answer := ""
	set := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	for i := 9; i >= 0; i-- {
		q = x / factorial(i)
		x = x % factorial(i)
		answer += fmt.Sprintf("%d", set[q])
		set = del(set, q)
	}
	fmt.Println(answer)
	// output: 2783915460
}

func factorial(i int) int {
	if i < 2 {
		return 1
	}
	return i * factorial(i-1)
}

func del(s []int, i int) []int {
	return append(s[:i], s[i+1:]...)
}
