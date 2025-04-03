.PHONY: setup run test freeze clean

PYTHON := .venv/bin/python
PIP := .venv/bin/pip

setup:
	python -m venv .venv
	. .venv/bin/activate && $(PIP) install -r requirements.txt
	. .venv/bin/activate && $(PIP) install -e .

run:
	$(PYTHON) src/main.py

test:
	pytest test

freeze:
	$(PIP) freeze --exclude-editable > requirements.txt

clean:
	rm -rf __pycache__ .venv *.pyc *.log