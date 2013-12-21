package main

import "fmt"

const MAX = 2000000

var primes [MAX]int

func sieve() {
	primes[0] = 1
	primes[1] = 1
	for i := 2; i*i <= MAX; i++ {
		if primes[i] == 0 {
			k := i
			for j := k * k; j < MAX; j += k {
				primes[j] = 1
			}
		}
	}
}

func main() {
	sieve()
	var sum int64 = 0
	for i := 0; i < MAX; i++ {
		if primes[i] == 0 {
			sum += int64(i)
		}
	}
	fmt.Println(sum)
	// output: 142913828922
}
