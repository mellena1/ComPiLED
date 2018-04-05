package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// our main function
func main() {
	router := mux.NewRouter()
	router.HandleFunc("/test", test).Methods("GET")
	log.Fatal(http.ListenAndServe(":20001", router))
}

func test(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode("testing, testing, 1.2.3")
}
