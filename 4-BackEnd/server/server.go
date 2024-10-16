package server

import (
	"io"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

var hitokoto string = "https://v1.hitokoto.cn?c=c&encode=text&charset=utf-8"
var lastCheckTime = map[string]time.Time{
	"ZJUEVA204": time.Now(),
}

func Ping(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"msg": "pong",
	})
}

func Check(c *gin.Context) {
	var req struct {
		Source string `json:"source"`
	}
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"code": 101,
			"msg":  "Should have a server name",
			"data": gin.H{},
		})
		return
	}

	if _, exists := lastCheckTime[req.Source]; !exists {
		c.JSON(http.StatusBadRequest, gin.H{
			"code": 100,
			"msg":  "Server not authorized",
			"data": gin.H{"isChecked": false},
		})
		return
	}

	lastCheckTime[req.Source] = time.Now()
	c.JSON(http.StatusOK, gin.H{
		"isChecked": true,
	})
}

func Status(c *gin.Context) {
	var req struct {
		Server string `json:"server"`
	}

	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"code": 101,
			"msg":  "Should have a server name",
			"data": gin.H{},
		})
		return
	}

	lastTime, exists := lastCheckTime[req.Server]
	resp, err := http.Get(hitokoto)
	var sentence string
	if err != nil || resp.StatusCode != http.StatusOK {
		sentence = "Failed to fetch data from hitokoto."
	} else {
		body, _ := io.ReadAll(resp.Body)
		sentence = string(body)
	}
	if !exists {
		c.JSON(http.StatusOK, gin.H{
			"lastTime":       "Never",
			"isDisconnected": true,
			"hitokoto":       sentence,
		})
		return
	} else {
		isDisconnected := time.Since(lastTime) > 5*time.Minute
		c.JSON(http.StatusOK, gin.H{
			"lastTime":       lastTime.Format("2006-01-02 15:04:05"),
			"isDisconnected": isDisconnected,
			"hitokoto":       sentence,
		})
	}
}
