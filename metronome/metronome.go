package main

import "fmt"

func main() {
	fmt.Println("Why hello Mr Fletcher.")
	grid := make([]uint16, 32)
	for i := 0; i < 32; i++ {
		if i%8 == 0 {
			grid[i] = 2
		}
		if i%8 == 0 {
			grid[i] = 1
		}
	}
	fmt.Printf("Metronome Configuratio: %d \n", grid)
}
