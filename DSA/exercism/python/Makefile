test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider -o markers=task ${test-pytest-filename.py}

watch:
	find ./ | entr -c make test
