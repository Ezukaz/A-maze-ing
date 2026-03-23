# Variables
program = a_maze_ing.py
debugger = pdb
package = pydantic mypy
config = config.txt
cache_dir = __pycache__ .mypy_cache
output_file = *.
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
	rm -rf $(cache_dir) $(output_file)
	find . -name "*.txt" ! -name "config.txt" -delete

# Lint the code with flake8 and mypy
lint:
	flake8 . ; mypy . $(mypy_flags)

# Strict linting
lint-strict:
	flake8 . ; mypy . --strict

.PHONY: install run debug clean lint lint-strict