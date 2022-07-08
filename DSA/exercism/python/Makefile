.PHONY: all test

all:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider -o markers=task -sv

test: all

watch:
	find ./ | entr -c make test

lint:
	pylint *.py
