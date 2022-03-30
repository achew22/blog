package main

import (
	"flag"
	"fmt"
	"os"
)

type options struct {
	// OutputPath to generate at.
	OutputPath string
}

func Run(argv []string) error {
	opts, err := parseArgs(argv, os.Stderr)
	if err != nil {
		return err
	}

	fmt.Printf("Finished generating to %q successfully\n", opts.OutputPath)
	return nil
}

func main() {
	if err := Run(os.Args[1:]); err == flag.ErrHelp {
		// If ErrHelp was returned it printed usage and wants to exit.
		os.Exit(1)
	} else if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v", err)
		os.Exit(1)
	}
}
