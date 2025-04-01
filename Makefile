PYTHON=python3

# Create virtual environment
venv:
	$(PYTHON) -m venv venv && source venv/bin/activate

# Install dependencies
install:
	pip install -r requirements.txt

lint:
	python -m pylint --disable=W,C,R scripts/
# W = warnings
# C = convention
# R = refactor

run:
	python main.py

	