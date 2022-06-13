test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider -o markers=task

watch:
	find ./ | entr -c make test

lint:
	pylint ./sets.py
