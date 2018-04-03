package filemanager

import (
	"io"
	"os"
	"strings"

	"encoding/json"
)

var configsDir = "/configs/"

type invalidLedJSONError struct {
	What string
}

func (e *invalidLedJSONError) Error() string {
	return e.What
}

// LedConfig ... Holds the data for an LED Config
type LedConfig struct {
	Name       string
	Location   string `json:"-"`
	Brightness int
	LEDs       []map[string]interface{}
}

// NewLedConfig ... Constructor for the ledConfig struct
func NewLedConfig(configJSONReader io.Reader) (*LedConfig, error) {
	dec := json.NewDecoder(configJSONReader)

	var ledConfig LedConfig
	for dec.More() {
		err := dec.Decode(&ledConfig)
		if err != nil {
			return nil, err
		}
	}
	ledConfig.Location = configsDir + ledConfig.Name + ".json"
	return &ledConfig, nil
}

// SaveConfig ... Saves a LedConfig struct to a file
func (config LedConfig) SaveConfig() error {
	fo, err := os.Create(config.Location)
	if err != nil {
		return err
	}
	enc := json.NewEncoder(fo)
	enc.SetIndent("", strings.Repeat(" ", 4))
	err = enc.Encode(&config)
	if err != nil {
		return err
	}
	fo.Close()
	return nil
}

func (config *LedConfig) validateJSON() error {
	return nil
}
