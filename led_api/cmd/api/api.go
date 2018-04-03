package main

import (
	"encoding/json"
	"log"
	"net/http"

	"led_api/internal/pkg/communication"
	"led_api/internal/pkg/filemanager"

	"github.com/gorilla/mux"
)

// our main function
func main() {
	router := mux.NewRouter()
	router.HandleFunc("/new-config", newConfig).Methods("POST")
	log.Fatal(http.ListenAndServe(":20001", router))
}

func newConfig(w http.ResponseWriter, r *http.Request) {
	var returnString string
	ledconfig, err := filemanager.NewLedConfig(r.Body)
	if err == nil {
		if err = ledconfig.SaveConfig(); err == nil {
			returnString = "Saved: " + ledconfig.Location
		} else {
			returnString = "ERROR (Saving config 'api.test'): " + err.Error()
		}
	} else {
		returnString = "ERROR (Making ledconfig 'api.test'): " + err.Error()
	}
	json.NewEncoder(w).Encode(returnString)
	defer communication.SendNewConfig(*ledconfig)
}
