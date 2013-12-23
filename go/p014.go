package main

import "fmt"

// TODO: buat collatz lebih efisien

func collatz(n int64) (count int64) {
	count = 1
	for n > 1 {
		if n%2 == 0 {
			n = n / 2
		} else {
			n = 3*n + 1
		}
		count++

	}
	return count
}
func main() {
	var a, na int64 = 1, 1
	for i := int64(1); i < 1000000; i++ {
		ni := collatz(i)
		if na <= ni {
			a, na = i, ni
		}
	}
	fmt.Println(a, na)
	// output: 837799 525
}
