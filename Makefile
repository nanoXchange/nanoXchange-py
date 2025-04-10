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
	black .
	ruff check . --fix
	pytest test
	./test/server/integration/run_server_tests.sh

freeze:
	$(PIP) freeze --exclude-editable > requirements.txt

clean:
	rm -rf __pycache__ .venv *.pyc *.log