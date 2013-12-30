package main

import (
	"fmt"
	"math"
)

func main() {
	sum := 0
	MAX := int(math.Pow(9, 5)) * 6
	for i := 10; i < MAX; i++ {
		if fpd(i) {
			sum += i
		}
	}
	fmt.Println(sum)
	// output: 443839
}

func fpd(n int) bool {
	orign := n
	product := 0
	for n > 0 {
		product += int(math.Pow(float64(n%10), 5))
		n /= 10
	}
	return orign == product
}
