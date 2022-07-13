run:
	python3.10 main.py

.PHONY: in
in:
	python3.10 main.py < in

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -v

.PHONY: watch
watch:
	find ./ | entr -s python3.10 main.py
