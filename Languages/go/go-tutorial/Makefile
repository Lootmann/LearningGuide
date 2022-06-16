run:
	go run main.go

.PHONY: test
test:
	go test -v

.PHONY: bench
bench:
	go test -bench=.

.PHONY: watch
watch:
	find . | entr -c go run main.go
