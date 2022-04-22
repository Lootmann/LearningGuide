run:
	go run main.go

.PHONY: test
test:
	go test -v

.PHONY: watch
watch:
	find . | entr -c go run main.go
