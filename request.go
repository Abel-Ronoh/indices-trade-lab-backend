package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

var APIURL = "https://api.example.com/forex" // Replace with your API URL

type ForexData struct {
	Pair      string  `json:"pair"`
	Price     float64 `json:"price"`
	Timestamp int64   `json:"timestamp"`
}

func getForexData(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	currencyPair := params["pair"]

	apiURL := fmt.Sprintf("%s/%s", APIURL, currencyPair)
	response, err := http.Get(apiURL)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer response.Body.Close()

	var data ForexData
	if err := json.NewDecoder(response.Body).Decode(&data); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/get_forex_data/{pair}", getForexData).Methods("GET")

	http.Handle("/", r)
	http.ListenAndServe(":8080", nil)
}
