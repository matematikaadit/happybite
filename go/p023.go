package main

import "fmt"

const MAX = 28124

func main() {
	div := make([]int, MAX)
	initialize(div)

	abd := abdGet(div)
	abdsum := abdSumGet(abd)

	sum := 0
	for i := 0; i < MAX; i++ {
		if !abdsum[i] {
			sum += i
		}
	}
	fmt.Println(sum)
	// output: 4179871
}

func initialize(div []int) {
	for i := 1; i < MAX; i++ {
		for j := 2 * i; j < MAX; j += i {
			div[j] += i
		}
	}
}

func abdGet(div []int) []int {
	result := make([]int, 0)
	for i := 0; i < MAX; i++ {
		if div[i] > i {
			result = append(result, i)
		}
	}
	return result
}

func abdSumGet(abd []int) []bool {
	result := make([]bool, MAX)
	for i := 0; i < len(abd); i++ {
		for j := 0; j <= i; j++ {
			index := abd[i] + abd[j]
			if index < MAX {
				result[index] = true
			}
		}
	}
	return result
}
