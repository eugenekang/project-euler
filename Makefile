WORKING_DIR:=src
BUILD_DIR:=${WORKING_DIR}/build
VENV:=${BUILD_DIR}/venv
PYTHON:=${VENV}/bin/python3
PYTHON_TEST:=${VENV}/bin/python3
PIP:=${VENV}/bin/pip3

all : lint

lint : deps
	${PYTHON} -m flake8

deps: venv requirements.txt
	${PIP} install -Ur requirements.txt --extra-index-url https://pypi.org/simple

clean:
	rm -rf ${BUILD_DIR}/
	find . -name "*.py[co]" -delete
	find . -name "__pycache__" -delete
	find . -name ".pytest_cache" -delete

test: venv
	src/build/venv/bin/pytest tests/unit/src/euler/test_euler_problems.py
	src/build/venv/bin/pytest tests/unit/src/support/test_math.py
	src/build/venv/bin/pytest tests/unit/src/support/test_custom_functions.py

venv:
	test -d ${VENV} || python3 -m venv ${VENV}/

run: deps
	${PYTHON} -m src.main
