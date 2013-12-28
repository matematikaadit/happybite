package main

import (
	"fmt"
	"math/big"
)

func main() {
	result := factorial(100)
	total := 0
	for _, v := range result.String() {
		n := int(v - '0')
		total += n
	}
	fmt.Println(total)
	// output: 648
}

func factorial(n int64) *big.Int {
	product := big.NewInt(1)
	for i := int64(1); i <= n; i++ {
		product.Mul(product, big.NewInt(i))
	}
	return product
}
