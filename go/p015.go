package main

import "fmt"

func main() {
	var path [21][21]int64
	for i := 0; i < 21; i++ {
		for j := 0; j < 21; j++ {
			if i == 0 || j == 0 {
				path[i][j] = 1
			} else {
				path[i][j] = path[i-1][j] + path[i][j-1]
			}
		}
	}
	fmt.Println(path[20][20])
	// output: 137846528820
}
