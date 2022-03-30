package main

import (
	"strings"
	"testing"

	"github.com/google/go-cmp/cmp"
)

func TestParseArgs(t *testing.T) {
	tests := []struct {
		in   []string
		want *options
		err  bool
	}{
		{[]string{"--fake_flag"}, nil, true},
		{[]string{}, &options{}, false},
		{[]string{"--output_path=asdf"}, &options{OutputPath: "asdf"}, false},
	}

	for _, test := range tests {
		t.Run(strings.Join(test.in, " "), func(t *testing.T) {
			var buf strings.Builder
			got, err := parseArgs(test.in, &buf)
			if test.err {
				if err == nil {
					t.Fatalf("Expected an error but didn't get one\n\nOutput: %s", buf.String())
				}
			} else {
				if err != nil {
					t.Fatalf("Expected no error but got: %v\n\nOutput: %s", err, buf.String())
				}
			}

			if diff := cmp.Diff(test.want, got); diff != "" {
				t.Errorf("Diff (-want,+got):\n%v", diff)
			}
		})
	}
}
