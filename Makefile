install: 
	# install Commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format: 
	# format Commands
	black *.py &&\
		black */*.py
lint: 
	# pylint Commands
	pylint --disable=R,C *.py */*.py
test:
	# test Commands
	python3 -m pytest -vv --cov=lib test*.py
build: 
	# build Commands for docker containers
deploy:
	# deploy Commands
all: 
	install format lint test deploy