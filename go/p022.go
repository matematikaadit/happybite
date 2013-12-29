package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

func main() {
	source, err := ioutil.ReadFile("../sources/names.txt")
	check(err)
	s := string(source)
	s = strings.Replace(s, "\"", "", -1)
	names := strings.Split(s, ",")
	sort.Strings(names)
	total := 0
	for i, name := range names {
		total += sum(name) * (i + 1)
	}
	fmt.Println(total)
	// output: 871198282
}

func sum(s string) int {
	total := 0
	for _, v := range s {
		i := int(v - 'A' + 1)
		total += i
	}
	return total
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
