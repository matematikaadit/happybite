package main

import "fmt"

var collmap = make(map[int64]int64)

func collatz(n int64) (count int64) {
	v, ok := collmap[n]
	if ok {
		return v
	}
	if n < 3 {
		collmap[n] = n
		return n
	}
	count = 1
	switch n % 2 {
	case 0:
		count = 1 + collatz(n/2)
	case 1:
		count = 1 + collatz(3*n+1)
	}
	collmap[n] = count
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
