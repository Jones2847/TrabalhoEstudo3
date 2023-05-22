install:
	python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt

test:
	python3 -m pytest -vv test_multiplier.py

format:
	python3 -m black *.py

lint:
	python3 -m pylint multiplier.py --disable=R,C

all: install lint test
