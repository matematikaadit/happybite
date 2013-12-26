package main

import "fmt"

var s = map[int]string{
	0:  "",
	1:  "one",
	2:  "two",
	3:  "three",
	4:  "four",
	5:  "five",
	6:  "six",
	7:  "seven",
	8:  "eight",
	9:  "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
}

func main() {
	sum := 0
	for i := 1; i < 1000; i++ {
		_, ok := s[i]
		if !ok {
			if i < 100 {
				s[i] = s[(i/10)*10] + s[i%10]
			} else {
				s[i] = s[i/100] + "hundred"
				if i%100 != 0 {
					s[i] += "and" + s[i%100]
				}
			}
		}
		v, _ := s[i]
		sum += len(v)
	}
	s[1000] = "onethousand"
	sum += len(s[1000])
	fmt.Println(sum)
	// output: 21124
}
