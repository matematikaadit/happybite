package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	for a := 1; a < 500; a++ {
		low := max(a, 500-a)
		for b := low; b < 500; b++ {
			c := 1000 - a - b
			if a*a+b*b == c*c {
				fmt.Println(a * b * c)
				// output: 31875000
			}
		}
	}
}
