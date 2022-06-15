test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -s -p no:cacheprovider -o markers=task

watch:
	find ./ | entr -c make test

lint:
	pylint *.py
