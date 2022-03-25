package main

import (
	"math/rand"
	"strconv"
	"time"
)

type Score struct {
	UserID string
	GameID int
	Point  int
}

func GetRandomNumber(low int, max int) int {
	return rand.Intn(max-low) + low
}

func GetUserId() string {
	return strconv.Itoa(GetRandomNumber(1, 10000))
}

func init() {
	// rand
	t := time.Now().UnixNano()
	rand.Seed(t)
}

func main() {
	scores := []Score{}
	for i := 0; i < 100; i++ {
		score := Score{
			UserID: GetUserId(),
			GameID: i,
			Point:  GetRandomNumber(1, 100),
		}
		scores = append(scores, score)
	}
}
