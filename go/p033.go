package main

import "fmt"

func main() {
	product := rat{1, 1}
	for a := 1; a < 10; a++ {
		for b := 1; b < 10; b++ {
			for c := 1; c < 10; c++ {
				if a == b {
					continue
				}
				lhs1 := rat{10*a + c, 10*c + b}
				lhs2 := rat{10*c + a, 10*b + c}
				rhs := rat{a, b}
				if lhs1.n < lhs1.d && equal(lhs1, rhs) {
					product = mul(product, rhs)
				}
				if lhs2.n < lhs2.d && equal(lhs2, rhs) {
					product = mul(product, rhs)
				}
			}
		}
	}
	fmt.Println(product)
	// output: {1 100}
}

type rat struct {
	n, d int
}

func mul(a, b rat) rat {
	num := a.n * b.n
	den := a.d * b.d
	d := gcd(num, den)
	return rat{num / d, den / d}
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func equal(a, b rat) bool {
	da := gcd(a.n, a.d)
	db := gcd(b.n, b.d)
	return a.n/da == b.n/db && a.d/da == b.d/db
}
