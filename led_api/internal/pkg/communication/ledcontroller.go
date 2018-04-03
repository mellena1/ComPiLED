package communication

import (
	"bytes"
	"encoding/json"
	"led_api/internal/pkg/filemanager"
	"net/http"
)

// SendNewConfig ... Send a config to led_controller
func SendNewConfig(ledconfig filemanager.LedConfig) error {
	b := new(bytes.Buffer)
	json.NewEncoder(b).Encode(ledconfig)
	res, err := http.Post("http://led_controller:20002/set-config", "application/json", b)
	if err == nil {
		defer res.Body.Close()
	}
	return err
}
