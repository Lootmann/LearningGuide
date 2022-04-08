run:
	python main.py

.PHONY: in
in:
	python main.py < in

.PHONY: watch
watch:
	find ./ | entr -c -s 'python main.py < in'
