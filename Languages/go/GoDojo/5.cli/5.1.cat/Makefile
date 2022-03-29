run:
	go run main.go -n fuga.txt hoge.txt

.PHONY: n
n:
	go run main.go -n fuga.txt hoge.txt

.PHONY: no-n
no-n:
	go run main.go fuga.txt hoge.txt

.PHONY: watch
watch:
	find . | entr -c go run main.go
