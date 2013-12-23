package main

import "fmt"
import "./lib/primes"

var a = primes.List(65536)

func divisor(n int) int {
	m := n
	result := 1
	for i, k := 0, a[0]; k*k <= n && m != 1; i++ {
		k := a[i]
		if m%k == 0 {
			p := 1
			for m%k == 0 {
				p++
				m /= k
			}
			result *= p
		}
	}
	if m != 1 {
		result *= 2
	}
	return result
}

func tri(n int) int {
	return (n + 1) * n / 2
}

func main() {
	for i := 1; ; i++ {
		n := tri(i)
		if divisor(n) >= 500 {
			fmt.Println(n)
			break
		}
	}
}
