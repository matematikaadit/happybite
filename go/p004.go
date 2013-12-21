package main

import "fmt"

func reverse(num int) (ret int) {
	ret = 0
	for num > 0 {
		ret = ret*10 + num%10
		num /= 10
	}
	return
}

func palindrome(num int) bool {
	return num == reverse(num)
}

func main() {
	last := 0
	for x := 900; x < 1000; x++ {
		for y := 900; y < 1000; y++ {
			n := x * y
			if n > last && palindrome(n) {
				last = n
			}
		}
	}
	fmt.Println(last)
	// output: 906609
}
