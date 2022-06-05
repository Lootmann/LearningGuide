run:
	python3.10 main.py

.PHONY: in
in:
	python3.10 main.py < 1
	python3.10 main.py < 2
	python3.10 main.py < 3

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -v

.PHONY: watch
watch:
	find ./ | entr -s python3.10 main.py
