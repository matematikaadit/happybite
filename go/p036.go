package main

import "fmt"

func main() {
	sum := 0
	for i := 1; i < 1000000; i += 2 {
		if dbp(i) {
			sum += i
		}
	}
	fmt.Println(sum)
	// output: 872187
}

func dbp(i int) bool {
	base2 := fmt.Sprintf("%b", i)
	base10 := fmt.Sprintf("%d", i)
	return base2 == reverse(base2) && base10 == reverse(base10)
}

func reverse(s string) string {
	n := len(s)
	runes := make([]rune, n)
	for _, rune := range s {
		n--
		runes[n] = rune
	}
	return string(runes[n:])
}
