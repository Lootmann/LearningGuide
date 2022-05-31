run:
	PYTHONDONTWRITEBYTECODE=1 python3.10 main.py

.PHONY: get
get:
	curl http://127.0.0.1:8080

.PHONY: post
post:
	http -f post http://127.0.0.1:8080 hello=world
