package main

import "fmt"

func main() {
	var tbl [201][8]int
	a := [8]int{1, 2, 5, 10, 20, 50, 100, 200}

	for i := 0; i < 201; i++ {
		for j := 0; j < 8; j++ {
			if i == 0 || j == 0 {
				tbl[i][j] = 1
			} else if i-a[j] < 0 {
				tbl[i][j] = tbl[i][j-1]
			} else {
				tbl[i][j] = tbl[i][j-1] + tbl[i-a[j]][j]
			}
		}
	}
	fmt.Println(tbl[200][7])
	// output: 73682
}
