package main

import (
	"strconv"
	"strings"
	"fmt"
	"bufio"
	"os"
)

func strtoint(line string) []int {
	cells := strings.Split(line, " ")
	result := make([]int, len(cells))
	for i, v := range cells {
		result[i], _ = strconv.Atoi(v)
	}
	return result
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	f, _ := os.Open("../sources/p018.txt")
	scanner := bufio.NewScanner(f)

	puff := make([][]int, 0, 15)
	for scanner.Scan() {
		puff = append(puff, strtoint(scanner.Text()))
	}

	for i := len(puff) - 2; i >= 0; i-- {
		for j := 0; j < len(puff[i]); j++ {
			puff[i][j] += max(puff[i+1][j], puff[i+1][j+1])
		}
	}
	fmt.Println(puff[0][0])
	// output: 1074
}
