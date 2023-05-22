install:
	python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt

test:
	python3 -m pytest -vv test_my_code.py

format:
	python3 -m black *.py

lint:
	python3 -m pylint my_code.py --disable=R,C

all: install lint test