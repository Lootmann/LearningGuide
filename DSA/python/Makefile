.PHONY: test
test:
	python3.10 -m pytest -vv -s

.PHONY: cov
cov:
	python3.10 -m pytest --cov

.PHONY: report
report:
	python3.10 -m pytest --cov-report html --cov=src tests/
