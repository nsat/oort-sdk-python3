PYTHON := python3

.PHONY: setup test format clean

setup:
	poetry env use $(PYTHON)
	poetry check
	poetry install

test:
	poetry run pytest test

format:
	poetry run black test


clean:
	rm -rf .pytest_cache
