run:
	python3.10 main.py

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -v

.PHONY: in
in:
	python3.10 main.py < in

.PHONY: watch
watch:
	find ./ | entr -s python3.10 main.py
