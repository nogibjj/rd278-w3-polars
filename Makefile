# Makefile for Python Project requested a basic, readable makefile from chatGPT to understand how these funciton

# Variables
PYTHON := python3
VENV := ~\.venv
SRC_DIR := pythonproject/src
TEST_DIR := pythonproject/tests
REQUIREMENTS := requirements.txt

# Default target
all: venv source install test format lint

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
source:
	$(VENV)/bin/activate

# Install project dependencies
install:
	$(VENV)/bin/pip install --upgrade pip -r  $(REQUIREMENTS)

# Run unit tests
test:
	$(VENV)/bin/pytest $(TEST_DIR)

# Format code with Black
format:
	$(VENV)/bin/black $(SRC_DIR)

# Lint code with Flake8
lint:
	$(VENV)/bin/pylint $(SRC_DIR)

# Clean up generated files and virtual environment
clean:
	rm -rf $(VENV) __pycache__ .pytest_cache
