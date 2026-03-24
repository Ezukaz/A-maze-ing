# Variables
program = a_maze_ing.py
debugger = pdb
package = pydantic mypy
config = config.txt
cache_dir = __pycache__ .mypy_cache mazegen.egg-info
output_file := $(shell grep '^OUTPUT_FILE=' config.txt | cut -d '=' -f2)
mypy_flags =	--warn-return-any \
				--warn-unused-ignores \
				--ignore-missing-imports \
				--disallow-untyped-defs \
				--check-untyped-defs

# Install dependencies
install:
	pip3 install $(package)

# Run the program
run:
	python3 $(program) $(config)

# Debug the program
debug:
	python3 -m $(debugger) $(program)

# Clean up caches and .pyc files
clean:
	rm -rf $(cache_dir)
	rm -f $(output_file)

# Lint the code with flake8 and mypy
lint:
	flake8 .
	mypy . $(mypy_flags)

# Strict linting
lint-strict:
	flake8 .
	mypy . --strict

install-build:
	pip3 install build

build:
	python3 -m build

.PHONY: install run debug clean lint lint-strict install-build build