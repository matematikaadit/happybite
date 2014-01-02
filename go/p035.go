package main

import (
	"./lib/primes"
	"fmt"
)

const MAX = 1000000

var prime_list = primes.List(MAX)
var prime_state = primes.State(MAX)
var state = make([]bool, MAX)

func main() {
	count := 0
	for _, v := range prime_list {
		if !state[v] {
			count += cycle(v)
		}
	}
	fmt.Println(count)
	// output: 55
}

func cycle(v int) int {
	s := fmt.Sprintf("%d", v)
	if zeroes(s) {
		return 0
	}
	oris := s
	var n int
	cyp := make([]int, 0)
	cyp = append(cyp, v)
	count := 1
	for i := 0; i < len(s)-1; i++ {
		s = fmt.Sprintf("%s%s", s[1:], string(s[0]))
		if s == oris {
			break
		}
		fmt.Sscanf(s, "%d", &n)
		if prime_state[n] { // not prime
			return 0
		}
		count++
		cyp = append(cyp, n)
	}
	for _, p := range cyp {
		state[p] = true
	}
	return count
}

func zeroes(s string) bool {
	for _, v := range s {
		if v == '0' {
			return true
		}
	}
	return false
}
