run:
	python3.10 main.py < in

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -v

.PHONY: watch
watch:
	find ./ | entr -c python3.10 main.py
