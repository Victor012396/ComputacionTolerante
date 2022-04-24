package main
import net/http
import fmt

import(
	"fmt"
	"net/http"
)

func homePage(w http.ResponseWritter, r *http.Request){
	fmt.Fprint(w,"My Awesome Go App")
}

func setupRoutes(){
	http.HandleFunc("/", homePage)
}

func main(){
	fmt.Println("Go Web App Started on Port 3000")
	setupRoutes()
	http.ListenAndServe(":3000",nil)
}
