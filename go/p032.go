package main

import "fmt"

func main() {
	set := make(map[int]bool)
	for i := 1; i < 10; i++ {
		for j := 1000; j < 10000; j++ {
			k := i * j
			if pandigital(i, j, k) {
				set[k] = true
			}
		}
	}
	for i := 10; i < 100; i++ {
		for j := 100; j < 1000; j++ {
			k := i * j
			if pandigital(i, j, k) {
				set[k] = true
			}
		}
	}
	sum := 0
	for k, _ := range set {
		sum += k
	}
	fmt.Println(sum)
	// output: 45228
}

func pandigital(a, b, c int) bool {
	s := fmt.Sprintf("%d%d%d", a, b, c)
	if len(s) != 9 {
		return false
	}
	digit := make([]int, 10)
	for _, v := range s {
		digit[v-'0'] += 1
	}
	for i := 1; i < 10; i++ {
		if digit[i] != 1 {
			return false
		}
	}
	return true
}
