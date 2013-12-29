package main

import (
	"./lib/primes"
	"fmt"
)

const MAX = 1000

var prime_list = primes.List(MAX)

func main() {
	ma, mb, mc := 0, 0, 0
	for a := -999; a < 1000; a += 2 {
		for _, b := range prime_list {
			c := longest(a, b)
			if c > mc {
				ma, mb, mc = a, b, c
			}
		}
	}
	fmt.Println(ma*mb, ma, mb, mc)
	// output: -59231 -61 971 71
}

func longest(a, b int) int {
	for x := 0; x < b; x++ {
		f := x*x + a*x + b
		if !primes.Test(f) {
			return x
		}
	}
	return b
}
