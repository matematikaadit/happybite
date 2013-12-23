package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	sum := new(big.Int)
	n := new(big.Int)
	f, _ := os.Open("../sources/p013.txt")
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		n.SetString(scanner.Text(), 0)
		sum.Add(sum, n)
	}
	fmt.Println(sum.String()[:10])
	// output: 5537376230
}
