package main

import "fmt"

func main() {
	a := 0
	b := 0

	for i := 999; i > 0; i-- {
		if i <= a {
			break
		}

		c := recycle(i)
		if c > a {
			a, b = c, i
		}
	}
	fmt.Println(b)
	// output: 983
}

func recycle(n int) int {
	pos := make([]int, n)
	a := 1
	for i := 1; i <= n; i++ {
		if pos[a] != 0 {
			return i - pos[a]
		}
		if a == 0 {
			return 0
		}
		pos[a] = i
		a = (a * 10) % n
	}
	return 0
}
