package backend

// Backend describes everything that a backend needs to implement
type Backend interface {
	Close() error
}
