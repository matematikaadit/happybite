package main

import "fmt"

func main() {
	a := 1
	b := 1
	total := 0
	MAX := 4000000

	for a < MAX {
		if a%2 == 0 {
			total += a
		}
		a, b = b, a+b
	}
	fmt.Println(total)
	// output: 4613732
}
