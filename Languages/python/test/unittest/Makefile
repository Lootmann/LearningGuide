test:
	python test.py

.PHONY: watch
watch:
	find ./ | entr -c python3 -m unittest -v test.py
