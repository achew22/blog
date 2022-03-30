package main

import (
	"flag"
	"io"
)

func parseArgs(args []string, output io.Writer) (*options, error) {
	flags := flag.NewFlagSet("blog", flag.ContinueOnError)
	flags.SetOutput(output)

	var result options
	flags.StringVar(&result.OutputPath, "output_path", "", "The path to generate into")

	if err := flags.Parse(args); err != nil {
		return nil, err
	}

	return &result, nil
}
