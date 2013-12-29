package main

import (
	"fmt"
	"math/big"
)

func main() {
	a := big.NewInt(1)
	b := big.NewInt(1)
	i := 1
	for len(a.String()) < 1000 {
		c := new(big.Int)
		c.Add(a, b)
		a = b
		b = c
		i++
	}
	fmt.Println(i)
	// output: 4782
}
