package main

import "fmt"

func prime(a int) bool {
	if a < 2 {
		return false
	}
	for i := 2; i*i <= a; i++ {
		if a%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	count := 0
	for i := 1; ; i++ {
		if prime(i) {
			count += 1
		}
		if count == 10001 {
			fmt.Println(i)
			// output: 104743
			break
		}
	}
}
