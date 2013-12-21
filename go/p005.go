package main

import "fmt"

func lcd(a, b int64) int64 {
	return a * b / gcd(a, b)
}

func gcd(a, b int64) int64 {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}
func main() {
	var result int64 = 1
	for i := int64(1); i <= 20; i++ {
		result = lcd(result, i)
	}
	fmt.Println(result)
	// output:
}
