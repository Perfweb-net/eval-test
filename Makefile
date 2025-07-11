install:
	pip install -r requirements.txt

test:
	pytest

test-unit:
	pytest -m unit

test-integration:
	pytest -m integration

coverage:
	pytest --cov=src/task_manager --cov-report=html --cov-report=term-missing

clean:
	rm -rf .pytest_cache htmlcov

lint:
	python3 -m py_compile src/task_manager/*.py

all: install lint test coverage