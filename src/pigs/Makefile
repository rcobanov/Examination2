#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:


# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-all: clean clean-doc


# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	-pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest discover . "*.py" -b

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover . "*.py" -b
	coverage html
	coverage report -m "dice.py" "bot.py" "player.py" "highscore.py"

test: lint coverage


# ---------------------------------------------------------
# Work with generating documentation.
#
.PHONY: pydoc
pydoc:
	install -d doc/pydoc
	$(PYTHON) -m pydoc -w "dice" "bot" "player" "highscore" "dice_test" "bot_test" "player_test" "highscore_test"
	mv *.html doc/pydoc

pdoc:
	rm -rf doc/pdoc
	pdoc --html -o doc/pdoc .

doc: pdoc pyreverse pydoc sphinx

pyreverse:
	install -d doc/pyreverse
	pyreverse *.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot
	ls -l doc/pyreverse


# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc . -a

radon-mi:
	@$(call MESSAGE,$@)
	radon mi .

radon-raw:
	@$(call MESSAGE,$@)
	radon raw .

radon-hal:
	@$(call MESSAGE,$@)
	radon hal .

metrics: radon-cc radon-mi radon-raw radon-hal


# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	bandit -r .
