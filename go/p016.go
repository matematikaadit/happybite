package main

import "fmt"
import "math/big"

func main() {
	a := big.NewInt(2)
	b := big.NewInt(1000)
	c := new(big.Int)
	c.Exp(a, b, nil)
	sum := 0
	for _, v := range c.String() {
		n := int(v - '0')
		sum += n
	}
	fmt.Println(sum)
	// output: 1366
}
