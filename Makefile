PYTHON := .venv/bin/python
PIP := .venv/bin/pip
.PHONY: test

setup:
	python -m venv .venv
	. .venv/bin/activate && $(PIP) install -r requirements.txt

run:
	. .venv/bin/activate && $(PYTHON) src/main.py

test:
	. .venv/bin/activate && PYTHONPATH=. pytest test/
	black src/ test/ 
	ruff check src/ test/

freeze:
	. .venv/bin/activate && $(PIP) freeze --exclude-editable > requirements.txt

clean:
	rm -rf __pycache__ .venv *.pyc *.log