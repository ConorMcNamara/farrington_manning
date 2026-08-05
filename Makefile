.PHONY: help install install-dev format lint type-check test test-cov clean pre-commit-install pre-commit-run all

help:
	@echo "Available commands:"
	@echo "  make install            - Install project dependencies"
	@echo "  make install-dev        - Install development dependencies"
	@echo "  make format             - Format code with ruff"
	@echo "  make lint               - Lint code with ruff"
	@echo "  make type-check         - Run type checking with zuban"
	@echo "  make test               - Run tests with pytest"
	@echo "  make test-cov           - Run tests with coverage report"
	@echo "  make pre-commit-install - Install pre-commit hooks"
	@echo "  make pre-commit-run     - Run pre-commit hooks on all files"
	@echo "  make clean              - Remove generated files and caches"
	@echo "  make all                - Run format, lint, type-check, and test"

install:
	uv sync --no-dev

install-dev:
	uv sync

format:
	uv run ruff format src tests
	uv run ruff check --fix src tests

lint:
	uv run ruff check src tests

type-check:
	uv run zuban check src

test:
	uv run pytest

test-cov:
	uv run pytest --cov=farrington_manning --cov-report=term-missing --cov-report=html

pre-commit-install:
	uv run pre-commit install

pre-commit-run:
	uv run pre-commit run --all-files

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	rm -rf .pytest_cache
	rm -rf .zuban_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

all: format lint type-check test
