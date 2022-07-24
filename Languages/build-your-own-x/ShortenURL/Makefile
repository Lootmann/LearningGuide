run:
	python3.10 src/main.py

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 pytest -sv

.PHONY: watch
watch:
	find ./ | entr -c python3.10 main.py
