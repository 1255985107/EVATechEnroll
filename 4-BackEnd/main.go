package main

import (
	"monitor/server"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/ping", server.Ping)
	r.POST("/check", server.Check)
	r.POST("/status", server.Status)

	r.Run(":8080")
}
