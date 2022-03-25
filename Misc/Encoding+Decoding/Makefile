run:
	python3 -m main.py

.PHONY: test
test:
	python3 -m test -v

.PHONY: watch
watch:
	find ./ | entr python main.py
