run:
	python3.10 main.py

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 python3.10 -m unittest -v

.PHONY: watch
watch:
	find ./ | entr -s python3.10 main.py
