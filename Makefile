PYTHON=python3

# Create virtual environment
venv:
	$(PYTHON) -m venv venv && source venv/bin/activate

# Install dependencies
install:
	pip install -r requirements.txt

lint:
	python -m pylint --disable=W,C,R scripts/ tests/
# W = warnings
# C = convention
# R = refactor

# Run unit tests
test:
	python -m unittest discover -s tests

run:
	python main.py

	