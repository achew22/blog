package main

import (
	"flag"
	"fmt"
	"io"
)

var missingMandatoryArgErr = fmt.Errorf("missing argument")

func parseArgs(args []string, output io.Writer) (*options, error) {
	flags := flag.NewFlagSet("blog", flag.ContinueOnError)
	flags.SetOutput(output)

	var result options
	flags.StringVar(&result.OutputPath, "output_path", "", "The path to generate into")

	if err := flags.Parse(args); err != nil {
		return nil, err
	}

	if result.OutputPath == "" {
		return nil, fmt.Errorf("missing --output_path argument: %w", missingMandatoryArgErr)
	}

	return &result, nil
}
