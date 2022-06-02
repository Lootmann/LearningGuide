run:
	python3.10 ./stack.py

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -v -s

.PHONY: watch
watch:
	find ./ | entr -s python3.10 ./stack.py
