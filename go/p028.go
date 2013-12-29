package main

import "fmt"

func main() {
	s := 1
	for i := 3; i <= 1001; i += 2 {
		s += 4*i*i - 6*(i-1)
	}
	fmt.Println(s)
	// output: 669171001
}
