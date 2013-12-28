package main

import (
	"fmt"
	"time"
)

func main() {
	total := 0
	for year := 1901; year <= 2000; year++ {
		for month := time.January; month <= time.December; month++ {
			date := time.Date(year, month, 1, 0, 0, 0, 0, time.UTC)
			if date.Weekday() == time.Sunday {
				total += 1
			}
		}
	}
	fmt.Println(total)
	// output: 171
}
