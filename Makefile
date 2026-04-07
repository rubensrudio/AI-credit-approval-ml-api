.PHONY: help setup install lint format test run docs docker-build docker-run docker-stop clean

# Variables
PYTHON := python3
PIP := pip3
PORT := 8000
ENV_FILE := .env

help:
	@echo "Credit Approval ML API - Makefile"
	@echo "===================================="
	@echo ""
	@echo "Available commands:"
	@echo "  make setup          - Create .env and install dependencies"
	@echo "  make install        - Install dependencies"
	@echo "  make edit           - Install in editable mode (dev)"
	@echo "  make train-model    - Train ML model"
	@echo "  make lint           - Run linter (flake8, pylint)"
	@echo "  make format         - Format code (black, isort)"
	@echo "  make test           - Run tests"
	@echo "  make test-cov       - Tests with coverage"
	@echo "  make run            - Run API locally"
	@echo "  make docker-build   - Build Docker image"
	@echo "  make docker-run     - Run via Docker Compose"
	@echo "  make docker-stop    - Stop Docker containers"
	@echo "  make clean          - Clean temporary files"
	@echo "  make help           - Show this menu"

setup:
	@echo "Setting up environment..."
	@[ -f "$(ENV_FILE)" ] || cp .env.example $(ENV_FILE)
	@echo "✓ .env file created (review variables if needed)"

install: setup
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt
	@echo "✓ Dependencies installed"

edit: setup
	@echo "Installing in editable mode..."
	$(PYTHON) -m pip install -e ".[dev]"
	@echo "✓ Editable install complete"

# Train model - works on Linux and Windows (uses python, not PYTHONPATH)
train-model:
	@echo "Training model..."
	@$(PYTHON) -c "import sys, os; sys.path.insert(0, os.path.abspath('.')); from scripts.train_model import main; main()"
	@echo "✓ Model trained"

lint:
	@echo "Running linter..."
	$(PYTHON) -m pylint src/ --max-line-length=100
	@echo "✓ Linting completed"

format:
	@echo "Formatting code..."
	$(PYTHON) -m black src/ tests/
	@echo "✓ Code formatted"

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest tests/ -v
	@echo "✓ Tests completed"

test-cov:
	@echo "Running tests with coverage..."
	$(PYTHON) -m pytest tests/ -v --cov=src --cov-report=html
	@echo "✓ Coverage generated at htmlcov/index.html"

run:
	@echo "Starting API at http://localhost:$(PORT)"
	@echo "Docs: http://localhost:$(PORT)/docs"
	$(PYTHON) -m uvicorn src.api.main:app --reload --host 0.0.0.0 --port $(PORT)

docker-build:
	@echo "Building Docker image..."
	docker-compose build
	@echo "✓ Image built"

docker-run:
	@echo "Starting Docker containers..."
	docker-compose up -d
	@echo "✓ Containers started. API at http://localhost:8000"

docker-stop:
	@echo "Stopping containers..."
	docker-compose down
	@echo "✓ Containers stopped"

clean:
	@echo "Cleaning temporary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.log" -delete 2>/dev/null || true
	@echo "✓ Cleanup completed"
