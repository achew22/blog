package generate

import (
	"os"
	"path/filepath"
)

// Generate the blog in the specified output directory.
func Generate(path string) error {
	if err := os.MkdirAll(path, 0o755); err != nil {
		return err
	}

	if err := os.WriteFile(filepath.Join(path, "index.html"), []byte("Hello world!"), 0o644); err != nil {
		return err
	}

	return nil
}
