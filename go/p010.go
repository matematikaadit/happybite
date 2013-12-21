package main

import "fmt"

const MAX = 2000000

var primes [MAX]bool

func sieve() {
	primes[0] = true
	primes[1] = true
	for i := 2; i*i <= MAX; i++ {
		if !primes[i] {
			for j := i * i; j < MAX; j += i {
				primes[j] = true
			}
		}
	}
}

func main() {
	sieve()
	var sum int64 = 0
	for i := 0; i < MAX; i++ {
		if !primes[i] {
			sum += int64(i)
		}
	}
	fmt.Println(sum)
	// output: 142913828922
}
