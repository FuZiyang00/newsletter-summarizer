PYTHON=python3

# Create virtual environment
venv:
	$(PYTHON) -m venv venv && source venv/bin/activate

# Install dependencies
install:
	pip install -r requirements.txt

lint:
	python -m pylint scripts/ tests/

# Run unit tests
test:
	python -m unittest tests.test_gmail_client

run:
	python main.py

	