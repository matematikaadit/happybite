package main

import "fmt"

func main() {
	a := 0
	b := 0
	for i := 1; i <= 100; i++ {
		a += i
		b += i * i
	}
	fmt.Println(a*a - b)
	// output: 25164150
}
