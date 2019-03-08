package server

import (
	"io"
	"net/http"

	"github.com/gorilla/handlers"
	"github.com/gorilla/mux"
	"github.com/mellena1/ComPiLED/pkg/backend"
)

// Server ties everything together that the server uses
type Server struct {
	Backend   backend.Backend
	LogWriter io.Writer
	Router    *mux.Router
}

// NewServer returns a new server given a backend
func NewServer(backend backend.Backend, logwriter io.Writer) *Server {
	return &Server{
		Backend:   backend,
		LogWriter: logwriter,
		Router:    mux.NewRouter(),
	}
}

// ListenAndServe starts the server
func (s *Server) ListenAndServe(addr string) error {
	var handler http.Handler = s.Router
	if s.LogWriter != nil {
		handler = handlers.LoggingHandler(s.LogWriter, s.Router)
	}
	return http.ListenAndServe(addr, handler)
}

// Close closes anything that the server has open
func (s *Server) Close() error {
	return s.Backend.Close()
}
