package main

import "fmt"

func main() {
	var (
		n    int64 = 600851475143
		k    int64 = 2
		last int64 = k
	)
	for n > 1 {
		if n%k == 0 {
			last = k
			for n%k == 0 {
				n /= k
			}
		}
		k += 1
	}
	fmt.Println(last)
	// output: 6
}
