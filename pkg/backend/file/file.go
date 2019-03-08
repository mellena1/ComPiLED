package file

// Backend implements backend.Backend by saving to the filesystem
type Backend struct {
	Folder string
}

// Close closes all files
func (b Backend) Close() error {
	return nil
}
