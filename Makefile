# Makefile

.PHONY: help clean clean-pyc clean-build clean-test test test-cov lint format docs docker-build docker-run install dev-install

help:
	@echo "clean - remove all build, test, and coverage artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "test - run tests quickly with the default Python"
	@echo "test-cov - run tests with coverage report"
	@echo "lint - check style with flake8"
	@echo "format - format code with black"
	@echo "docs - generate and open HTML documentation"
	@echo "docker-build - build the Docker image"
	@echo "docker-run - run the services defined in docker-compose.yml"
	@echo "install - install the package"
	@echo "dev-install - install development dependencies"
	@echo "server - run the API server"
	@echo "client - run the web client"

clean: clean-pyc clean-build clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-test:
	rm -fr .tox/
	rm -fr .pytest_cache
	rm -fr .coverage
	rm -fr htmlcov/

test:
	pytest

test-cov:
	pytest --cov=my_library tests/

lint:
	flake8 my_library tests

format:
	black my_library tests

docs:
	cd docs && mkdocs build
	cd docs && mkdocs serve

docker-build:
	cd docker && docker-compose build

docker-run:
	cd docker && docker-compose up

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt

server:
	uvicorn api:app --reload --port 5555

client:
	python web.py