# Create virtual environment
venv:
	source myvenv/bin/activate

# Run unit tests
test_gmail_client:
	python -m unittest tests.test_gmail_client

run:
	python main.py

	