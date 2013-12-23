package main

import "fmt"
import "./lib/primes"

const MAX = 2000000

var primeList = primes.List(MAX)

func main() {
	var sum int64 = 0
	for _, v := range primeList {
		sum += int64(v)
	}
	fmt.Println(sum)
	// output: 142913828922
}
