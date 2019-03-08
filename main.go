package main

import (
	"log"

	"github.com/mellena1/ComPiLED/pkg/backend/file"
	"github.com/mellena1/ComPiLED/pkg/server"
)

func main() {
	backend := file.Backend{}
	app := server.NewServer(backend, nil)

	log.Println("Listening on port 8080...")
	log.Fatal(app.ListenAndServe(":8080"))
}
