PORT=8888
run:
	PYTHONDONTWRITEBYTECODE=1 uvicorn main:app --reload --port $(PORT)

.PHONY: test
test:
	curl http://127.0.0.1:$(PORT)
