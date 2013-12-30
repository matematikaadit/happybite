package main

import "fmt"

func main() {
	sum := 0
	for i := 10; i < 7*fact(9); i++ {
		if factsum(i) == i {
			sum += i
		}
	}
	fmt.Println(sum)
	// output: 40730
}

func fact(n int) int {
	if n < 2 {
		return 1
	}
	return n * fact(n-1)
}

func factsum(n int) int {
	sum := 0
	for n > 0 {
		sum += fact(n % 10)
		n /= 10
	}
	return sum
}
