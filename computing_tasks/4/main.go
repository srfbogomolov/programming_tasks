package main

import "fmt"

func main() {
	for x := 0; x < 5; x++ {
		for y := 0; y < 8; y++ {
			fmt.Print("A")
		}
		fmt.Println()
	}
}
