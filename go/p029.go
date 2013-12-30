package main

import (
	"fmt"
	"math/big"
)

func main() {
	set := make(map[string]bool)
	for i := 2; i <= 100; i++ {
		for j := 2; j <= 100; j++ {
			a := big.NewInt(int64(i))
			b := big.NewInt(int64(j))
			c := new(big.Int)
			c.Exp(a, b, nil)
			set[c.String()] = true
		}
	}
	fmt.Println(len(set))
	// output: 9183
}
