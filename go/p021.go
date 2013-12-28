package main

import "fmt"

const MAX int = 10001

var d [MAX]int

func main() {
	initialize()
	total := 0
	for n := 1; n < MAX; n++ {
		if d[n] < MAX && d[n] != n && d[d[n]] == n {
			total += n
		}
	}
	fmt.Println(total)
	// output: 31626
}

func initialize() {
	for n := 1; n < MAX; n++ {
		for k := 2 * n; k < MAX; k += n {
			d[k] += n
		}
	}
}
