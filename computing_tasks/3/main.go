package main

import (
	"fmt"
	"strings"
)

func main() {
	for i := 1; i <= 5; i++ {
		fmt.Println(strings.Repeat("0", i))
	}
}
