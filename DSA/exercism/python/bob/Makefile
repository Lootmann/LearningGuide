test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider -o markers=task

watch:
	find ./ | entr -c make test

lint:
	pylint bob.py

alltest:
	python3.10 -m unittest bob_test.TestBobLetter
	python3.10 -m unittest bob_test.TestCalmDown
	python3.10 -m unittest bob_test.TestSure
	python3.10 -m unittest bob_test.TestChillOut

