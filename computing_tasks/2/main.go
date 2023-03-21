package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()

	fmt.Println(t.Weekday().String())
	fmt.Println(t.Month().String())
	fmt.Println("Serafim")
}
