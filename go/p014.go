package main

import "fmt"

var collslice [1000000]int

func collatz(n int64) int {
	orin := n
	count := 0

	for n >= orin {
		switch n & 1 {
		case 0:
			count++
			n = n >> 1
		case 1:
			count++
			n = n<<1 + n + 1
		}
	}
	collslice[orin] = count + collslice[n]
	return collslice[orin]
}

func main() {
	var a int64 = 1
	var na int = 1
	collslice[1] = 1
	for i := int64(2); i < 1000000; i++ {
		ni := collatz(i)
		if na <= ni {
			a, na = i, ni
		}
	}
	fmt.Println(a, na)
	// output: 837799 525
}
