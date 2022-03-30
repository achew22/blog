package main

import (
	"fmt"
	"os"
)

func main() {
	if err := Run(os.Args); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v", err)
		os.Exit(1)
	}
}

func Run(args []string) error {
	return nil
}
